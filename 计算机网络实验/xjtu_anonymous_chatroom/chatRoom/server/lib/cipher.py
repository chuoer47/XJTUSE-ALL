from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def encrypt_AESkey(AESkey: bytes, pubKeyPEM: bytes) -> bytes:
    """encrypt AESkey using RSC public key PEM"""
    # creating RSC pubkey using pubkeyPEM
    pubKey = RSA.import_key(pubKeyPEM)
    # encrypt
    encryptor = PKCS1_OAEP.new(pubKey)
    return encryptor.encrypt(AESkey)
