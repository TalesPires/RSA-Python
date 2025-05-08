from Cryptodome.PublicKey import RSA

chave = RSA.generate(2048)

chave_privada = chave.export_key()

chave_publica = chave.publickey().export_key()

with open("chave_privada.pem", "wb") as f:
    f.write(chave_privada)
    
with open("chave_publica.pem", "wb") as f:
    f.write(chave_publica)
