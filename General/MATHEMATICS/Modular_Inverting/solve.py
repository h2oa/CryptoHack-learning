'''
What is the inverse element: 3 * d ≡ 1 mod 13?
'''

p = 13
d = (3 ** (p - 2)) % 13

print(d)