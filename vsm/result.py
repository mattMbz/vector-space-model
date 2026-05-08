from dataclasses import dataclass


@dataclass(frozen=True)
class SearchResult:
    doc_id: str
    score: float
    text: str