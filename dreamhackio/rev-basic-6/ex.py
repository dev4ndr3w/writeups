#!/usr/bin/env python2

_data_offset = 0x00002400

with open("./chall6.exe", "r") as f:
    data = f.read()
    n = data[_data_offset+0x20:_data_offset+0x11f]
    enc_flag = data[_data_offset:_data_offset+0x12]
    f.close()

dec_flag = ""
for j in range(len(enc_flag)):
    for i in range(0x20, 0x7e):
        if enc_flag[j] == n[i]:
            dec_flag += chr(i)

print(dec_flag)
