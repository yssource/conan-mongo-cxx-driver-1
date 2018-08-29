#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(archs=["x86_64"], args="--build missing")
    builder.add_common_builds()
    builder.add({}, {"use_17_standard" : False}, {}, {})
    builder.run()
