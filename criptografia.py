from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

data = input("\nDigite a mensagem para criptografar: ").encode("utf-8")

chave_publica = RSA.import_key(open("chave_publica.pem").read())
cifra_rsa_publica = PKCS1_OAEP.new(chave_publica)
texto_encriptado = cifra_rsa_publica.encrypt(data)

chave_privada = RSA.import_key(open("chave_privada.pem").read())
cifra_rsa_privada = PKCS1_OAEP.new(chave_privada)
texto_desencriptado = cifra_rsa_privada.decrypt(texto_encriptado)

print("Texto encriptado:", texto_encriptado)
print("Texto desencriptado:", texto_desencriptado.decode("utf-8"))