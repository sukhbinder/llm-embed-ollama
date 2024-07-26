from click.testing import CliRunner
from llm.cli import cli
import llm


def test_ollama_embed_small():
    model = llm.get_embedding_model("all-minilm")
    floats = model.embed("hello world")
    assert len(floats) == 384
    assert all(isinstance(f, float) for f in floats)


def test_ollama_embed_long_string():
    model = llm.get_embedding_model("all-minilm")
    outputs = list(model.embed_multi(["a" * 9000, "two"]))
    for floats in outputs:
        assert len(floats) == 384


def test_ollama_embed_multi(tmpdir):
    db_path = str(tmpdir / "test.db")
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "embed-multi",
            "-m",
            "all-minilm",
            "test",
            "-",
            "-d",
            db_path,
        ],
        input='[{"id": "a", "text": "abc"}]',
        catch_exceptions=False,
    )
    assert result.exit_code == 0
