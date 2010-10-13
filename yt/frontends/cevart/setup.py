#!/usr/bin/env python
import setuptools
import os, sys, os.path

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('cevart',parent_package,top_path)
    config.add_extension("_cevart_reader",
        ["yt/frontends/cevart/_cevart_reader.cpp"],
        include_dirs=["yt/frontends/cevart/cevart_headers/"])
    config.make_config_py() # installs __config__.py
    config.make_svn_version_py()
    return config
