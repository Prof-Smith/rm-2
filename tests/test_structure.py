from pathlib import Path

def test_required_files():
    r = Path(__file__).parents[1]
    assert (r / "mkdocs.yml").exists()
    assert (r / ".github/workflows/pages.yml").exists()
    for n in range(1, 9):
        assert (r / f"docs/modules/module-{n}.md").exists()
        assert (r / f"docs/labs/module-{n}.md").exists()
