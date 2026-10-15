import copy
import json
import unittest

from jsonschema import ValidationError
from tools.catalog import ROOT, generated_files, matches, validate_case


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.case = json.loads((ROOT / "cases/ENV-0001.json").read_text(encoding="utf-8"))

    def test_customer_report_alone_cannot_confirm_root_cause(self):
        self.case["cause"]["evidence_ids"] = ["E1"]
        with self.assertRaisesRegex(ValueError, "confirmed requires"):
            validate_case(self.case)

    def test_unrelated_confirmed_evidence_cannot_confirm_root_cause(self):
        self.case["cause"]["evidence_ids"] = ["E5"]
        with self.assertRaisesRegex(ValueError, "confirmed requires"):
            validate_case(self.case)

    def test_dangling_evidence_is_rejected(self):
        self.case["remediations"][0]["evidence_ids"].append("E99")
        with self.assertRaisesRegex(ValueError, "unknown evidence"):
            validate_case(self.case)

    def test_duplicate_evidence_is_rejected(self):
        self.case["evidence"].append(copy.deepcopy(self.case["evidence"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate evidence"):
            validate_case(self.case)

    def test_sensitive_source_urls_are_rejected(self):
        for url in ["https://example.com/report?token=synthetic", "https://user:pass@example.com/report"]:
            with self.subTest(url=url):
                self.case["evidence"][2]["reference"] = url
                with self.assertRaisesRegex(ValueError, "without credentials"):
                    validate_case(self.case)

    def test_fixture_path_cannot_escape_repo(self):
        self.case["reproducer"]["path"] = "../../private.test.mjs"
        with self.assertRaises(ValidationError):
            validate_case(self.case)

    def test_evidence_date_must_be_real(self):
        self.case["evidence"][0]["observed_at"] = "2026-02-31"
        with self.assertRaises(ValidationError):
            validate_case(self.case)

    def test_search_respects_status_platform_and_case(self):
        self.assertTrue(matches(self.case, "TOSORTED", "windows", True))
        self.assertFalse(matches(self.case, "toSorted", "macos"))
        self.case["status"] = "reported"
        self.assertFalse(matches(self.case, "toSorted", confirmed=True))

    def test_generated_document_keeps_verification_limits(self):
        output = generated_files([self.case])
        document = output[next(path for path in output if path.as_posix() == "docs/cases/ENV-0001.md")]
        self.assertIn(self.case["limitations"][0], document)
        self.assertIn(self.case["evidence"][0]["scope"], document)


if __name__ == "__main__":
    unittest.main()
