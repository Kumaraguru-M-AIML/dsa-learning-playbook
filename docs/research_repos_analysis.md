# ⚙️ Research, Development, and Analysis (RDA) — Repo Intelligence

> **System Context:** In accordance with **ARIA Operating Rules (Section 0 & 3D)**, this document maps out the essential components of the four targeted repositories, filters out unnecessary lockfiles/bloat, and structures them into the workspace.

---

## 📊 Repo Assessment Matrix (RDA)

| Repository | Purpose | Essential Components (Keep) | Bloat / Unneeded (Prune) | Value to Workspace |
| :--- | :--- | :--- | :--- | :--- |
| **`karpathy/autoresearch`** | AI-driven literature research & summarization pipeline. | `prepare.py`, `train.py`, `analysis.ipynb`, `program.md`, `README.md` | `uv.lock` (443KB, lockfile), `.python-version` | High. Powers research agent loops and paper ingestion patterns. |
| **`karpathy/nanoGPT`** | Production-grade minimal GPT transformer in PyTorch. | `model.py`, `train.py`, `sample.py`, `bench.py`, `configurator.py`, `config/`, `data/shakespeare/`, `data/shakespeare_char/`, `assets/`, `*.ipynb` | `.gitattributes`, large dataset caches. | Very High. Provides the reference architecture for lightweight custom training. |
| **`karpathy/nn-zero-to-hero`** | Educational notebooks for neural net foundations (micrograd/makemore). | `lectures/micrograd/`, `lectures/makemore/`, `README.md` | Course meta-files, large video links. | High. Core theoretical mental models for deep learning architecture. |
| **`lucasastorian/llmwiki`** | LLM-powered wiki engine, Supabase db migrations, and local MCP server. | `mcp/` (local server scripts), `converter/` (main.py), `shared/`, `web/src/` (core logic), `README.md` | `package-lock.json` (403KB), `tsconfig.tsbuildinfo` (480KB), full dependencies. | Medium-High. Blueprint for exposing wiki structures via Model Context Protocol. |

---

## 🎯 Target Execution Plan

1. **Create Destination**: Initialize a clean directory `c:\Master  db\R&D workspace\NEW\research_repos\`.
2. **Transfer Autoresearch**: Copy core code (`prepare.py`, `train.py`, `analysis.ipynb`, `program.md`, `README.md`) to `research_repos\autoresearch\`.
3. **Transfer NanoGPT**: Copy core code (`model.py`, `train.py`, `sample.py`, `bench.py`, `configurator.py`, `config\`, `data\`, `assets\`, `*.ipynb`, `README.md`) to `research_repos\nanoGPT\`.
4. **Transfer NN-Zero-to-Hero**: Copy lectures (`lectures\makemore\`, `lectures\micrograd\`, `README.md`) to `research_repos\nn-zero-to-hero\`.
5. **Transfer LLMWiki**: Copy core engine and MCP server (`mcp\`, `converter\`, `shared\`, `web\src\`, `README.md`) to `research_repos\llmwiki\`.
6. **Clean Up**: Delete the `temp_downloads\` folder containing raw ZIPs and raw unzipped folders.

---
*Analysis completed under ARIA Operating Rules v1.1 | Correctness > Speed | Token Economy Active*
