from __future__ import annotations

__all__ = [
    "to_base",
    "from_base",
    "BaseCodec",
    "base16",
    "base32",
    "base36",
    "base58",
    "base62",
]

_DEFAULT_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
_BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

_MIN_BASE = 2
_MAX_BASE = 62


def _resolve_alphabet(base: int, alphabet: str) -> str:
    if alphabet:
        if len(alphabet) != base:
            raise ValueError(
                f"Custom alphabet length ({len(alphabet)}) must equal base ({base})"
            )
        if len(set(alphabet)) != len(alphabet):
            raise ValueError("Custom alphabet must not contain duplicate characters")
        return alphabet
    if not (_MIN_BASE <= base <= _MAX_BASE):
        raise ValueError(f"Base must be between {_MIN_BASE} and {_MAX_BASE}, got {base}")
    return _DEFAULT_ALPHABET[:base]


def to_base(number: int, base: int, *, alphabet: str = "") -> str:
    """Convert a non-negative integer to a string in the given base (2-62).

    Args:
        number: Non-negative integer to convert.
        base: Target base (2-62, or any length if custom alphabet is provided).
        alphabet: Optional custom alphabet. Length must equal *base*.

    Returns:
        String representation in the target base.

    Raises:
        ValueError: If *number* is negative or *base* is out of range.
    """
    alpha = _resolve_alphabet(base, alphabet)

    if number < 0:
        raise ValueError(f"Number must be non-negative, got {number}")

    if number == 0:
        return alpha[0]

    digits: list[str] = []
    while number:
        number, remainder = divmod(number, base)
        digits.append(alpha[remainder])

    return "".join(reversed(digits))


def from_base(value: str, base: int, *, alphabet: str = "") -> int:
    """Convert a string in the given base back to an integer.

    Args:
        value: String to decode.
        base: Source base (2-62, or any length if custom alphabet is provided).
        alphabet: Optional custom alphabet. Length must equal *base*.

    Returns:
        Decoded integer.

    Raises:
        ValueError: If *value* contains characters not in the alphabet or *base*
            is out of range.
    """
    alpha = _resolve_alphabet(base, alphabet)
    lookup = {ch: idx for idx, ch in enumerate(alpha)}

    result = 0
    for ch in value:
        if ch not in lookup:
            raise ValueError(
                f"Character {ch!r} is not valid for base {base}"
            )
        result = result * base + lookup[ch]

    return result


class BaseCodec:
    """Reusable encoder/decoder for a specific base and alphabet.

    Args:
        base: Target base (2-62, or any length if custom alphabet is provided).
        alphabet: Optional custom alphabet. Length must equal *base*.
    """

    __slots__ = ("_base", "_alphabet")

    def __init__(self, base: int, *, alphabet: str = "") -> None:
        # Validate eagerly so errors surface at construction time.
        self._alphabet = _resolve_alphabet(base, alphabet)
        self._base = base

    @property
    def base(self) -> int:
        """The numeric base of this codec."""
        return self._base

    @property
    def alphabet(self) -> str:
        """The alphabet used by this codec."""
        return self._alphabet

    def encode(self, number: int) -> str:
        """Encode a non-negative integer to a string."""
        return to_base(number, self._base, alphabet=self._alphabet)

    def decode(self, value: str) -> int:
        """Decode a string back to an integer."""
        return from_base(value, self._base, alphabet=self._alphabet)

    def __repr__(self) -> str:
        return f"BaseCodec(base={self._base})"


# Pre-built codec instances
base16 = BaseCodec(16)
base32 = BaseCodec(32)
base36 = BaseCodec(36)
base58 = BaseCodec(58, alphabet=_BASE58_ALPHABET)
base62 = BaseCodec(62)
