import telnetlib
import json
import base64
import codecs

HOST = 'socket.cryptohack.org'
PORT = 13377

tn = telnetlib.Telnet(host=HOST, port=PORT)

def readline():
    return tn.read_until(b"\n")

def receive_data():
    data = readline().decode()
    data = json.loads(data)
    return data

def send_data(data):
    data = json.dumps(data).encode()
    tn.write(data)

def de_rot13(en_str):
    return codecs.decode(en_str, 'rot_13')

def de_hex(en_str):
    return bytes.fromhex(en_str).decode()

def de_utf8(en_str):
    de = ''
    for i in en_str:
        de += chr(i)
    return de

def de_bigint(en_str):
    return bytes.fromhex(en_str[2:]).decode()

def de_base64(en_str):
    return base64.b64decode(en_str).decode()

def solve(type, en_str):
    if type == 'rot13':
        return de_rot13(en_str)
    elif type == 'hex':
        return de_hex(en_str)
    elif type == 'utf-8':
        return de_utf8(en_str)
    elif type == 'bigint':
        return de_bigint(en_str)
    else:
        return de_base64(en_str)

while True:
    receive_json = receive_data()
    print("Received data: %s" % receive_json)
    type = receive_json['type']
    en_str = receive_json['encoded']

    send = {
        "decoded": solve(type, en_str)
    }

    send_data(send)