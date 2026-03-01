
# GitHub Copilot Demo — Python Track

A ready-to-run demo repo to teach beginners how to use **GitHub Copilot** with Python in ~60 minutes.

## ✅ What you'll demonstrate
- Inline code generation from comments
- Copilot Chat for explaining, refactoring, and documenting code
- Generating **unit tests** with `pytest` and iterating on failures
- A small **data task** using `pandas` and simple plotting
- Drafting repo docs: README sections and PR templates

> Copilot suggests; **you** decide. Always read, run, and test the code.

---

## 🧰 Setup

### Option A: Local
1. Ensure you have **Python 3.10+** and **Git** installed.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Open the folder in **VS Code**. When prompted, install recommended extensions (Copilot, Copilot Chat, Python).

### Option B: GitHub Codespaces (recommended for classes)
- Open this repo in Codespaces → you'll get VS Code in the browser with extensions ready.

---

## ▶️ Quick start

Run tests (they will evolve during the demo):
```bash
pytest -q
```

Run the data task script (you'll complete it with Copilot):
```bash
python src/python/data_tasks.py
```

---

## 🧪 Demo flow (short version)
1. **Inline generation** in `src/python/calculator.py` from natural language comments.
2. **Explain & refactor** with Copilot Chat (select code → Ask Copilot).
3. **Generate tests** in `src/python/test_calculator.py` and run `pytest`.
4. **Data task** in `src/python/data_tasks.py` reading `data/sales.csv` with `pandas`.
5. **Docs & hygiene**: have Copilot draft a "Getting Started" and a PR template.

Detailed step-by-step prompts live in **/exercises**.

---

## 🛡️ Responsible use checklist
- No secrets/PII in prompts or code.
- Review suggestions for correctness and security.
- Prefer standard library or vetted deps; pin versions for production.

---

## ℹ️ Troubleshooting
- If Copilot suggestions look irrelevant, ensure the **file is saved** and you’ve provided a **clear comment** near the cursor.
- In Chat, **select code** before asking to increase context quality.

Happy teaching! 🧑‍🏫🤖
