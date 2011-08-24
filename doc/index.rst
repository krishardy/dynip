.. DynIP documentation master file, created by
   sphinx-quickstart on Mon Aug 22 22:57:01 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

DynIP documentation
===================

About DynIP
===========

DynIP is an embarrasingly-simple client and server purely for getting systematic updates of a client's IP address.

How it works
------------

The client is typically configured to run on a schedule basis using crontab or Windows Scheduled Tasks.  When launched, the client sends a UDP datagram to the server, with it's hostname in the data packet.

The server, when it receives the UDP datagram, opens a JSON file at the path specified in the ``client_log_path`` of the dynip configuration file.  The server looks to see if the client name (the data portion of the packet) is already in the list of known addresses.  If it is, it updates the record with the new IP address from the packet header and the current date and time.  If it is new, it adds it to the dict of known hosts.


Installation
============

You can download DynIP from PyPi:

http://pypi.python.org/pypi/DynIP

To install, execute the following: ::

    $ easy_install DynIP


Usage
=====

To configure the server, copy or edit example.conf and set the ``server_ip``, ``server_port`` and ``client_log_path`` parameters in the ``DynIP:Server`` section.  Descriptions of each are in example.conf.

Then start the server by typing: ::

    $ python dynip/server.py your_config_file.conf

To launch the client and have it fire off a UDP packet, edit your configuration file (example.conf or whatever you copied it to), and modify the ``server_hostname`` and ``server_port`` lines in the ``DynIP:Client`` section.  Descriptions of each are in the code.

Then launch the client by typing: ::

    $ python dynip/client.py your_config_file.conf

The client will fire a single UDP packet to the server.  The server will then save the hostname, ip address and date/time in the file specified in ``client_log_path`` in the .conf file.


Options
-------

To enable verbose (INFO-level) logging, add `-v` to the command line when launching the server or client. ::

    $ python dynip/server.py -v my_config.conf
    $ python dynip/client.py -v my_config.conf


To enable debug (DEBUG-level) logging, add `--debug` to the command line when launching the server or client. ::

    $ python dynip/server.py --debug my_config.conf
    $ python dynip/client.py --debug my_config.conf


Both the server and client return usage information if you add `--help` or `-h` to the command line when invoking the client or server.


Why I Built It
==============

I am about to go on an extended trip away from home, yet need to know the dynamic IP address that is assigned to my home cable router so that I can easily help my family remotely in case they need help with their computers.  In order to do this, I need to know the IP address that my cable provider as assigned to my cable modem.

By installing the client on each of my computers at home and triggering the client to run every 5 minutes, the server will always keep a log of the most recent public IP address of the boundary device.


License
=======

DynIP is licensed under a BSD License.  See the LICENSE file.


Get The Source
==============

The git repository is available at:

http://github.com/krishardy/dynip


Modules
=======

dynip
-----

.. automodule:: dynip
    :members:
    :show-inheritance:

dynip.server
^^^^^^^^^^^^

.. automodule:: dynip.server
    :members:
    :show-inheritance:

dynip.client
^^^^^^^^^^^^

.. automodule:: dynip.client
    :members:
    :show-inheritance:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

