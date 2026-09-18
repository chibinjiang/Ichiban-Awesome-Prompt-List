from pathlib import Path

from ichiban_prompt.core import validate_all, search_prompts


ROOT = Path(__file__).parents[1]


def test_prompt_validation():
    issues = validate_all(ROOT)
    assert issues == [], [str(issue) for issue in issues]


def test_search():
    results = search_prompts(ROOT, "SQLAlchemy")
    assert results
