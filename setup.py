# -*- coding: utf-8 -*-
from setuptools import setup
setup(
    name='sync',
    version='1.0.0',
    description='mirror sync',
    url='https://github.com/Tara-X/mirror-sync',
    author='SRK.Lyu',
    author_email='superalsrk@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='mirror sync',
    packages=[
        'sync',
        'sync.utils'
    ],

    install_requires=['requests>=2.5.0', 'pytest>=2.9.2', 'unittest2>=1.1.0'],
    test_suite='sync_tests'
)
