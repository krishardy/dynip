import socket
import sys
import logging

log = logging.getLogger(__name__)

def main(argv):
    remote_ip = socket.gethostbyname("localhost")
    remote_port=28630
    message = socket.gethostname()
    sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
            )
    sock.sendto(message, (remote_ip, remote_port))

if __name__ == "__main__":
    sys.exit(main(sys.argv))
