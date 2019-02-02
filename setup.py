from setuptools import setup

setup(
    name='XNATUM',
    url='https://github.com/rgllm/xnatum',
    author='Rogério Moreira',
    author_email='r@rgllm.com',
    packages=['core'],
    install_requires=['numpy'],
    version='0.1',
    license='MIT',
    description='A package for connecting and manage data on XNAT.',
)
