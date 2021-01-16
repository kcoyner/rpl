from build_manpages.build_manpages import get_install_cmd
from setuptools import setup
from setuptools.command.install import install

setup(
    cmdclass={
        'install': get_install_cmd(install),
    }
)
