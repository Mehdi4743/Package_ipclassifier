# setup.py

from setuptools import setup, find_packages

setup(
    name="ipclassifier",
    version="0.1.0",
    description="A library to classify IP addresses by their class",
    author="Mehdi",
    author_email="boussalem.e192@ucd.ac.ma",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.6",
)
