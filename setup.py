from setuptools import find_packages
from setuptools import setup

setup(
    name="__XXXXX__Package",
    version="0.0.1",
    maintainer="niv",
    description=f"Local folders of __XXXXX__ as Python module",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)