from setuptools import setup
from setuptools.command.install import install
import os

class Installer(install):
    def run(self):
        print(os.popen('cp transfer /usr/bin/').read())

setup(
        name='transfer',
        url='https://github.com/alkass/transfer',
        author='Fadi Hanna Al-Kass',
        description='transfer.sh CLI Utility',
        long_description=open('README.md').read(),
        cmdclass={'install': Installer},
        install_requires=['requests'],
)
