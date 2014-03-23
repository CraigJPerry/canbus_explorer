#!/usr/bin/env python
# encoding: utf-8


import unittest
from canbus_explorer import __version__


class SemanticVersioningCompliance(unittest.TestCase):

    def test_version_number_complies_with_semver_inc_optional_pre_release_metadata(self):
        """I use a subset of `Semantic Versioning <http://semver.org>_`.

        Specifically i exclude build metadata (the trailing
        +build-host_date_whatever), since in python it's not as useful.

        The following will match, in ascending order:

            1.2.3
            1.2.4-alpha.1
            1.2.4-alpha.2
            1.2.4-final.1
            1.2.4
        """
        self.assertRegexpMatches(__version__, "^\d\.\d\.\d(-(alpha|beta|candidate|final)\.\d)?$")


if __name__ == "__main__":
    unittest.main()

