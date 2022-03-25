import datetime
import socket
import os

if __name__ == "__main__":
    ts = datetime.datetime.now()
    home_dir = os.environ["HOME"]
    user = os.environ["USERNAME"]
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    with open ("web.log", "w") as tf:
        tf.write("{}: {}@{} ip: {} home-dir: {}".format(ts, user, hostname, local_ip, home_dir))

