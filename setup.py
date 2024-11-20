from setuptools import find_packages, setup

setup(
    name='mlbdatatools',
    packages=find_packages(include=['mlbdatatools']),
    version='0.1.1',
    description='DataFrames, type-safety, and plotting for modern baseball analytics.',
    author='Joey Sinclair',
    install_requires=['pandas', 'numpy', 'matplotlib', 'requests'],
)