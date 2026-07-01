from __future__ import annotations

import argparse
import sys
import unittest
from typing import Iterable, List


MODULES = {
    "startup": "automation.tests.test_startup",
    "home": "automation.tests.test_home",
    "product": "automation.tests.test_product",
    "cart": "automation.tests.test_cart",
    "login": "automation.tests.test_login",
    "customer_service": "automation.tests.test_customer_service",
}


def iter_test_cases(suite: unittest.TestSuite) -> Iterable[unittest.TestCase]:
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from iter_test_cases(item)
        else:
            yield item


def filter_suite_by_case_ids(suite: unittest.TestSuite, case_ids: List[str]) -> unittest.TestSuite:
    selected = unittest.TestSuite()
    normalized = {case_id.upper() for case_id in case_ids}
    for case in iter_test_cases(suite):
        method = getattr(case, case._testMethodName)
        if getattr(method, "case_id", "").upper() in normalized:
            selected.addTest(case)
    return selected


def load_suite(modules: List[str]) -> unittest.TestSuite:
    loader = unittest.defaultTestLoader
    suite = unittest.TestSuite()
    for module_name in modules:
        suite.addTests(loader.loadTestsFromName(MODULES[module_name]))
    return suite


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Android automation test modules.")
    parser.add_argument(
        "--module",
        action="append",
        choices=sorted(MODULES),
        help="Run only specific business modules. Can be repeated.",
    )
    parser.add_argument(
        "--case",
        action="append",
        help="Run only specific case ids such as TC-START-01. Can be repeated.",
    )
    parser.add_argument("--verbosity", type=int, default=2)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    modules = args.module or list(MODULES)
    suite = load_suite(modules)
    if args.case:
        suite = filter_suite_by_case_ids(suite, args.case)
    result = unittest.TextTestRunner(verbosity=args.verbosity).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
