#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup

try:
    def u8(s):
        return s.decode('unicode-escape')
except NameError:
    def u8(s):
        return s

DESC = """Free replacement for rpl (replace strings in files)."""

setup(name='rpl',
      version='1.5.6',
      description=DESC,
      author=u8('Göran Weinholt'),
      author_email=u8('weinholt@debian.org'),
      url='https://github.com/kcoyner/rpl',
      license='GPL v2 or later',
      scripts=['rpl'],
      classifiers=[
          'Environment :: Console',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
     )
