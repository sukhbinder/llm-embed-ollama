import llm
from ollama import embeddings

MAX_LENGTH = 8192


@llm.hookimpl
def register_embedding_models(register):
    for model_id in (
        "mxbai-embed-large",
        "nomic-embed-text",
        "all-minilm",
        "bge-large",
        "bge-m3"
        
    ):
        register(OllamaEmbeddingModel(model_id))


class OllamaEmbeddingModel(llm.EmbeddingModel):
    def __init__(self, model_id):
        self.model_id = model_id
        self._model = None

    def _apply_prefix_suffix(self, text: str) -> str:
        prefix = getattr(self, "prefix", None)
        suffix = getattr(self, "suffix", None)

        if prefix:
            text = f"{prefix}{text}"
        if suffix:
            text = f"{text}{suffix}"
        return text

    def embed_batch(self, texts):
        if self._model is None:
            self._model=embeddings
        # self.embeddings(model="mxbai-embed-large", prompt=d)
        processed = [
            self._apply_prefix_suffix(text)[:MAX_LENGTH]
            for text in texts
        ]

        results = [
            self._model(model=self.model_id, prompt=text)["embedding"]
            for text in processed
        ]
        return (list(map(float, result)) for result in results)
