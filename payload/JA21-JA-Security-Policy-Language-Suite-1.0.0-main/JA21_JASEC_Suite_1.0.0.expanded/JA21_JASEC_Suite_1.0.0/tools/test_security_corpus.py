"""Check corrected leak invariant and dataset consistency; no policy runtime runs."""
import csv
import gzip
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SecuritySourceRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        master = ROOT / 'corpus/technical/JA21_JASEC_TECHNICAL_CORPUS_10000.jsonl.gz'
        with gzip.open(master, 'rt', encoding='utf-8') as stream:
            cls.records = [json.loads(line) for line in stream if line.strip()]
        cls.by_id = {r['record_id']: r for r in cls.records}

    def test_pass_and_failure_polarity_remain_distinct(self):
        counts = {'pass': 0, 'expected_fail': 0}
        for r in self.records:
            status = r['validation_result']['expected_status']
            flag = re.search(r'assert policy\.secret_leak == (true|false)', r['source']).group(1)
            self.assertEqual(flag, 'false' if status == 'pass' else 'true', r['record_id'])
            counts[status] += 1
        self.assertEqual(counts, {'pass': 7500, 'expected_fail': 2500})

    def test_source_hashes_and_qualifications_match_new_source(self):
        for r in self.records:
            digest = hashlib.sha256(r['source'].encode('utf-8')).hexdigest()
            self.assertEqual(r['ast']['origin_hash'], digest)
            self.assertEqual(r['_suite_publication']['source_sha256'], digest)
            qualification = r['_audit_qualification']
            self.assertEqual(qualification['source_sha256'], digest)
            self.assertTrue(qualification['source_hash_verified'])
            self.assertFalse(qualification['native_execution_eligible'])
            self.assertIsNone(qualification['observed_result'])

    def test_all_shards_match_the_updated_master(self):
        occurrences = 0
        for path in (ROOT / 'corpus/technical/shards').glob('*.jsonl.gz'):
            with gzip.open(path, 'rt', encoding='utf-8') as stream:
                for line in stream:
                    r = json.loads(line)
                    self.assertEqual(r, self.by_id[r['record_id']])
                    occurrences += 1
        self.assertEqual(occurrences, 10000)

    def test_selected_script_sources_and_hashes_match(self):
        with (ROOT / 'catalogs/SCRIPT_CATALOG.csv').open(encoding='utf-8', newline='') as stream:
            catalog = list(csv.DictReader(stream))
        self.assertEqual(len(catalog), 1000)
        for row in catalog:
            source = (ROOT / row['file']).read_text(encoding='utf-8')
            self.assertEqual(source, self.by_id[row['record_id']]['source'])
            self.assertEqual(hashlib.sha256(source.encode('utf-8')).hexdigest(), row['source_sha256'])

    def test_conformance_references_match(self):
        path = ROOT / 'conformance/CONFORMANCE_CASES.jsonl'
        for line in path.read_text(encoding='utf-8').splitlines():
            row = json.loads(line)
            self.assertEqual(row['source_sha256'], self.by_id[row['record_id']]['ast']['origin_hash'])


if __name__ == '__main__':
    unittest.main()
