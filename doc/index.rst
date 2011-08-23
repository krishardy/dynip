.. DynIP documentation master file, created by
   sphinx-quickstart on Mon Aug 22 22:57:01 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to DynIP's documentation!
=================================

Contents:

.. toctree::
   :maxdepth: 2


About DynIP
===========

For an overview of DynIP, please read the README file.  I will eventaully move the info to this file, but I obviously haven't done it yet.


Installation
============

You can download DynIP from PyPi:

http://pypi.python.org/pypi/DynIP

To install, execute the following: ::

    $ easy_install DynIP


Usage
=====

To configure the server, edit dynip/server.py and modify the UDP_IP, UDP_PORT and CLIENT_LOG_PATH.  Descriptions of each are in the code.

Then start the server by typing: ::

    $ python dynip/server.py

To launch the client and have it fire off a UDP packet, edit dynip/client.py and modify the SERVER_HOSTNAME and SERVER_PORT lines.  Descriptions of each are in the code.

Then launch the client by typing: ::

    $ python dynip/client.py

The server will then save the hostname, ip address and date/time in the CLIENT_LOG_PATH file (dynip.json in the default configuration).


Options
-------

To enable verbose (INFO-level) logging, add `-v` to the command line when launching the server or client. ::

    $ python dynip/server.py -v
    $ python dynip/client.py -v


To enable debug (DEBUG-level) logging, add `--debug` to the command line when launching the server or client. ::

    $ python dynip/server.py --debug
    $ python dynip/client.py --debug


Both the server and client return usage information if you add `--help` or `-h` to the command line when invoking the client or server.



Get The Source
==============

The git repository is available at:

http://github.com/krishardy/dynip



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

