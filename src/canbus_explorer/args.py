#!/usr/bin/env python
# encoding: utf-8


"""Argument parsing utilities & customisations."""

import sys
import argparse


class ArgumentParsingError(Exception):
    """Raised in place of SystemExit in the original ArgumentParser."""
    pass


class ExceptionRaisingArgumentParser(argparse.ArgumentParser):
    """An ArgumentParser which raises a checked exception instead of
    terminating the Python process on major errors. Provides for more
    graceful application termination."""

    def error(self, message):
        """Prints a usage message incorporating the message to stderr
        then raises ArgumentParsingError(message)."""
        self.print_usage(sys.stderr)
        raise ArgumentParsingError(message)

