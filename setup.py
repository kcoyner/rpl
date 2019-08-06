#!/usr/bin/env python3
# Copyright (c) 2016 Kevin Coyner <kcoyner@debian.org>
#
# This file is part of rpl.
# Redistributable under the GNU General Public License
# https://www.gnu.org/licenses/#GPL

from setuptools import setup

DESC = """Replace strings in files."""

long_description = open('README.md').read()

setup(name='rpl',
      version='1.6.0',
      description=DESC,
      long_description=long_description,
      maintainer='Reuben Thomas',
      maintainer_email='rrt@sc3d.org',
      url='https://github.com/rrthomas/rpl',
      license='GPL v3 or later',
      scripts=['rpl'],
      install_requires=['chardet'],
      classifiers=[
          'Environment :: Console',
          'Programming Language :: Python :: 3',
      ],
     )
