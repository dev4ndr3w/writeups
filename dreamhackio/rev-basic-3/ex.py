#!/usr/bin/env python

crypt_flag = [0x49, 0x60, 0x67, 0x74, 0x63, 0x67, 0x42, 0x66, 0x80, 0x78, 0x69, 0x69, 0x7B, 0x99, 0x6D, 0x88, 0x68, 0x94, 0x9F, 0x8D, 0x4D, 0xA5, 0x9D, 0x45]
plain_flag = ""


for key in range(0, 24):
    plain_flag += chr(key^(crypt_flag[key]-key*2))

print("{}".format(plain_flag))
