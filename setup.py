#!/usr/bin/python3
# 2019-7-16

from setuptools import setup

setup(
    name='AssasiansBot',
    version='1.0.0',
    description='A GroupMe Bot used to moderate and enable all interactions for a game of Assasians.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dgisolfi/AssasiansBot',
    author='dgisolfi',
    license='MIT',
    packages=['AssasiansBot'],
    install_requires=[
        'flask>=0.12.3',
        'requests>=2.20.0',
        'markdown>=2.6.11',
    ],
    zip_safe=False
)