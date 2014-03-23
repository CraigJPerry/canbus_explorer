#!/usr/bin/env python
# encoding: utf-8


"""Testing helpers and utilities."""


class DevNull(object):
    """A cross platform equiv of writing to /dev/null."""

    def __init__(self):
        self._chunks = []

    def write(self, data):
        self._chunks.append(data)

    @property
    def chunks(self):
        return "".join(self._chunks)

