from Crypto.Util.number import *

"""
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
"""

hex1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
hex2 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
hex3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
hex4 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

# KEY1, KEY2, KEY3, FLAG in int
KEY1 = int(hex1, 16)
KEY2 = int(hex2, 16) ^ KEY1
KEY3 = int(hex3, 16) ^ KEY2
FLAG = int(hex4, 16) ^ KEY1 ^ KEY2 ^ KEY3

flag = long_to_bytes(FLAG).decode()

print(flag)