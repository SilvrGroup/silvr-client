import codecs
import os

from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    """Open a related file and return its content."""
    with codecs.open(os.path.join(here, filename), encoding="utf-8") as f:
        content = f.read()
    return content


README = read_file("README.md")
CHANGELOG = read_file("CHANGELOG.md")

INSTALL_REQUIRES = [
    "httpx",
]

TESTS_REQUIRE = [
    x.replace(" \\", "")
    for x in read_file("./dev-requirements.txt").split("\n")
    if not x.startswith(" ")
]

setup(
    name="silvr-client",
    version="0.1.0",
    description="Silvr client",
    long_description=README + "\n\n" + CHANGELOG,
    license="Apache License (2.0)",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords="web services",
    author="Silvr Group",
    author_email="contact@silvr.co",
    url="https://github.com/SilvrGroup/silvr-client/",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
    test_suite="silvr_client.tests",
    tests_require=TESTS_REQUIRE,
)
