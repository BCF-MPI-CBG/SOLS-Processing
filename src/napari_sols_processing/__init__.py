try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
from ._functions import some_processing_function

__all__ = (
    "some_processing_function",
)
