# Applied Risk Management Lab v2

A complete eight-module MkDocs course built around a consistent three-part architecture:

1. Clean professional case
2. Scaffolded quantitative lab
3. Submission studio

## Deploy

The repository includes `.github/workflows/pages.yml`. Push the extracted repository contents with Git, enable GitHub Pages with **GitHub Actions** as the source, and the workflow will build the site with `mkdocs build --strict`.

## Validate locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs build --strict
mkdocs serve
```
