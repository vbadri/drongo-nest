#!/usr/bin/env python

from setuptools import find_packages, setup


setup(
    name='drongo-nest',
    version='1.0.0a1',
    description='High performance server for drongo.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
