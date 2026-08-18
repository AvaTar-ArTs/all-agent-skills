"""Tests for scripts/common/verify.py"""
import os
import sys
import tempfile
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from common.verify import verify_nonempty


def test_verify_passes_non_empty_file():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b'\x89PNG\r\n\x1a\n' + b'\x00' * 100)
        path = f.name
    try:
        verify_nonempty(path)  # should not raise
    finally:
        os.remove(path)


def test_verify_raises_on_missing_file():
    with pytest.raises(RuntimeError, match="not found"):
        verify_nonempty('/tmp/sap_test_does_not_exist_999.png')


def test_verify_raises_on_empty_file():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        path = f.name
    try:
        with pytest.raises(RuntimeError, match="0 bytes"):
            verify_nonempty(path, min_bytes=1)
    finally:
        os.remove(path)


def test_verify_enforces_min_bytes():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b'small')
        path = f.name
    try:
        with pytest.raises(RuntimeError, match="5 bytes"):
            verify_nonempty(path, min_bytes=1024)
    finally:
        os.remove(path)
