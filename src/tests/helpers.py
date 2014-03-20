#!/usr/bin/env python
# encoding: utf-8


"""Testing helpers and utilities."""


class DevNull(object):
    """A cross platform equiv of writing to /dev/null."""

    def __init__(self):
        self.chunks = []

    def write(self, data):
        self.chunks.append(data)

