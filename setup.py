
from setuptools import setup, find_packages

setup(
    name="cdiserrors",
    version='0.2.0',
    description="The auth system for the gdcapi.",
    license="Apache",
    packages=find_packages(),
    install_requires=[
        'cdislogging>=0.1.0',
        'Flask>=0.10.1,<1.0.0',
        'Werkzeug>=0.12.2,<1.0.0',
    ],
)
