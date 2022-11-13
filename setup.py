import os
from build_manpages.build_manpages import get_install_cmd
from setuptools import setup
from distutils.command.build import build

class rpl_build(build):
    def run(self):
        os.environ['COLUMNS'] = '999'
        self.spawn(['help2man', '--locale=C.UTF-8', '--no-info', '--name="replace strings in files"', '--include=man-include.1', '--output=rpl.1', './rpl'])
        super().run()

setup(
    cmdclass={
        'build': rpl_build,
        'install': get_install_cmd(),
    }
)
