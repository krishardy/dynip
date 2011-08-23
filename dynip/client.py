#!/usr/bin/python
"""
DynIP Client

A embarrisingly-simple client with sends UDP packets to the DynIP server.

Copyright (c) 2011, R. Kristoffer Hardy
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import socket
import sys
import logging

# SERVER_HOSTNAME:
#   Hostname or IP Address
#   Example:
#     SERVER_HOSTNAME="127.0.0.1"  # By IP Address
#     SERVER_HOSTNAME="google.com"  # By domain name
SERVER_HOSTNAME="localhost"

# SERVER_PORT:
#   The port that the server is listening on 
SERVER_PORT=28630

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)

# Return Codes
RETCODE_OK = 0

def main(argv):
    """
    Send a single UDP datagram to the server
    """

    # Handle command-line params
    if "-v" in argv:
        log.setLevel(logging.INFO)

    if "--debug" in argv:
        log.setLevel(logging.DEBUG)

    if "-h" in argv or "--help" in argv:
        usage()
        return RETCODE_OK

    log.debug("Looking up hostname")
    server_ip = socket.gethostbyname(SERVER_HOSTNAME)

    log.debug("Preparing message")
    message = socket.gethostname()

    log.debug("Preparing socket")
    sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
            )

    log.debug("Sending UDP datagram")
    sock.sendto(message, (server_ip, SERVER_PORT))

    return RETCODE_OK


def usage():
    print """client.py ([options])
Sends a single UDP packet to the DynIP server.

Optional:
-h | --help                 Print this usage info
-v                          Enable verbose (INFO-level) logging
--debug                     Enable debug (DEBUG-level) logging
"""


if __name__ == "__main__":
    sys.exit(main(sys.argv))
