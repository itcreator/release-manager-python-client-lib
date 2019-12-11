# coding: utf-8

"""
    Release Manager

    This application generate version for your software.  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Contact: vitalleshchyk@gmail.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "release-manager-client"
VERSION = "0.2.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Release Manager",
    author="Vital Leshchyk",
    author_email="vitalleshchyk@gmail.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Release Manager"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="3-Clause BSD",
    long_description="""\
    This application generate version for your software.  # noqa: E501
    """
)
