from setuptools import setup
from setuptools import find_packages

setup(
    name='xnatum',
    url='https://github.com/rgllm/xnatum',
    author='Rogério Moreira',
    author_email='r@rgllm.com',
    packages=find_packages(),
    install_requires=['xnat'],
    version='0.2',
    license='MIT',
    description='A package for connecting and manage data on XNAT.',
)
