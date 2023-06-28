from Crypto.Util.number import *

hex = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
str = long_to_bytes(int(hex, 16)).decode()

flag = 'crypto{'

def preXorKey():
    return long_to_bytes(bytes_to_long(str[0:7].encode()) ^ bytes_to_long(flag.encode())).decode()

preXorKey = preXorKey()
xorKey = preXorKey + 'y' # myXORkey

for i in range(0, 5):
    print(long_to_bytes(bytes_to_long(str[8*i:8*i+8].encode()) ^ bytes_to_long(xorKey.encode())).decode(), end = '')
print(long_to_bytes(bytes_to_long(str[-2:].encode()) ^ bytes_to_long('my'.encode())).decode())