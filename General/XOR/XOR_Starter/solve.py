str = 'label'
num = 13
flag = ''

for i in str:
    flag += chr(ord(i) ^ num)

print(flag)