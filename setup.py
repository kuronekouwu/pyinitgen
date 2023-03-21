"""Install packages as defined in this file into the Python environment."""
from setuptools import setup

setup(
    name="pyinitgen",
    author="M-307",
    author_email="me@m307.dev",
    description="A python __init__ generator",
    version='0.0.1',
    install_requires=[
        "setuptools>=45.0",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.0",
        "Topic :: Utilities",
    ],
)