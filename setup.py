import sys
import argparse
from setuptools import setup, Extension, find_packages


parser = argparse.ArgumentParser(
    prog='ProgramName',
    description='What the program does',
    epilog='Text at the bottom of help')

parser.add_argument('-n', '--name', type=str)
parser.add_argument('-l', '--link', type=str)

args = parser.parse_args()

name = args.name
url = args.link

setup(
    name=name,
    version="0.0.0",
    author="anonymous",
    description=f"Fake package of {name}.",
    dependency_links=[url],
    packages=find_packages(),
    python_requires=">=3.8"
)
