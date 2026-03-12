import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.analysis import populate, analysis
from src.user import User

TESTS_DIR = os.path.dirname(__file__)


def build_output(users: list[User]) -> str:
    lines = [repr(u) for u in users]
    lines.append("\n===== FLAGGED USERS =====\n")
    flagged = [f"{u.id}  :  {u.name}" for u in users if u.malicious_flag]
    if flagged:
        lines.extend(f + "\n" for f in flagged)
    else:
        lines.append("NO FLAGGED USERS\n")
    return "".join(lines)


class TestCases(unittest.TestCase):

    def test_analysis_test1(self):
        result = analysis(populate(os.path.join(TESTS_DIR, "test1.json")), 3)
        actual = build_output(result)

        with open(os.path.join(TESTS_DIR, "test1_result.txt"), "w") as f:
            f.write(actual)

        with open(os.path.join(TESTS_DIR, "test1_expected.txt")) as f:
            expected = f.read()

        self.assertEqual(actual, expected)

    def test_analysis_test2(self):
        result = analysis(populate(os.path.join(TESTS_DIR, "test2.json")), 3)
        actual = build_output(result)

        with open(os.path.join(TESTS_DIR, "test2_result.txt"), "w") as f:
            f.write(actual)

        with open(os.path.join(TESTS_DIR, "test2_expected.txt")) as f:
            expected = f.read()

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
