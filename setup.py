import codecs
import os
import re

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))


version = "0.0.1"
pattern = re.compile(r"^#*\s*(?P<version>[0-9]+\.[0-9]+(\.[0-9]+)?)$")

changes = os.path.join(CURRENT_PATH, "CHANGES.rst")
with codecs.open(changes, encoding="utf-8") as changes:
    for line in changes:
        res = pattern.match(line)
        if res:
            version = res.group("version")
            break


setuptools.setup(
    name="pycommands",
    version=version,
    author="Rafael Cassau",
    author_email="rafa.cassau@gmail.com",
    description="Handle a list of commands that should be executed easily and with undo support.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafaelcassau/pycommands",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
