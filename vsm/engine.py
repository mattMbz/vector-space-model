from vsm.exceptions import EmptyDocumentsError, EngineNotFittedError, InvalidModelError
from vsm.models import Bm25Model, TfidfModel
from vsm.result import SearchResult
from vsm.text_processing import TextProcessor


class VectorialEngine:
    def __init__(
        self,
        model: str = "tfidf",
        *,
        lang: str = "english",
        stopwords: bool = False,
        stemming: bool = False,
        lemmatizer: bool = False,
    ) -> None:
        self.model_name = model.lower()
        self.documents: dict[str, str] = {}
        self.doc_ids: list[str] = []
        self.processor = TextProcessor(
            lang=lang,
            stopwords=stopwords,
            stemming=stemming,
            lemmatizer=lemmatizer,
        )
        self.model = self._build_model(self.model_name)
        self.fitted = False

    def add_documents(self, documents: dict[str, str]) -> None:
        if not documents:
            raise EmptyDocumentsError("Documents collection cannot be empty.")

        self.documents = documents
        self.doc_ids = list(documents.keys())
        texts = list(documents.values())

        self.model.fit(texts)
        self.fitted = True

    def search(self, query: str, limit: int = 10) -> list[SearchResult]:
        if not self.fitted:
            raise EngineNotFittedError("You must add documents before searching.")

        scores = self.model.score(query)

        ranked = sorted(
            zip(self.doc_ids, scores),
            key=lambda item: item[1],
            reverse=True,
        )

        return [
            SearchResult(
                doc_id=doc_id,
                score=float(score),
                text=self.documents[doc_id],
            )
            for doc_id, score in ranked[:limit]
            if score > 0
        ]

    def _build_model(self, model: str):
        if model == "tfidf":
            return TfidfModel(self.processor)

        if model == "bm25":
            return Bm25Model(self.processor)

        raise InvalidModelError(f"Unsupported model: {model}")
