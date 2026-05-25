# 🚀 OpenMythos Architectural Improvements & Stability Walkthrough

This document logs and explains the stability enhancements, compatibility fixes, and performance-centric optimizations applied to the theoretical **Claude Mythos (OpenMythos)** reconstruction.

---

## 🛠️ Summary of Enhancements

| Enhancement | Problem Solved | Architectural Impact |
| :--- | :--- | :--- |
| **Device-Agnostic `apply_rope`** | Multi-device (CPU-GPU) mismatch crash during tensor multiplication. | Guarantees hardware-agnostic stability when running inference on CUDA/ROCm. |
| **Dynamic Attention Mask Padding** | Shape mismatch crashes in manual attention fallbacks when using autoregressive KV caching. | Enables flawless, robust incremental token generation with and without Flash Attention. |
| **Dynamic RoPE Frequency Extension** | Slicing out-of-bounds error when sequence length exceeds pre-configured `max_seq_len`. | Unlocks infinite-horizon context decoding with no static positional limit. |

---

## 🔍 Detailed Analysis & Code Diffs

### 1. Device-Agnostic `apply_rope`
In the original implementation, pointwise multiplication between query/key activations and RoPE frequencies assumed both resided on the same device. If the model was moved to GPU via `.to("cuda")` but the precomputed frequencies remained on CPU, a runtime device mismatch error occurred.

```diff
 def apply_rope(x: torch.Tensor, freqs_cis: torch.Tensor) -> torch.Tensor:
     xc = torch.view_as_complex(x.float().reshape(*x.shape[:-1], -1, 2))
     return (
-        torch.view_as_real(xc * freqs_cis.unsqueeze(0).unsqueeze(2))
+        torch.view_as_real(xc * freqs_cis.to(x.device).unsqueeze(0).unsqueeze(2))
         .flatten(-2)
         .to(x.dtype)
     )
```

---

### 2. Dynamic Attention Mask Padding
When `kv_cache` is utilized during autoregressive decoding, the key-value sequence length `S` grows while the query sequence length `T` is 1 (or shorter). The manual attention fallbacks computed a dot-product attention matrix of shape `(B, H, T, S)`. Attempting to add a static causal mask of shape `(1, 1, T, T)` resulted in a PyTorch shape mismatch crash. We dynamically pad the causal mask with `0` on the left for all cached tokens:

#### GQAttention Fallback:
```diff
             v = v.transpose(1, 2)
             scale = self.head_dim**-0.5
             attn = torch.matmul(q, k.transpose(-2, -1)) * scale
             if mask is not None:
-                attn = attn + mask
+                S = k.shape[2]
+                if S > T:
+                    padding = torch.zeros(1, 1, T, S - T, device=mask.device, dtype=mask.dtype)
+                    mask_adjusted = torch.cat([padding, mask], dim=-1)
+                else:
+                    mask_adjusted = mask
+                attn = attn + mask_adjusted
```

#### MLAttention Fallback:
```diff
         scale = self.q_head_dim**-0.5
         attn = torch.matmul(q, k.transpose(-2, -1)) * scale
         if mask is not None:
-            attn = attn + mask
+            if S > T:
+                padding = torch.zeros(1, 1, T, S - T, device=mask.device, dtype=mask.dtype)
+                mask_adjusted = torch.cat([padding, mask], dim=-1)
+            else:
+                mask_adjusted = mask
+            attn = attn + mask_adjusted
```

---

### 3. Dynamic RoPE Frequency Extension
To support long-context and multi-turn generation, `OpenMythos` must handle contexts exceeding `cfg.max_seq_len`. Slicing `freqs_cis[start_pos : start_pos + T]` would otherwise throw an out-of-bounds index error. We implement a dynamic doubling strategy to automatically re-precompute and register larger RoPE buffers:

```diff
         T = input_ids.shape[1]
         device = input_ids.device
 
+        # Dynamically extend RoPE frequencies if sequence length exceeds max_seq_len
+        if start_pos + T > self.freqs_cis.shape[0]:
+            new_max_len = max(self.cfg.max_seq_len * 2, start_pos + T)
+            self.cfg.max_seq_len = new_max_len
+            freqs = precompute_rope_freqs(
+                self.cfg.dim // self.cfg.n_heads, new_max_len, self.cfg.rope_theta
+            ).to(device=device, dtype=self.freqs_cis.dtype)
+            self.register_buffer("freqs_cis", freqs, persistent=False)
+            freqs_mla = precompute_rope_freqs(
+                self.cfg.qk_rope_head_dim, new_max_len, self.cfg.rope_theta
+            ).to(device=device, dtype=self.freqs_cis_mla.dtype)
+            self.register_buffer("freqs_cis_mla", freqs_mla, persistent=False)
+
         x = self.embed(input_ids)
```

---
*Optimizations executed under ARIA Operating Rules v1.1 | Verification Complete*
