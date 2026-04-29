"""Tests for philiprehberger_base_convert."""

from __future__ import annotations

import pytest

from philiprehberger_base_convert import (
    BaseCodec,
    base16,
    base32,
    base36,
    base58,
    base62,
    from_base,
    to_base,
)


def test_to_base_hex() -> None:
    assert to_base(255, 16) == "ff"


def test_from_base_hex() -> None:
    assert from_base("ff", 16) == 255


def test_round_trip_base62() -> None:
    for n in (0, 1, 99, 1234, 9999999):
        assert from_base(to_base(n, 62), 62) == n


def test_to_base_zero() -> None:
    assert to_base(0, 16) == "0"


def test_to_base_negative_raises() -> None:
    with pytest.raises(ValueError):
        to_base(-1, 16)


def test_invalid_base_raises() -> None:
    with pytest.raises(ValueError):
        to_base(10, 1)
    with pytest.raises(ValueError):
        to_base(10, 63)


def test_from_base_invalid_char_raises() -> None:
    with pytest.raises(ValueError):
        from_base("xyz!", 16)


def test_custom_alphabet_round_trip() -> None:
    alpha = "ACGT"
    for n in (0, 1, 5, 42):
        encoded = to_base(n, 4, alphabet=alpha)
        assert from_base(encoded, 4, alphabet=alpha) == n


def test_custom_alphabet_wrong_length_raises() -> None:
    with pytest.raises(ValueError):
        to_base(10, 4, alphabet="ABC")


def test_custom_alphabet_duplicate_chars_raises() -> None:
    with pytest.raises(ValueError):
        to_base(10, 4, alphabet="AABB")


def test_codec_encode_decode() -> None:
    assert base62.decode(base62.encode(123456789)) == 123456789


def test_base16_codec() -> None:
    assert base16.encode(255) == "ff"
    assert base16.decode("ff") == 255


def test_base32_codec() -> None:
    assert base32.decode(base32.encode(9999)) == 9999


def test_base36_codec() -> None:
    assert base36.decode(base36.encode(123456789)) == 123456789


def test_base58_uses_bitcoin_alphabet() -> None:
    # base58 alphabet excludes 0, O, I, l
    encoded = base58.encode(0)
    assert "0" not in encoded
    assert "O" not in encoded


def test_codec_repr() -> None:
    assert "62" in repr(base62)


def test_codec_alphabet_property() -> None:
    assert len(base62.alphabet) == 62
    assert base62.base == 62


def test_encode_bytes_round_trip() -> None:
    data = b"\x00\x01\x02\xff\xab"
    assert base62.decode_bytes(base62.encode_bytes(data)) == data


def test_encode_bytes_preserves_leading_zeros() -> None:
    data = b"\x00\x00\xff"
    assert base62.decode_bytes(base62.encode_bytes(data)) == data


def test_encode_bytes_empty() -> None:
    assert base62.decode_bytes(base62.encode_bytes(b"\x00")) == b"\x00"


# ---------------------------------------------------------------------------
# min_length padding
# ---------------------------------------------------------------------------


def test_to_base_min_length_pads_with_zero_char() -> None:
    assert to_base(5, 16, min_length=4) == "0005"


def test_to_base_min_length_does_not_truncate() -> None:
    # If output is already longer than min_length, leave it.
    assert to_base(255, 16, min_length=2) == "ff"


def test_to_base_min_length_zero_default() -> None:
    assert to_base(255, 16) == "ff"


def test_to_base_min_length_for_zero() -> None:
    assert to_base(0, 16, min_length=4) == "0000"


def test_codec_encode_min_length() -> None:
    assert base62.encode(0, min_length=8) == "00000000"
    assert base62.encode(123, min_length=4).startswith("0")


def test_to_base_min_length_with_custom_alphabet_uses_first_char() -> None:
    # Custom alphabet uses its first char for padding.
    out = to_base(1, 4, alphabet="ACGT", min_length=5)
    assert out.startswith("AAAA")


def test_min_length_round_trip_decodes_correctly() -> None:
    encoded = base62.encode(42, min_length=10)
    assert base62.decode(encoded) == 42
