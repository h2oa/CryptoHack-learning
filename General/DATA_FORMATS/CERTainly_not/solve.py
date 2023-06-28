from Crypto.PublicKey import RSA

f = open('2048b-rsa-example-cert.der', 'rb')
key = RSA.importKey(f.read())

print(key.n)