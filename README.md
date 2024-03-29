# philiprehberger-base-convert

[![Tests](https://github.com/philiprehberger/py-base-convert/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-base-convert/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-base-convert.svg)](https://pypi.org/project/philiprehberger-base-convert/)
[![GitHub release](https://img.shields.io/github/v/release/philiprehberger/py-base-convert)](https://github.com/philiprehberger/py-base-convert/releases)
[![Last updated](https://img.shields.io/github/last-commit/philiprehberger/py-base-convert)](https://github.com/philiprehberger/py-base-convert/commits/main)
[![License](https://img.shields.io/github/license/philiprehberger/py-base-convert)](LICENSE)
[![Bug Reports](https://img.shields.io/github/issues/philiprehberger/py-base-convert/bug)](https://github.com/philiprehberger/py-base-convert/issues?q=is%3Aissue+is%3Aopen+label%3Abug)
[![Feature Requests](https://img.shields.io/github/issues/philiprehberger/py-base-convert/enhancement)](https://github.com/philiprehberger/py-base-convert/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)
[![Sponsor](https://img.shields.io/badge/sponsor-GitHub%20Sponsors-ec6cb9)](https://github.com/sponsors/philiprehberger)

Convert numbers between any base (2-62) with human-friendly APIs.

## Installation

```bash
pip install philiprehberger-base-convert
```

## Usage

### Basic Conversion

```python
from philiprehberger_base_convert import to_base, from_base

# Convert to base 16 (hex)
to_base(255, 16)      # "ff"
from_base("ff", 16)   # 255

# Convert to base 62
to_base(999999, 62)   # "4c91"
from_base("4c91", 62) # 999999
```

### Pre-built Codecs

```python
from philiprehberger_base_convert import base16, base36, base58, base62

base62.encode(123456789)       # "8M0kX"
base62.decode("8M0kX")         # 123456789

base58.encode(123456789)       # Bitcoin-style base58
base36.encode(123456789)       # "21i3v9"
base16.encode(255)             # "ff"
```

### Bytes Encoding

Encode arbitrary bytes (UUIDs, hashes, binary data) to compact base-N strings:

```python
from philiprehberger_base_convert import base62

# Encode bytes to base62
data = b"\x00\x01\x02\xff"
encoded = base62.encode_bytes(data)

# Decode back to bytes
decoded = base62.decode_bytes(encoded)
assert decoded == data

# Encode a UUID to a compact string
import uuid
uid = uuid.uuid4().bytes
short_id = base62.encode_bytes(uid)
```

### Custom Alphabet

```python
from philiprehberger_base_convert import to_base, from_base, BaseCodec

# Use a custom alphabet for base 3
to_base(42, 3, alphabet="XYZ")   # "YXZX"
from_base("YXZX", 3, alphabet="XYZ")  # 42

# Reusable codec with custom alphabet
codec = BaseCodec(4, alphabet="ACGT")
codec.encode(42)   # "GCAC"
codec.decode("GCAC")  # 42
```

## API

| Function / Class | Description |
|------------------|-------------|
| `to_base(number, base, *, alphabet="")` | Convert int to string in given base (2-62) |
| `from_base(value, base, *, alphabet="")` | Convert string in given base back to int |
| `BaseCodec(base, *, alphabet="")` | Reusable encoder/decoder for a fixed base |
| `BaseCodec.encode(number)` | Encode int to string |
| `BaseCodec.decode(value)` | Decode string to int |
| `BaseCodec.encode_bytes(data)` | Encode bytes to a base-N string (preserves leading zero bytes) |
| `BaseCodec.decode_bytes(value)` | Decode a base-N string back to bytes |
| `base16` | Pre-built codec for base 16 |
| `base32` | Pre-built codec for base 32 |
| `base36` | Pre-built codec for base 36 |
| `base58` | Pre-built codec for base 58 (Bitcoin alphabet) |
| `base62` | Pre-built codec for base 62 |

## Development

```bash
pip install -e .
python -m pytest tests/ -v
```

## Support

If you find this package useful, consider giving it a star on GitHub — it helps motivate continued maintenance and development.

[![LinkedIn](https://img.shields.io/badge/Philip%20Rehberger-LinkedIn-0A66C2?logo=linkedin)](https://www.linkedin.com/in/philiprehberger)
[![More packages](https://img.shields.io/badge/more-open%20source%20packages-blue)](https://philiprehberger.com/open-source-packages)

## License

[MIT](LICENSE)
