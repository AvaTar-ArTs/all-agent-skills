"""Tests: adapter CLI shape — dry-run, absolute path enforcement, Suno exit-5 (Step 4 acceptance)."""
import json
import os
import subprocess
import sys
import tempfile
import pytest

SKILL = os.path.join(os.path.dirname(__file__), '..')
ADAPTERS = os.path.join(SKILL, 'scripts', 'adapters')
FIXTURES = os.path.join(SKILL, 'tests', 'fixtures')
IMAGE_SPEC = os.path.join(FIXTURES, 'sample-unit-image.yaml')
AUDIO_SPEC = os.path.join(FIXTURES, 'sample-unit-audio.yaml')


def run_adapter(name: str, spec: str, out: str, extra: list = None) -> subprocess.CompletedProcess:
    cmd = [sys.executable, os.path.join(ADAPTERS, f'{name}.py'),
           '--spec', spec, '--out', out] + (extra or [])
    return subprocess.run(cmd, capture_output=True, text=True)


def test_openai_images_dryrun():
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, 'out.png')
        r = run_adapter('openai_images', IMAGE_SPEC, out, ['--dry-run'])
        assert r.returncode == 0
        result = json.loads(r.stdout.strip())
        assert result['ok'] is True
        assert result['dry_run'] is True
        assert result['backend'] == 'openai_images'


def test_replicate_dryrun():
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, 'out.png')
        r = run_adapter('replicate', IMAGE_SPEC, out, ['--dry-run'])
        assert r.returncode == 0
        result = json.loads(r.stdout.strip())
        assert result['ok'] is True


def test_fal_dryrun():
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, 'out.png')
        r = run_adapter('fal', IMAGE_SPEC, out, ['--dry-run'])
        assert r.returncode == 0
        result = json.loads(r.stdout.strip())
        assert result['ok'] is True


def test_comfyui_dryrun():
    with tempfile.TemporaryDirectory() as td:
        wf_path = os.path.join(td, 'workflow.json')
        with open(wf_path, 'w') as f:
            json.dump({"1": {"class_type": "CLIPTextEncode", "inputs": {"text": "", "clip": ["2", 0]}}}, f)
        spec_path = os.path.join(td, 'comfyui-spec.yaml')
        with open(spec_path, 'w') as f:
            f.write(f"backend: comfyui\nunit_id: test-comfyui\nprompt: test prompt\nparams:\n  workflow_path: {wf_path}\n")
        out = os.path.join(td, 'out.png')
        r = run_adapter('comfyui', spec_path, out, ['--dry-run'])
        assert r.returncode == 0
        result = json.loads(r.stdout.strip())
        assert result['ok'] is True


def test_elevenlabs_dryrun_exits_1_bad_voice_id():
    """REPLACE_ME voice_id must cause exit 1 in dry-run."""
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, 'out.mp3')
        r = run_adapter('elevenlabs', AUDIO_SPEC, out, ['--dry-run'])
        assert r.returncode == 1


def test_suno_dryrun():
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, 'out.mp3')
        r = run_adapter('suno_unofficial', AUDIO_SPEC, out, ['--dry-run'])
        assert r.returncode == 0
        result = json.loads(r.stdout.strip())
        assert result['ok'] is True


def test_suno_live_without_base_exits_5():
    env = {k: v for k, v in os.environ.items() if k != 'SUNO_API_BASE'}
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, 'out.mp3')
        cmd = [sys.executable, os.path.join(ADAPTERS, 'suno_unofficial.py'),
               '--spec', AUDIO_SPEC, '--out', out]
        r = subprocess.run(cmd, capture_output=True, text=True, env=env)
        assert r.returncode == 5
        result = json.loads(r.stdout.strip())
        assert result['ok'] is False
        assert result['error_code'] == 5


def test_relative_out_exits_1():
    r = run_adapter('openai_images', IMAGE_SPEC, 'relative/out.png', ['--dry-run'])
    assert r.returncode == 1
    assert 'ERROR' in r.stderr or 'must be absolute' in r.stderr


def test_overwrite_refused_when_out_exists():
    """Live mode must exit 1 (before any API call) if --out already contains data."""
    env = {k: v for k, v in os.environ.items() if k not in ('PIPELINE_ALLOW_OVERWRITE',)}
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, 'existing.png')
        with open(out, 'wb') as f:
            f.write(b'X' * 200)
        cmd = [sys.executable, os.path.join(ADAPTERS, 'openai_images.py'),
               '--spec', IMAGE_SPEC, '--out', out]
        r = subprocess.run(cmd, capture_output=True, text=True, env=env)
        assert r.returncode == 1
        assert 'already exists' in r.stderr


def test_overwrite_allowed_with_env():
    """PIPELINE_ALLOW_OVERWRITE=1 should bypass the guard; adapter proceeds to require_env (exit 2)."""
    env = {k: v for k, v in os.environ.items()}
    env['PIPELINE_ALLOW_OVERWRITE'] = '1'
    env.pop('OPENAI_API_KEY', None)
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, 'existing.png')
        with open(out, 'wb') as f:
            f.write(b'X' * 200)
        cmd = [sys.executable, os.path.join(ADAPTERS, 'openai_images.py'),
               '--spec', IMAGE_SPEC, '--out', out]
        r = subprocess.run(cmd, capture_output=True, text=True, env=env)
        # Guard bypassed → require_env exits 2 (missing key), NOT 1 (overwrite refused)
        assert r.returncode == 2


def test_comfyui_dryrun_exits_1_without_workflow_path():
    """ComfyUI dry-run must exit 1 when workflow_path is absent (W4 fix)."""
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, 'out.png')
        # IMAGE_SPEC has no spec.params.workflow_path — comfyui should refuse
        r = run_adapter('comfyui', IMAGE_SPEC, out, ['--dry-run'])
        assert r.returncode == 1
        assert 'workflow_path' in r.stderr
