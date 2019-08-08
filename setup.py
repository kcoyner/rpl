#!/usr/bin/env python3

from setuptools import setup

long_description = open('README.md').read()

setup(name='rpl',
      version='1.6.1',
      description="""Replace strings in files.""",
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
