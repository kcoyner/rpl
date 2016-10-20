#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup

DESC = """Free replacement for rpl (replace strings in files)."""

setup(name='rpl',
      version='1.5.6',
      description=DESC,
      author=u'Göran Weinholt',
      author_email=u'weinholt@debian.org',
      url='https://github.com/kcoyner/rpl',
      license='GPL v2 or later',
      scripts=['rpl'],
      classifiers=[
          'Environment :: Console',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
     )
