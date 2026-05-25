# AI Tutoring Assistant Prototype

## Goal
Create a minimal AI‑augmented tutoring service that can answer learner questions using the research‑grade knowledge base you have built (neuroscience, principles, memory‑encoding techniques, etc.). The service will retrieve relevant passages from the markdown artifacts, embed them, and feed them to an LLM to generate answers with citations.

## Architecture Overview
1. **Data Ingestion**
   - Scan the `brain` directory for all `*_deep_dive.md` files.
   - Split each file into logical chunks (e.g., by heading) of ~200‑300 words.
   - Store each chunk with metadata: `source_file`, `heading`, `text`.
2. **Embedding Layer**
   - Use OpenAI `text-embedding-ada-002` (or equivalent) to generate a vector for each chunk.
   - Persist embeddings in a simple JSON‑lines file (`embeddings.jsonl`).
3. **Retrieval Service**
   - Simple cosine‑similarity search over the embeddings to return top‑k (e.g., 5) most relevant chunks for a user query.
4. **LLM Generation**
   - Prompt template includes the retrieved chunks and asks the model to answer the user query, citing the source file and heading.
   - Use OpenAI `gpt-4o-mini` (or the model you are running) via API.
5. **Web API**
   - Flask app exposing `/ask` endpoint (POST JSON `{ "question": "..." }`).
   - Returns `{ "answer": "...", "sources": ["file.md#Heading"] }`.
6. **Front‑End** (optional for MVP)
   - Minimal HTML page with a text box, submit button, and area to display answer and source links.

## Implementation Steps
| Step | Action | Files Modified/Created |
|------|--------|------------------------|
| 1 | Write a Python script `scripts/build_index.py` that scans the `brain` folder, splits markdown, generates embeddings, and writes `embeddings.jsonl`. | `scripts/build_index.py` |
| 2 | Write a retrieval module `scripts/retrieve.py` with a function `search(query, k=5)` returning top chunks. | `scripts/retrieve.py` |
| 3 | Write the Flask API `app.py` that loads embeddings on start, uses `retrieve.search`, calls OpenAI LLM, and returns JSON. | `app.py` |
| 4 | Create a tiny front‑end `static/index.html` and `static/main.js` that POSTs to `/ask`. | `static/index.html`, `static/main.js` |
| 5 | Add a `requirements.txt` listing `flask`, `openai`, `tiktoken`, `numpy`, `scikit-learn`. | `requirements.txt` |
| 6 | Update `task.md` to mark the AI tutoring assistant task as in‑progress and add a deliverable checklist. |

## Verification Plan
1. **Unit Test for Retrieval**
   - Create `tests/test_retrieve.py` that loads a small sample embedding file (generated from a subset of markdown) and asserts that a known query returns a chunk containing an expected keyword.
   - Run with `pytest -q`. (Will add the test file in step 6.)
2. **Manual End‑to‑End Test**
   - Start the Flask server: `python app.py`.
   - Open `http://localhost:5000` in a browser, ask a question such as "What is the spacing effect?".
   - Verify the answer is coherent, cites `principles_rules_deep_dive.md#Spacing Effect`, and the source link opens the correct markdown section.
3. **Smoke Test for Embedding Build**
   - Run `python scripts/build_index.py` and ensure `embeddings.jsonl` is created and contains >0 lines.
4. **Code Review**
   - All new files will be listed in the implementation plan for the user to review.

## Risks & Mitigations
- **Rate limits on OpenAI API** – Use a small batch for MVP; can switch to local embeddings later.
- **Citation accuracy** – Prompt forces the model to include the `source_file#heading` string; we will post‑process to ensure it matches known metadata.
- **Performance** – For a prototype, a linear scan over embeddings is acceptable (<1 s for a few hundred chunks).

## Next Steps (after approval)
- Implement the scripts and API.
- Run the verification steps.
- Package the prototype (Dockerfile optional) for easy deployment.

---
*Please review this implementation plan. Once approved, I will move to execution mode and create the required files.*
