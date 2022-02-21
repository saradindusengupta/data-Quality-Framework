#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="data-quality-framework",
    author_email='saradindu.mi1@iiitmk.ac.in',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Check and monitor data distribution and metric changes for tim-series data",
    entry_points={
        'console_scripts': [
            'data_quality_framework=data_quality_framework.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='data_quality_framework',
    name='data_quality_framework',
    packages=find_packages(include=['data_quality_framework', 'data_quality_framework.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/saradindusengupta/data_quality_framework',
    version='0.0.1',
    zip_safe=False,
)
