class VectorialEngineError(Exception):
    """Base exception for VectorialEngine."""

class EmptyDocumentsError(VectorialEngineError):
    """Raised when trying to add an empty document collection."""

class EngineDocumentsError(VectorialEngineError):
    """Raised when trying to add an empty document collection."""

class EngineNotFittedError(VectorialEngineError):
    """Raised when searching before adding documents."""

class InvalidModelError(VectorialEngineError):
    """Raised when an unsupported retrieval model is selected."""

class InvalidLanguageError(VectorialEngineError):
    """Raised when an unsupported language is selected."""

class MissingLanguageResourceError(VectorialEngineError):
    """Raised when a language resource is not installed."""
