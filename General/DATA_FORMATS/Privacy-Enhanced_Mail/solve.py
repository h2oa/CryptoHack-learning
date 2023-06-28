from Crypto.PublicKey import RSA
import base64

f = open('privacy_enhanced_mail.pem', 'r')
key = RSA.importKey(f.read())

print(key.d)