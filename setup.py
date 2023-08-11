from setuptools import setup, find_packages


def print_install_message():
    print("***************************************")
    print("* This package is made by MRayan Asim *")
    print("***************************************")


import atexit

atexit.register(print_install_message)

setup(
    name="100-python-projects",
    version="0.2",
    description="A collection of Python projects",
    author="MRayan Asim",
    author_email="mrayanasim09@gmail.com",
    packages=find_packages(),
)
