#!/usr/bin/env python
# encoding: utf-8


"""Application launcher."""

import sys
import argparse
import canbus_explorer


class ArgumentParsingError(Exception):
    pass


class ExceptionRaisingArgumentParser(argparse.ArgumentParser):

    def error(self, message):
        raise ArgumentParsingError(message)


def parse_arguments():
    parser = ExceptionRaisingArgumentParser(
        description=canbus_explorer.__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    return parser.parse_args()


def main():
    args = parse_arguments()


if __name__ == "__main__":
    main()

