#!/usr/bin/env python
# encoding: utf-8


"""Application launcher."""

import sys
import argparse
import canbus_explorer
from canbus_explorer.args import ExceptionRaisingArgumentParser


def parse_arguments(argv):
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

    return parser.parse_args(argv[1:])


def main(argv=None):
    if argv is None:
        argv = sys.argv
    args = parse_arguments(argv)


if __name__ == "__main__":
    main()

