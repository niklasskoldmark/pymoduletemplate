# -*- coding: utf-8 -*-

from .context import pymoduletemplate

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(pymoduletemplate.hmm())


if __name__ == "__main__":
    unittest.main()
