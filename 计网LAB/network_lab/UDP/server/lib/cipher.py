from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA


def encrypt_AESkey(AESkey: bytes, pubKeyPEM: bytes) -> bytes:
    """encrypt AESkey using RSC public key PEM"""
    # creating RSC pubkey using pubkeyPEM
    pubKey = RSA.import_key(pubKeyPEM)
    # encrypt
    encryptor = PKCS1_OAEP.new(pubKey)
    return encryptor.encrypt(AESkey)

class AESCipher:
    """using ECB mode"""
    def __init__(self, AES_key: bytes):
        self.key = AES_key
        self.cipher = AES.new(self.key, AES.MODE_ECB)
        self.plaintext = ''

    def set_plaintext(self, plaintext):
        self.plaintext = plaintext
        self.padding()

    def padding(self):
        padding = 4 - len(self.plaintext) % 4
        if padding:
            self.plaintext += b'=' * padding

    def decrypt(self, ciphertext):
        ret = self.cipher.decrypt(ciphertext)
        ret = ret.decode('utf-8','ignore')
        ret = ret.rstrip('\0')
        return ret

    def encrypt(self, plaintext: str):
        plaintext = plaintext.encode('utf-8')
        cnt = len(plaintext) % 16
        plaintext += ('\0' * (16 - cnt)).encode('utf-8')
        ret = self.cipher.encrypt(plaintext)
        return ret


class RSCCipher:
    def __init__(self):
        # initializing keypair
        self.keyPair = RSA.generate(2048)
        self.pubKey = self.keyPair.publickey()
        self.pubKeyPEM: bytes = self.pubKey.exportKey()
        self.privKeyPEM: bytes = self.keyPair.exportKey()

        # getting private key
    def decrypt(self, msg: bytes) -> bytes:
        privKey = RSA.import_key(self.privKeyPEM)
        decryptor = PKCS1_OAEP.new(privKey)
        return decryptor.decrypt(msg)
