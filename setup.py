import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="criapi",
    version="1.0.2",
    description="An API to get cricket scores,scorecards and commentary in python.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sAksham-Ar/criapi",
    author="Saksham Arya",
    author_email="aryasaksham@gmail.com",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["criapi"],
    include_package_data=True,
    install_requires=["requests","bs4"],
)