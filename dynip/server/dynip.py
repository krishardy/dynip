"""
DynIP Server

A embarrisingly-simple server which listens for UDP packets and logs
the data, the source IP address and time.

Copyright (c) 2011, R. Kristoffer Hardy
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import socket
import json
import logging
import sys
import datetime
import traceback
import os



# UDP_IP
#   IP Address that the server will listen on.
#   "*" means that dynip should self-discover the ip address
UDP_IP = "*"

# UDP_PORT
#   Port number that the server will listen on.
UDP_PORT=28630

# CLIENT_LOG_PATH
#   Path (absolute path preferred) to the JSON file that will
#   serve as the client log.
CLIENT_LOG_PATH="dynip.json"

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)

# Return Codes (DO NOT EDIT)
RETCODE_CANNOT_OPEN_CLIENT_LOG_PATH=2


def main(argv):
    """
    Listen for UDP packets and save the remote IP address and data
    to the file specified in ``CLIENT_LOG_PATH``

    Notes: This reads the entire JSON file in on each packet, so
    this is not suitable for any significant load or anything but
    a trivial number of clients.
    """
    log.info("Starting server...")

    if os.path.exists(CLIENT_LOG_PATH) == False:
        client_data = {}
    else:
        try:
            log.info("Opening CLIENT_LOG_PATH: {0}".format(CLIENT_LOG_PATH))
            client_log_fh = open(CLIENT_LOG_PATH, "r")
        except:
            print "ERROR: Could not open {0}".format(CLIENT_LOG_PATH)
            return RETCODE_CANNOT_OPEN_CLIENT_LOG_PATH

        log.info("Opened CLIENT_LOG_PATH successfully".format(CLIENT_LOG_PATH))

        try:
            log.info("Importing json data from CLIENT_LOG_PATH")
            client_data = json.load(client_log_fh)
            if isinstance(client_data, dict) == False:
                client_data = {}
        except:
            log.debug(traceback.format_exc())
            log.info("Improper format of CLIENT_LOG_PATH found.  Starting from scratch.")
            client_data = {}

        log.debug(client_data)

        client_log_fh.close()

    log.info("Opening UDP socket")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if UDP_IP == "*":
        log.info("Discovering IP address")
        listen_ip = socket.gethostbyname(
                socket.gethostname()
                )
    else:
        listen_ip = UDP_IP

    sock.bind((listen_ip, UDP_PORT))

    log.info("Listening on {0}:{1}".format(UDP_IP, UDP_PORT))

    # Enter the listen loop
    if listen_loop(sock, client_data, CLIENT_LOG_PATH) != True:
        log.error("The listen_loop did not exit gracefully.")

    # Shut down gracefully
    log.info("Shutting down the server")
    sock.close()
    log.info("Server stopped")

    return 0


def listen_loop(sock, client_data, log_path):
    while True:
        # Block while waiting for the next packet
        try:
            log.debug("Waiting for the next packet")
            data, addr = sock.recvfrom(1024)
        except KeyboardInterrupt:
            # Break out of loop and exit gracefully
            break

        log.debug("Received packet from {0} | Data: {1}".format(addr, data))

        # Add the data to the client_data dict
        client_data[data] = [
                addr[0],
                datetime.datetime.now().isoformat(' ')
                ]

        # Write out the changes to a clean file
        log.info("Saving data")
        client_log_fh = open(CLIENT_LOG_PATH, "w")
        json.dump(client_data, client_log_fh)
        client_log_fh.close()

    return True



if __name__ == "__main__":
    sys.exit(main(sys.argv))
