#!/usr/bin/env python
# encoding: utf-8


"""Testing helpers and utilities."""


class DevNull(object):
    """A cross platform equiv of writing to /dev/null."""

    def write(self, data):
        pass

