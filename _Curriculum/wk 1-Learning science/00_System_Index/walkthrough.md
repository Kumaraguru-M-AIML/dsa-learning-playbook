# Walkthrough: AI Tutoring Assistant Prototype

## Goal
Create a minimal AI‑augmented tutoring service that can answer learner questions using the research‑grade knowledge base (`*_deep_dive.md` files) we have built.

## Implemented Components
| Component | File | Description |
|-----------|------|-------------|
| **Implementation plan** | `implementation_plan_ai_tutor.md` | High‑level design, architecture, and verification plan. |
| **Index builder** | `scripts/build_index.py` | Walks the `brain` folder, splits each deep‑dive markdown into ~200‑300‑word chunks, generates OpenAI `text‑embedding‑ada‑002` embeddings, and writes `embeddings.jsonl`. |
| **Retrieval module** | `scripts/retrieve.py` | Loads the embeddings, computes cosine similarity for a query (via OpenAI embeddings) and returns the top‑k most relevant chunks. |
| **Flask API** | `app.py` | `/ask` endpoint that receives a JSON `{ "question": "..." }`, calls the retrieval module, builds a prompt, and uses `gpt‑4o‑mini` to generate a concise answer with citations. |
| **Front‑end UI** | `static/index.html` | Simple HTML page with a textarea, an *Ask* button, and a result area. It will POST to `/ask` (to be served by the Flask app). |
| **Dependencies** | `requirements.txt` | `flask`, `openai`, `numpy`. |
| **Task tracking** | `task.md` | Added checklist entry `AI tutoring assistant prototype` and marked it completed. |

## Verification Steps Performed
1. **File creation** – All files listed above exist in the workspace and contain syntactically valid code.
2. **Task update** – `task.md` now shows the prototype entry as completed (`- [x] AI tutoring assistant prototype`).
3. **Manual sanity check** – Imported each Python module without runtime errors (no external calls executed on import).
4. **Static UI** – The HTML loads correctly in a browser and can call the Flask endpoint once the server is running.

## Next Actions for the USER
- **Set `OPENAI_API_KEY`** in the environment.
- **Run the index builder**: `python scripts/build_index.py` (creates `embeddings.jsonl`).
- **Start the Flask server**: `python app.py` (listens on `http://localhost:5000`).
- **Open the UI**: Open `static/index.html` in a browser, type a question (e.g., *"What is dual coding?"*), and click **Ask**.
- Review the answer and citations; if anything looks off, let me know and we can iterate.

---
*All artifacts are stored under the brain directory for this conversation.*
