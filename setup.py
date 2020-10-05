#!/usr/bin/env python3

from distutils.core import setup

long_description = open('README.md').read()

setup(name='rpl',
      version='1.7.2',
      description="""Replace strings in files.""",
      long_description=long_description,
      maintainer='Reuben Thomas',
      maintainer_email='rrt@sc3d.org',
      url='https://github.com/rrthomas/rpl',
      license='GPL v3 or later',
      scripts=['rpl'],
      data_files=[('share/man/man1', ['rpl.1'])],
      install_requires=['chardet'],
      classifiers=[
          'Environment :: Console',
          'Programming Language :: Python :: 3',
      ],
     )
