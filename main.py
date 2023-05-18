from secp348 import curve,scalar_mult
import random
import socket

# Long-term Private key: a
a = random.randrange(1, curve.n)
# Long-term Public key: a * G
a_pub = scalar_mult(a, curve.g)


"""The session key part"""
# Receiving their long-term public key
# b = random.randrange(1, curve.n)
# b_pub = scalar_mult(b, curve.g)
# This is session key
# x  = random.randrange(1, curve.n)
# xG = scalar_mult(x, curve.g)
# y  = random.randrange(1, curve.n)
# yG = scalar_mult(y, curve.g)
# B_send = scalar_mult(y, a_pub)
# B_send = scalar_mult(b, Bob_send)
# Sending Session Key
# A_send = scalar_mult(x, b_pub)
# A_send = scalar_mult(a, Alice_send)
# Check Shared key
# k_a = scalar_mult(x, B_send)
# k_b = scalar_mult(y, A_send)
# print("\nA\'s secret key (a):\t", a)
# print("A\'s public key:\t", a_pub)
# print("\nB\'s secret key (b):\t", b)
# print("B\'s public key:\t", b_pub)
# print("\nA\'s session secret key (a):\t", x)
# print("A\'s  session public key:\t", Al_send)
# print("\nB\'s  session secret key (b):\t", y)
# print("B\'s  session public key:\t", B_send)
# print("A\'s shared key:\t", k_a)
# print("B\'s shared key:\t", k_b)
# print("abxyG: \t", (k_a[0]))
# res=(a*b*x*y) % curve.n
# res=scalar_mult(res, curve.g)
# print("(abxy)G \t", (res[0]))
"""End"""

def send(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print(a_pub)
    s.sendall(str(a_pub).encode())
    s.close()
def receive(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    conn, addr = s.accept()
    received_data = b""
    data = conn.recv(1024)
    print(data)
    conn.close()
    return data

host = "172.20.10.10"
port = 9999

send(host, port)
BPublicKey= receive(port)
sharedSecret2 = scalar_mult(a, eval(BPublicKey))

print("==========================")
print("B\'s shared key:\t", sharedSecret2)

print("\n==========================")

# Verify
# print("abG: \t", (sharedSecret2[0]))
# res=(a_pub*b_pub) % curve.n
# res=scalar_mult(res, curve.g)
# print("(ab)G \t", (res[0]))
