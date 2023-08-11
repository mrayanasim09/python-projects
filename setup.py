from setuptools import setup, find_packages


def print_install_message():
    print("***************************************")
    print("* This package is made by MRayan Asim *")
    print("***************************************")


import atexit

atexit.register(print_install_message)

setup(
    name="top_python_projects",
    version="0.5",
    description="A collection of Python projects",
    author="MRayan Asim",
    author_email="mrayanasim09@gmail.com",
    packages=find_packages(),
)
