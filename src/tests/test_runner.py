#!/usr/bin/env python
# encoding: utf-8


import sys
import unittest
from tests.helpers import DevNull
from canbus_explorer import runner
from canbus_explorer.args import ArgumentParsingError


class LaunchApplication(unittest.TestCase):
    """Ensure the app can be started."""

    def setUp(self):
        self._stderr = sys.stderr
        sys.stderr = DevNull()

    def tearDown(self):
        sys.stderr = self._stderr

    def test_can_invoke_application(self):
        self.assertRaises(ArgumentParsingError, runner.main)


if __name__ == "__main__":
    unittest.main()

