#!/usr/bin/env python
"""
Stable Flow - Agentic Coding Documentation

A comprehensive documentation generation system designed for AI-assisted development.
"""

import os
import re
from setuptools import setup, find_packages

# Read version from a version file or extract from __init__.py
def get_version():
    """Extract version from version file or return default."""
    version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
    if os.path.exists(version_file):
        with open(version_file, 'r') as f:
            return f.read().strip()

    # Default version
    return '1.0.0'

def get_long_description():
    """Read README for long description."""
    readme_file = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_file):
        with open(readme_file, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

def get_requirements():
    """Read requirements from requirements.txt."""
    requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_file):
        with open(requirements_file, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

# Package metadata
VERSION = get_version()
LONG_DESCRIPTION = get_long_description()
REQUIREMENTS = get_requirements()

setup(
    name='stable-flow',
    version=VERSION,
    description='AI-Powered Documentation Generation for Software Projects',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Stable Flow Development Team',
    author_email='team@stableflow.dev',
    url='https://github.com/your-org/stable-flow',
    project_urls={
        'Documentation': 'https://github.com/your-org/stable-flow/docs/',
        'Source': 'https://github.com/your-org/stable-flow',
        'Tracker': 'https://github.com/your-org/stable-flow/issues',
    },
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Utilities',
    ],
    keywords='documentation, ai, templates, software-development, project-management',
    packages=find_packages(exclude=['tests', 'tests.*', 'examples', 'examples.*']),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=22.0.0',
            'flake8>=6.0.0',
            'mypy>=1.0.0',
            'pre-commit>=3.0.0',
            'memory-profiler>=0.61.0',
        ],
        'docs': [
            'sphinx>=5.0.0',
            'sphinx-rtd-theme>=1.2.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'stable-flow=scripts.stable_flow:main',
        ],
    },
    python_requires='>=3.8',
    zip_safe=False,
    test_suite='tests',
    tests_require=[
        'pytest>=7.0.0',
        'pytest-cov>=4.0.0',
    ],
)</content>
</xai:function_call name="write">
<parameter name="file_path">pyproject.toml

