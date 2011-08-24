import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "DynIP",
    version = "0.1d",
    author = "Kris Hardy",
    author_email = "kris@rkrishardy.com",
    description = ("A painfully simple UDP Client/Server for tracking the IP addresses of your devices."),
    license = "BSD",
    keywords = "udp ip tracking",
    url = "http://www.rkrishardy.com",
    packages=['dynip'],
    long_description=read('README'),
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Internet",
        "Environment :: No Input/Output (Daemon)",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
    ],
    data_files=[
        ('.', ['example.conf', 'test.conf'])
    ]
)
