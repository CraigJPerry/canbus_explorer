#!/usr/bin/env python
# encoding: utf-8


"""Canbus Explorer is a cross-platform GUI to assist in reverse
engineering and debugging Canbus messages. I created this app to
assist in reverse engineering the appropriate canbus messages to
broadcast on my cars canbus for automating various functions"""


import pkg_resources

__version__ = pkg_resources.require("canbus_explorer")[0].version

