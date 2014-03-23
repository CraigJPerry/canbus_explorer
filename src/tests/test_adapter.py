#!/usr/bin/env python
# encoding: utf-8


import unittest
from pkg_resources import resource_filename
from canbus_explorer.adapter import ReplayAdapter


REPLAY_FIXTURE = resource_filename("canbus_explorer", "canbus-demo.log")


class ReplayAdapterTests(unittest.TestCase):
    """Verify the replay adapter behaves as expected."""

    def setUp(self):
        self.adapter = ReplayAdapter(REPLAY_FIXTURE)

    def test_can_instantiate_replay_adapter(self):
        self.assertIsInstance(self.adapter, ReplayAdapter)


if __name__ == "__main__":
    unittest.main()

