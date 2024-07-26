import llm
from ollama import embeddings

MAX_LENGTH = 8192


@llm.hookimpl
def register_embedding_models(register):
    for model_id in (
        "mxbai-embed-large",
        "nomic-embed-text",
        "all-minilm",
    ):
        register(OllamaEmbeddingModel(model_id))


class OllamaEmbeddingModel(llm.EmbeddingModel):
    def __init__(self, model_id):
        self.model_id = model_id
        self._model = None

    def embed_batch(self, texts):
        if self._model is None:
            self._model=embeddings
        # self.embeddings(model="mxbai-embed-large", prompt=d)
        results = [self._model(model=self.model_id, prompt=text[:MAX_LENGTH])["embedding"] for text in texts]
        return (list(map(float, result)) for result in results)
