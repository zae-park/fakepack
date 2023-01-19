import sys
import argparser
from setuptools import setup, Expension

with open("README.md", "r", encoding="utf-8") as me:
    long_description = me.read()

argparser.add_argument('-n', '--name', description = 'Package name.')
argparser.add_argument('-l', '--link', description = 'Package link - git.')

setuptools.setup(
    name="example-pkg-scdev-pd-columns",
    version="0.0.1",
    author="Schooldevops",
    author_email="schooldevops@gmail.com",
    description="schooldevops sample lib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/schooldevops/python-tutorials",
    project_urls={
        "Bug Tracker": "https://github.com/schooldevops/python-tutorials/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
