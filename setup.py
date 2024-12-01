from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pytest>=8.3.3',
        'pytest-cov>=5.0.0',
    ],
) 