#!/usr/bin/env python3

from pwn import *
import os

context.log_level = "debug"

server = ["pwnable.kr", 2222, "input2", "guest"]

def connection():
    connectionHandle = ssh(host=server[0], port=server[1], user=server[2], password=server[3])
    return connectionHandle

if __name__ == "__main__":
    connectionHandle = connection()
    connectionHandle.upload_file("./local-exploit.py", "/tmp/dev4ndr3w/local-exploit.py")
    processHandle = connectionHandle.run("ln -s /home/input2/flag /tmp/dev4ndr3w/flag")
