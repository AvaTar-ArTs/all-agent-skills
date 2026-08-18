"""Tests for scripts/common/paths.py"""
import os
import sys
import tempfile
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from common.paths import require_abs, ensure_parent, backup_with_timestamp, refuse_overwrite


def test_require_abs_passes_absolute():
    assert require_abs('/tmp/foo') == '/tmp/foo'


def test_require_abs_rejects_relative():
    with pytest.raises(ValueError, match="must be absolute"):
        require_abs('relative/path.png')


def test_ensure_parent_creates_dirs():
    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, 'a', 'b', 'c.png')
        ensure_parent(path)
        assert os.path.isdir(os.path.join(td, 'a', 'b'))


def test_backup_with_timestamp_creates_backup():
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        f.write(b'data')
        original = f.name
    try:
        backup = backup_with_timestamp(original)
        assert backup is not None
        assert 'backup' in backup
        assert not os.path.exists(original)
        assert os.path.exists(backup)
    finally:
        if backup and os.path.exists(backup):
            os.remove(backup)


def test_backup_returns_none_when_absent():
    result = backup_with_timestamp('/tmp/does_not_exist_sap_test_12345.png')
    assert result is None


def test_refuse_overwrite_passes_when_absent(tmp_path):
    out = str(tmp_path / "nonexistent.png")
    refuse_overwrite(out)  # should not raise or exit


def test_refuse_overwrite_passes_when_empty(tmp_path):
    out = tmp_path / "empty.png"
    out.write_bytes(b"")
    refuse_overwrite(str(out))  # zero-byte file is not "non-empty" — should pass


def test_refuse_overwrite_exits_1_when_nonempty(tmp_path, monkeypatch):
    monkeypatch.delenv("PIPELINE_ALLOW_OVERWRITE", raising=False)
    out = tmp_path / "existing.png"
    out.write_bytes(b"X" * 100)
    with pytest.raises(SystemExit) as exc:
        refuse_overwrite(str(out))
    assert exc.value.code == 1


def test_refuse_overwrite_bypassed_by_env(tmp_path, monkeypatch):
    monkeypatch.setenv("PIPELINE_ALLOW_OVERWRITE", "1")
    out = tmp_path / "existing.png"
    out.write_bytes(b"X" * 100)
    refuse_overwrite(str(out))  # should not exit
