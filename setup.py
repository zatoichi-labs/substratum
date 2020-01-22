#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    find_packages,
    setup,
)

extras = {
    'test': [
    ],
    'docs': [
    ],
    'dev': [
        "bumpversion",
        "ipython",
        "twine",
    ]
}

extras['dev'] = (
    extras['test'] + 
    extras['docs'] +
    extras['dev']
)

setup(
    name='substratum',
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version='0.1.0-alpha.3',
    description="""Substratum""",
    long_description_markdown_filename='README.md',
    author='Zatoichi Labs',
    author_email='admin@zatoichi-labs.com',
    url='https://github.com/zatoichi-labs/substratum',
    install_requires=[
        "base58",
        "eth-utils>=1.8,<2.0",
        "scalecodec@https://github.com/polkascan/py-scale-codec/tarball/master#egg=scalecodec",
        "subkey",
    ],
    setup_requires=['setuptools-markdown'],
    python_requires='>=3.8,<4',
    extras_require=extras,
    py_modules=['substratum'],
    license='MIT',
    zip_safe=False,
    keywords='substrate',
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
