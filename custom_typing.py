from typing import Generic, TypeVar
from constants import LOW, MEDIUM, HIGH

class _Quality:
    LOW : str
    MEDIUM : str
    HIGH : str

T = TypeVar('T')

class _SupportsWrite(Generic[T]):
    """
    Builtin Typing
    """
