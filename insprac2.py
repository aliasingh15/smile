from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair=RSA.generate(1024)
pubKey=keyPair.publickey()

print(f"public key:(n={hex(pubKey.n)},e={hex(pubKey.e)})")
pubKeyPEM=pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
privKey=keyPair

print(f"Private Key:(n={hex(privKey.n)},d={hex(privKey.n)})")
privKeyPEM=privKey.exportKey()
print(privKeyPEM.decode('ascii'))

msg="Ismile Academy"
encryptor=PKCS1_OAEP.new(pubKey)
encrypted=encryptor.encrypt(msg.encode('utf-8'))
print("Encrypted:",binascii.hexlify(encrypted).decode('utf-8'))
