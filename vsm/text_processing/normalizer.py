import unicodedata


class TextNormalizer:
    def normalize(self, text: str) -> str:
        normalized_text = text.lower()
        return self._remove_accents(normalized_text)

    def _remove_accents(self, text: str) -> str:
        normalized = unicodedata.normalize("NFD", text)
        return "".join(char for char in normalized if unicodedata.category(char) != "Mn")
