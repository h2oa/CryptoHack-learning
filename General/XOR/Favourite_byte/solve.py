from Crypto.Util.number import *

hex = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
num = int(hex, 16)
en_str = long_to_bytes(num).decode()

j = 0
while True:
    flag = ''
    for i in en_str:
        flag += chr(ord(i) ^ j)
    j += 1
    if flag[0:6] == 'crypto':
        print(flag)
        break