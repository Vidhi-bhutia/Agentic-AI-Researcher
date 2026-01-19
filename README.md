# AI Researcher (Demo)

Agentic AI automation that searches arXiv, reasons over papers, and drafts a research-style PDF via LaTeX. **Demo/prototype only — not for real publishing. Validate all content manually.**

## What’s Included
- Agentic workflow (search, read, draft)
- Gemini LLM integration
- LaTeX → PDF via **Tectonic**
- Example output: `Example of Generated Doc/AI_Researcher.pdf`

## Prerequisites
- Python 3.10+ (recommended)
- **uv** (Python dependency manager)
- **Tectonic** (LaTeX engine)
- **Gemini API key**

## Install uv
```bash
# Recommended
pipx install uv

# Or
pip install uv
```

## Install Tectonic
- **macOS (Homebrew)**:
  ```bash
  brew install tectonic
  ```
- **Linux (snap)**:
  ```bash
  sudo snap install --classic tectonic
  ```
  If snap isn’t available, see: https://tectonic-typesetting.github.io
- **Windows**: Download installer from https://tectonic-typesetting.github.io and ensure `tectonic` is on PATH.

Verify:
```bash
tectonic --version
```

## Environment Variables
Create a `.env` in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

## Install & Sync Dependencies
From project root:
```bash
uv sync
```

## Run the Agent
Adjust the entry point if yours differs:
```bash
uv run python main.py
```
or
```bash
uv run python -m ai_agent
```

## Generate / Rebuild PDF Manually (Tectonic)
If a LaTeX file (e.g., `output.tex`) is produced and you want to recompile:
```bash
tectonic output.tex -o output.pdf
```

## Example Output
- `Example of Generated Doc/AI_Researcher.pdf` — AI-generated sample PDF included for reference.

## Notes & Limitations
- Demo/prototype; not production-ready. Do not use as-is for formal publication.
- Check citations, math, and text before sharing.
- Respect Gemini API usage limits and policies.

## Troubleshooting
- `tectonic` not found: reinstall and confirm PATH (`tectonic --version`).
- Missing deps: rerun `uv sync`.
- `.env` not loading: ensure it’s in project root and names match exactly.