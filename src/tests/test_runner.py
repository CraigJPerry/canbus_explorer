#!/usr/bin/env python
# encoding: utf-8


import unittest
from canbus_explorer import runner


class LaunchApplication(unittest.TestCase):
    """Ensure the app can be started."""

    def test_can_invoke_application(self):
        self.assertRaises(SystemExit, runner.main)


if __name__ == "__main__":
    unittest.main()

