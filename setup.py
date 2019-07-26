import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pythonds9",
    version="0.0.0",
    author="Richard Emile Sarkis",
    author_email="rich@sark.is",
    description="Data Structures package for Problem Solving with Algorithms and Data Structures using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/damnefacts/pythonds9",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ),
)
