from nltk.stem.snowball import SnowballStemmer

from vsm.text_processing.languages import LanguageConfig


class Stemmer:
    def __init__(self, language: LanguageConfig) -> None:
        self.language = language
        self._stemmer = SnowballStemmer(language.nltk_name)

    def stem_tokens(self, tokens: list[str]) -> list[str]:
        return [self._stemmer.stem(token) for token in tokens]
