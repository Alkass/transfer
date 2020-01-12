from setuptools import setup
from setuptools.command.install import install
import sys, os, stat
from shutil import copyfile

__PROG_NAME__ = 'transfer'

setup(
        name=__PROG_NAME__,
        version='1.0.0',
        license=open('LICENSE').read(),
        url='https://github.com/alkass/%s' % __PROG_NAME__,
        author='Fadi Hanna Al-Kass',
        author_email='f_alkass@zgps.live',
        description='transfer.sh CLI utility',
        long_description=open('README.md').read(),
        keywords='file sharing upload service',
        packages=[__PROG_NAME__],
        install_requires=open('requirements.txt').read().split('\n'),
        entry_points={
            'console_scripts': ['{prog} = {prog}:main'.format(prog=__PROG_NAME__)],
        }
)
