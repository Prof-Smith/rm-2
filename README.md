# Applied Risk Management Lab

A complete eight-module MkDocs course repository built around decision-first, case-based, quantitative risk education.

## Local preview
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

## Publish
Push to a GitHub repository with `main` as the default branch, then enable GitHub Pages with **GitHub Actions** as the source. The included workflow builds in strict mode and deploys the generated site.

## Repository principles
- One essential question per module
- Frame → Learn → Investigate → Model → Decide
- One principal decision artifact per module
- Common claim/evidence/uncertainty/action/reversal standard
- Synthetic numerical data are clearly labeled

## Structure
- `docs/modules`: student pathways
- `docs/cases`: compact investigations
- `docs/labs`: executable notebooks
- `docs/assets`: design assets
- `data`: data documentation
- `.github/workflows`: Pages deployment
