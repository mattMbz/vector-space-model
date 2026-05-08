from rank_bm25 import BM25Okapi
from vsm.text_processing import TextProcessor


class Bm25Model:
    def __init__(self, processor: TextProcessor | None = None) -> None:
        self.processor = processor or TextProcessor()
        self.model: BM25Okapi | None = None

    def fit(self, documents: list[str]) -> None:
        tokenized_documents = [self.processor.process(doc) for doc in documents]
        self.model = BM25Okapi(tokenized_documents)

    def score(self, query: str) -> list[float]:
        tokenized_query = self.processor.process(query)
        scores = self.model.get_scores(tokenized_query)
        return scores.tolist()
