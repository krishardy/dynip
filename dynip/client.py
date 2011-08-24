#!/usr/bin/python
"""
DynIP Client

A embarrisingly-simple client with sends UDP packets to the DynIP server.
"""
"""
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
import argparse
import ConfigParser
import traceback
import return_codes as rc

CONFIG_SECTION = "DynIP:Client"

# DEFAULT_SERVER_HOSTNAME:
#   Hostname or IP Address
#   Example:
#     DEFAULT_SERVER_HOSTNAME="127.0.0.1"  # By IP Address
#     DEFAULT_SERVER_HOSTNAME="google.com"  # By domain name
DEFAULT_SERVER_HOSTNAME="localhost"

# DEFAULT_SERVER_PORT:
#   The port that the server is listening on 
DEFAULT_SERVER_PORT=28630

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)


# Prepare argparser
argparser = argparse.ArgumentParser(description="Sends a single packet to the DynIP server.")
argparser.add_argument('-v', '--verbose', help="Enable verbose (INFO-level) logging",
        action='store_const',
        default=logging.WARNING,
        const=logging.INFO
        )
argparser.add_argument('--debug', help="Enable debug (DEBUG-level) logging",
        action='store_const',
        default=logging.WARNING,
        const=logging.DEBUG
        )
argparser.add_argument('config', help="Configuration .conf file",
        type=str, nargs=1)


def main(argv):
    """
    Send a single UDP datagram to the server

    :argv: List of command line arguments from sys.argv
    """

    # Parse the command-line arguments
    args = argparser.parse_args()
    log.setLevel(min(args.verbose, args.debug))

    try:
        config = ConfigParser.ConfigParser(
                {CONFIG_SECTION:
                    {'server_hostname': DEFAULT_SERVER_HOSTNAME,
                     'server_port': DEFAULT_SERVER_PORT
                    }
                })
        config.read(args.config)
        server_hostname = config.get(CONFIG_SECTION, 'server_hostname')
        server_port = config.get(CONFIG_SECTION, 'server_port')
    except:
        log.fatal("ERROR: Could not read configuration file {0}".format(args.config))
        return rc.CANNOT_READ_CONFIG

    # Validate the params
    if server_hostname == "":
        log.fatal("ERROR: server_hostname is required")
        return rc.SERVER_HOSTNAME_MISSING


    log.debug("Looking up hostname")
    server_ip = socket.gethostbyname(server_hostname)

    if send_packet(server_ip, server_port) == True:
        return rc.OK
    else:
        return rc.PACKET_SEND_FAILED

def send_packet(destination_ip, destination_port):
    """
    Send a single UDP packet to the target server.

    :destination_ip: IP address of the server
    :destination_port: Port number of the server
    """
    try:
        import socket

        log.debug("Preparing message")
        message = socket.gethostname()

        log.debug("Preparing socket")
        sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_DGRAM
                )

        log.debug("Sending UDP datagram to {0}:{1}".format(destination_ip, destination_port))
        sock.sendto(message, (destination_ip, int(destination_port)))
        return True
    except:
        log.warning("Packet should not be sent to the destination")
        log.warning(traceback.format_exc())
        return False



def usage():
    """Print usage information"""
    argparser.print_help()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
