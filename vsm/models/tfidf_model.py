from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vsm.text_processing import TextProcessor


class TfidfModel:
    def __init__(self, processor: TextProcessor | None = None) -> None:
        self.processor = processor or TextProcessor()
        self.vectorizer = TfidfVectorizer()
        self.document_matrix = None

    def fit(self, documents: list[str]) -> None:
        processed_documents = [
            self.processor.process_document(document) for document in documents
        ]
        self.document_matrix = self.vectorizer.fit_transform(processed_documents)
    
    def score(self, query: str) -> list[float]:
        processed_query = self.processor.process_document(query)
        query_vector = self.vectorizer.transform([processed_query])
        scores = cosine_similarity(query_vector, self.document_matrix).flatten()
        return scores.tolist()
