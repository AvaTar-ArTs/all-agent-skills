from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
CREATE = SKILL_ROOT / "scripts/create_basic_plugin.py"
VALIDATE = SKILL_ROOT / "scripts/validate_plugin.py"
CACHEBUSTER = SKILL_ROOT / "scripts/update_plugin_cachebuster.py"


def run(*args: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", *(str(arg) for arg in args)],
        capture_output=True,
        text=True,
        check=False,
    )


class PluginCreatorTests(unittest.TestCase):
    def test_basic_scaffold_omits_unused_skills_contract(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            created = run(CREATE, "basic-sample", "--path", root)
            self.assertEqual(created.returncode, 0, created.stderr)
            plugin = root / "basic-sample"
            manifest = json.loads((plugin / ".codex-plugin/plugin.json").read_text())
            self.assertNotIn("skills", manifest)
            self.assertFalse((plugin / "skills").exists())
            self.assertEqual(run(VALIDATE, plugin).returncode, 0)

    def test_full_optional_scaffold_validates(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            plugin = root / "full-sample"
            created = run(
                CREATE,
                "full-sample",
                "--path",
                root,
                "--with-skills",
                "--with-hooks",
                "--with-scripts",
                "--with-assets",
                "--with-mcp",
                "--with-apps",
            )
            self.assertEqual(created.returncode, 0, created.stderr)
            manifest = json.loads((plugin / ".codex-plugin/plugin.json").read_text())
            self.assertEqual(manifest["skills"], "./skills/")
            self.assertEqual(run(VALIDATE, plugin).returncode, 0)

    def test_folder_manifest_name_mismatch_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            self.assertEqual(run(CREATE, "manifest-name", "--path", root).returncode, 0)
            renamed = root / "different-folder-name"
            (root / "manifest-name").rename(renamed)
            validated = run(VALIDATE, renamed)
            self.assertNotEqual(validated.returncode, 0)
            self.assertIn("must match the outer plugin folder name", validated.stdout)

    def test_duplicate_marketplace_preflight_leaves_no_second_plugin(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            marketplace = root / "marketplace.json"
            first = run(
                CREATE,
                "duplicate-sample",
                "--path",
                root / "first/plugins",
                "--marketplace-path",
                marketplace,
                "--with-marketplace",
            )
            self.assertEqual(first.returncode, 0, first.stderr)
            second_plugin = root / "second/plugins/duplicate-sample"
            second = run(
                CREATE,
                "duplicate-sample",
                "--path",
                root / "second/plugins",
                "--marketplace-path",
                marketplace,
                "--with-marketplace",
            )
            self.assertNotEqual(second.returncode, 0)
            self.assertFalse(second_plugin.exists())

    def test_nameless_existing_marketplace_is_rejected_before_scaffold(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            marketplace = root / "marketplace.json"
            marketplace.write_text('{"plugins": []}\n', encoding="utf-8")
            plugin = root / "plugins/nameless-marketplace"
            created = run(
                CREATE,
                "nameless-marketplace",
                "--path",
                root / "plugins",
                "--marketplace-path",
                marketplace,
                "--with-marketplace",
            )
            self.assertNotEqual(created.returncode, 0)
            self.assertFalse(plugin.exists())

    def test_invalid_semver_cachebuster_is_rejected_without_rewrite(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            plugin = root / "cachebuster-sample"
            self.assertEqual(run(CREATE, "cachebuster-sample", "--path", root).returncode, 0)
            manifest_path = plugin / ".codex-plugin/plugin.json"
            manifest = json.loads(manifest_path.read_text())
            manifest["version"] = "dev-build+other-tag"
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
            before = manifest_path.read_bytes()
            updated = run(CACHEBUSTER, plugin, "--cachebuster", "audit")
            self.assertNotEqual(updated.returncode, 0)
            self.assertEqual(manifest_path.read_bytes(), before)

    def test_empty_marketplace_category_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            created = run(CREATE, "empty-category", "--path", root, "--category", "   ")
            self.assertNotEqual(created.returncode, 0)
            self.assertFalse((root / "empty-category").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
