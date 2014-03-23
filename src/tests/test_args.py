#!/usr/bin/env python
# encoding: utf-8


import sys
import unittest
import argparse
from tests.helpers import DevNull
from canbus_explorer.args import ExceptionRaisingArgumentParser, ArgumentParsingError


class ValidateExceptionRaising(unittest.TestCase):
    """Verify that the ArgumentParser raises a checked exception
    instead of default behaviour of an unchecked exception (which
    terminates the runtime)."""

    def setUp(self):
        self._stderr = sys.stderr
        sys.stderr = DevNull()
        self.argparser = ExceptionRaisingArgumentParser()

    def tearDown(self):
        sys.stderr = self._stderr

    def test_can_create_arg_parser(self):
        self.assertIsInstance(self.argparser, argparse.ArgumentParser)

    def test_raises_checked_exceptions(self):
        self.argparser.add_argument("-r", "--required", required=True)
        self.assertRaises(ArgumentParsingError, self.argparser.parse_args)


if __name__ == "__main__":
    unittest.main()

