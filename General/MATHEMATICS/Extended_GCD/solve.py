import math

p = 26513
q = 32321
gcd = 1

u = 1

while True:
    if (gcd - p * u) % q == 0:
        v = (gcd - p * u) // q
        print('u = %s, v = %s' % (u, v))
        break
    u += 1