import socket
import json
import logging
import sys
import datetime


log = logging.getLogger(__name__)
UDP_IP = "*"
UDP_PORT=28630
#ADDR_LOG="/var/www/sakarta.com/dynaddr.json"
CLIENT_LOG_PATH="dynip.json"


def main(argv):
    global log, UDP_IP, CLIENT_LOG_PATH

    log.info("Starting server...")

    log.info(
            "Listening on port {0}"\
                    .format(UDP_PORT)
                    )
    sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
            )

    if UDP_IP == "*":
        UDP_IP = socket.gethostbyname(
                socket.gethostname()
                )

    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)

        log.info(
                "Received packet from {0}"\
                        .format(addr))

        try:
            client_log_fh = open(CLIENT_LOG_PATH, "w")
        except:
            log.info("ERROR: Could not open {0}".format(CLIENT_LOG_PATH))
            continue

        try:
            client_data = json.load(client_log_fh)
        except:
            client_data = {}

        client_data[data] = [addr[0], datetime.datetime.now().isoformat(' ')]

        log.info("Saving data")
        json.dump(client_data, client_log_fh)
        client_log_fh.close()

    sock.close()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
