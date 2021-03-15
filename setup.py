from os import name
from setuptools import setup, find_packages

setup(
    name = 'mynotify',
    version = '1.0.0',
    packages = find_packages(exclude=("test",)),
    install_requires=[
        'Click~=7.1',
        'plyer~=2.0',
    ],
    entry_points={
        'console_scripts': [
            'mynotify=mynotify.core:cli'
        ]
    }
)