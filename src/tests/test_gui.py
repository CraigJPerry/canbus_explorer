#!/usr/bin/env python
# encoding: utf-8


import sys
import unittest
from canbus_explorer.gui import launch_gui_mainloop


@unittest.skip("Not ready yet, will hang test runs")
class GUILoadAndInitialisation(unittest.TestCase):
    """Ensure the GUI can be brought up."""

    def test_can_load_ui(self):
        launch_gui_mainloop(sys.argv)


if __name__ == "__main__":
    unittest.main()

