import importlib
import subprocess
import sys
import unittest


class ScaffoldTest(unittest.TestCase):
    def test_modules_import(self):
        for name in ("harness.sandbox", "harness.grade", "harness.metrics", "harness.run_eval"):
            importlib.import_module(name)

    def test_clis_show_help(self):
        for script in ("harness/run_eval.py", "scripts/mine_tasks.py", "scripts/validate_tasks.py"):
            r = subprocess.run([sys.executable, script, "--help"], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)


if __name__ == "__main__":
    unittest.main()
