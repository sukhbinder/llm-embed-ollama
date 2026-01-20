import llm
import pytest
import os

IN_GITHUB_ACTIONS = os.environ.get("GITHUB_ACTIONS") == "true"

@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Not running on GitHub")
def test_ollama_embed_with_prefix_changes_output():
    model = llm.get_embedding_model("all-minilm")

    # simulate llm injecting prefix
    setattr(model, "prefix", "query: ")
    v1 = model.embed("hello world")

    # no prefix
    setattr(model, "prefix", None)
    v2 = model.embed("hello world")

    assert len(v1) == len(v2)
    assert v1 != v2
