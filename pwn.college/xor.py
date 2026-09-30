key = int(input("Digite o valor da chave: ")) # Chave

e = int(input("Digite o valor do Encrypted secret: ")) # Encrypted secret

d = key ^ e # Decrypted secret
print(d)