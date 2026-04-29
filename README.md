# philiprehberger-base-convert

[![Tests](https://github.com/philiprehberger/py-base-convert/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-base-convert/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-base-convert.svg)](https://pypi.org/project/philiprehberger-base-convert/)
[![Last updated](https://img.shields.io/github/last-commit/philiprehberger/py-base-convert)](https://github.com/philiprehberger/py-base-convert/commits/main)

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

### Fixed-width output

Pass `min_length` to left-pad the encoded string with the alphabet's zero character. Useful for fixed-width identifiers:

```python
from philiprehberger_base_convert import to_base, base62

to_base(5, 16, min_length=4)        # "0005"
base62.encode(0, min_length=8)      # "00000000"
base62.encode(123, min_length=6)    # zero-padded base62
```

## API

| Function / Class | Description |
|------------------|-------------|
| `to_base(number, base, *, alphabet="", min_length=0)` | Convert int to string in given base (2-62); `min_length` left-pads with zero char |
| `from_base(value, base, *, alphabet="")` | Convert string in given base back to int |
| `BaseCodec(base, *, alphabet="")` | Reusable encoder/decoder for a fixed base |
| `BaseCodec.encode(number, *, min_length=0)` | Encode int to string with optional left-padding |
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

If you find this project useful:

⭐ [Star the repo](https://github.com/philiprehberger/py-base-convert)

🐛 [Report issues](https://github.com/philiprehberger/py-base-convert/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

💡 [Suggest features](https://github.com/philiprehberger/py-base-convert/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)

❤️ [Sponsor development](https://github.com/sponsors/philiprehberger)

🌐 [All Open Source Projects](https://philiprehberger.com/open-source-packages)

💻 [GitHub Profile](https://github.com/philiprehberger)

🔗 [LinkedIn Profile](https://www.linkedin.com/in/philiprehberger)

## License

[MIT](LICENSE)
