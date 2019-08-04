#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Kevin Coyner <kcoyner@debian.org>
#
# This file is part of rpl.
# Redistributable under the GNU General Public License
# https://www.gnu.org/licenses/#GPL

from setuptools import setup

DESC = """Free replacement for rpl (replace strings in files)."""

long_description =  open('README.md').read()

setup(name='rpl',
      version='1.6.0',
      description=DESC,
      long_description=long_description,
      author=u'Göran Weinholt',
      author_email=u'weinholt@debian.org',
      url='https://github.com/kcoyner/rpl',
      license='GPL v3 or later',
      scripts=['rpl'],
      install_requires=['chardet']
      classifiers=[
          'Environment :: Console',
          'Programming Language :: Python :: 3',
      ],
     )
