# setup.py

from setuptools import setup, find_packages

setup(
    name="mr_analytics",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'my_module=mymodule.mymodule:hello',
        ],
    },
)
