import unittest
from pathlib import Path


class SmokeTest(unittest.TestCase):
    def test_generated_file_when_present(self):
        path = Path("e2e-smoke.txt")
        if path.exists():
            self.assertEqual(path.read_text(), "smoke test passed\n")
