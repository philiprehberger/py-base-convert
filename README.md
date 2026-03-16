# philiprehberger-base-convert

[![Tests](https://github.com/philiprehberger/py-base-convert/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-base-convert/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-base-convert.svg)](https://pypi.org/project/philiprehberger-base-convert/)
[![License](https://img.shields.io/github/license/philiprehberger/py-base-convert)](LICENSE)

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

## API Reference

| Function / Class | Description |
|---|---|
| `to_base(number, base, *, alphabet="")` | Convert int to string in given base (2-62) |
| `from_base(value, base, *, alphabet="")` | Convert string in given base back to int |
| `BaseCodec(base, *, alphabet="")` | Reusable encoder/decoder for a fixed base |
| `BaseCodec.encode(number)` | Encode int to string |
| `BaseCodec.decode(value)` | Decode string to int |
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

## License

MIT
