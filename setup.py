from setuptools import setup, find_packages

setup(
    name='Area and Volumes',
    version='0.2',
    packages=find_packages(),
    description='A Python library for solving areas and formulas',
    author='Jacob D',
    author_email='d8008385@gmail.com',
    url='https://github.com/JacobD2013/Areas-and-Volumes',
    install_requires=[
        'mpmath>=1.2.9'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)
