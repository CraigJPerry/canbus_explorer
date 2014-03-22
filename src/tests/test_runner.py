#!/usr/bin/env python
# encoding: utf-8


import sys
import unittest
from tests.helpers import DevNull
from canbus_explorer import runner, __version__


class LaunchApplication(unittest.TestCase):
    """Ensure the app can be started."""

    def setUp(self):
        self._stderr = sys.stderr
        sys.stderr = DevNull()

    def tearDown(self):
        sys.stderr = self._stderr

    def test_can_invoke_application(self):
        runner.main(["canbus_explorer"])
        self.assertEqual("", "".join(sys.stderr.chunks))

    def test_can_view_version_number_via_the_appropriate_cmdline_argument(self):
        self.assertRaises(SystemExit, runner.main, ["canbus_explorer", "-v"])
        self.assertIn(__version__, "".join(sys.stderr.chunks))


if __name__ == "__main__":
    unittest.main()

