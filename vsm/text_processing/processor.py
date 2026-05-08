from vsm.text_processing.languages import get_language_config
from vsm.text_processing.lemmatizer import Lemmatizer
from vsm.text_processing.normalizer import TextNormalizer
from vsm.text_processing.stemmer import Stemmer
from vsm.text_processing.stopwords import StopWordsRemover
from vsm.text_processing.tokenizer import Tokenizer


class TextProcessor:
    def __init__(
        self,
        *,
        lang: str = "english",
        stopwords: bool = False,
        stemming: bool = False,
        lemmatizer: bool = False,
    ) -> None:
        self.language = get_language_config(lang)
        self.use_stopwords = stopwords
        self.use_stemming = stemming
        self.use_lemmatizer = lemmatizer
        self.normalizer = TextNormalizer()
        self.tokenizer = Tokenizer()
        self.stopwords_remover = (
            StopWordsRemover(self.language) if self.use_stopwords else None
        )
        self.stemmer = Stemmer(self.language) if self.use_stemming else None
        self.lemmatizer = Lemmatizer(self.language) if self.use_lemmatizer else None

    def process(self, text: str) -> list[str]:
        normalized = self.normalize(text)
        tokens = self.tokenizer.tokenize(normalized)

        if self.stopwords_remover is not None:
            tokens = self.stopwords_remover.remove(tokens)

        if self.stemmer is not None:
            tokens = self.stemmer.stem_tokens(tokens)

        if self.lemmatizer is not None:
            tokens = self.lemmatizer.lemmatize_tokens(tokens)

        return tokens

    def normalize(self, text: str) -> str:
        return self.normalizer.normalize(text)

    def tokenize(self, text: str) -> list[str]:
        return self.process(text)

    def process_document(self, text: str) -> str:
        return " ".join(self.process(text))
