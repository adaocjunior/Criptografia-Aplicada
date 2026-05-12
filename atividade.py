import time
import os
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

texto = b"RSA MIT Rivest Shamir Adleman"


def teste_rsa(bits):
    inicio = time.perf_counter()

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=bits
    )

    public_key = private_key.public_key()

    ciphertext = public_key.encrypt(
        texto,
        padding.PKCS1v15()
    )

    plaintext = private_key.decrypt(
        ciphertext,
        padding.PKCS1v15()
    )

    fim = time.perf_counter()

    return fim - inicio


def teste_ecc():
    inicio = time.perf_counter()

    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()

    assinatura = private_key.sign(
        texto,
        ec.ECDSA(hashes.SHA256())
    )

    public_key.verify(
        assinatura,
        texto,
        ec.ECDSA(hashes.SHA256())
    )

    fim = time.perf_counter()

    return fim - inicio


def teste_aes(bits):
    inicio = time.perf_counter()

    chave = os.urandom(bits // 8)
    iv = os.urandom(16)

    cipher = Cipher(
        algorithms.AES(chave),
        modes.CFB(iv),
        backend=default_backend()
    )

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(texto) + encryptor.finalize()

    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    fim = time.perf_counter()

    return fim - inicio


def teste_des():
    inicio = time.perf_counter()

    chave = os.urandom(8)
    iv = os.urandom(8)

    cipher = Cipher(
        algorithms.TripleDES(chave * 3),
        modes.CFB(iv),
        backend=default_backend()
    )

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(texto) + encryptor.finalize()

    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    fim = time.perf_counter()

    return fim - inicio


def teste_3des(bits):
    inicio = time.perf_counter()

    if bits == 112:
        chave = os.urandom(16)
    else:
        chave = os.urandom(24)

    iv = os.urandom(8)

    cipher = Cipher(
        algorithms.TripleDES(chave),
        modes.CFB(iv),
        backend=default_backend()
    )

    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(texto) + encryptor.finalize()

    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    fim = time.perf_counter()

    return fim - inicio


algoritmos = [
    ("RSA 1024", lambda: teste_rsa(1024)),
    ("RSA 2048", lambda: teste_rsa(2048)),
    ("RSA 4096", lambda: teste_rsa(4096)),
    ("RSA 8192", lambda: teste_rsa(8192)),
    ("ECC 256", teste_ecc),
    ("AES 128", lambda: teste_aes(128)),
    ("AES 256", lambda: teste_aes(256)),
    ("DES 56", teste_des),
    ("3DES 112", lambda: teste_3des(112)),
    ("3DES 168", lambda: teste_3des(168)),
]

print("RESULTADOS DO EXPERIMENTO= ")

for nome, funcao in algoritmos:

    print(f"Executando {nome}...")

    tempos = []

    for i in range(3):
        tempo = funcao()
        tempos.append(tempo)

        print(f"Execucao {i+1}: {tempo:.6f} segundos")

    media = sum(tempos) / len(tempos)

    print(f"Tempo medio: {media:.6f} segundos")