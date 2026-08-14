# Backup Criptografado

###### Categoria: Crypto
###### Autor: Luis Pedro do Carmo Costa

##  **Introdução**

Esse desafio tem como dificuldade fácil e faz parte de uma série de desafios propostos pela Escola de Cyber do INATEL.

## **Resolução**

Em primeiro lugar, na descrição do desafio diz:

> O algoritmo utilizado foi AES-128 -O modo de operação foi ECB -A chave possui 16 caracteres  
> A chave utilizada foi: cybersecurity!!!

Após analisar as informações fornecidas, concluí que o algoritmo utilizado na criptografia era o AES-128 e que a chave possuía 16 caracteres. Dessa forma, utilizei o CyberChef para realizar a descriptografia do conteúdo interceptado.

Primeiramente, utilizei a operação **"From Base64"** para decodificar o conteúdo, pois os dados estavam representados em Base64. Em seguida, utilizei a operação **"AES Decrypt"**, configurando o modo de operação como **ECB** e utilizando a chave fornecida, `cybersecurity!!!`.

Após realizar essas operações, foi possível obter o conteúdo original da mensagem, revelando a flag:

```text
DUCK{AES_is_symmetric_crypto}
```

<img width="1545" height="897" alt="Captura de Tela (149)" src="https://github.com/user-attachments/assets/17e7aa62-21fd-463d-b67a-3eb77b12194c" />

## **Conclusão**

Esse desafio foi importante para meu desenvolvimento na área de cibersegurança e também, foi importante para aprimorar meus conceitos em cripto.
