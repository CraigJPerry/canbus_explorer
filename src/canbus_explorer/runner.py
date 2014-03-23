#!/usr/bin/env python
# encoding: utf-8


"""Application launcher."""

import sys
import argparse
import canbus_explorer
from canbus_explorer.gui import launch_gui_mainloop
from canbus_explorer.args import ExceptionRaisingArgumentParser


def parse_arguments(argv):
    """Consume known command line arguments."""

    parser = ExceptionRaisingArgumentParser(
        prog="canbus_explorer",
        description=canbus_explorer.__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-v", "--version", action="version",
        version=canbus_explorer.__version__,
        help="Print the Canbus Explorer version and exit."
    )

    parsed_args, remaining_argv = parser.parse_known_args(argv)
    return parsed_args, remaining_argv


def main(argv=None):
    """Application entry point."""
    if argv is None:
        argv = sys.argv

    parsed_args, remaining_argv = parse_arguments(argv)
    return launch_gui_mainloop(remaining_argv)


if __name__ == "__main__":
    sys.exit(main())

