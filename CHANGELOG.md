# Changelog

## 0.2.0 (2026-03-27)

- Add `BaseCodec.encode_bytes()` and `BaseCodec.decode_bytes()` for binary data encoding
- Add issue templates, PR template, and Dependabot config
- Add full badge set and Support section to README

## 0.1.8

- Trim keywords to match pyproject template guide

## 0.1.7- Add pytest and mypy tool configuration to pyproject.toml

## 0.1.6

- Add basic import test

## 0.1.5

- Add Development section to README
- Add wheel build target to pyproject.toml

## 0.1.2

- Fix publish workflow (remove nonexistent test step)

## 0.1.1

- Re-release for PyPI publishing

## 0.1.0 (2026-03-15)

- Initial release
- `to_base()` and `from_base()` for arbitrary base conversion (2-62)
- `BaseCodec` class for reusable encode/decode
- Pre-built codecs: `base16`, `base32`, `base36`, `base58`, `base62`
- Custom alphabet support
