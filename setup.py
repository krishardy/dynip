import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "DynIP",
    version = "0.1e",
    author = "Kris Hardy",
    author_email = "kris@rkrishardy.com",
    description = ("A painfully simple UDP Client/Server for tracking the IP addresses of your devices."),
    license = "BSD",
    keywords = "udp ip tracking",
    url = "http://readthedocs.org/docs/dynip/en/latest",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.rst'),

    classifiers=[
        "Topic :: Utilities",
        "Topic :: Internet",
        "Environment :: No Input/Output (Daemon)",
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ],

    package_data = {
        'dynip.init': ['example.conf'],
    },

    install_requires=[
        'argparse'
    ],

    entry_points = """
        [console_scripts]
        dynip-init = dynip.init.console:main
        dynipd = dynip.server:main
        dynipc = dynip.client:main
    """
)
