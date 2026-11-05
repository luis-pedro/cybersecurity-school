# VaultDoor1

**Categoria:** Engenharia Reversa     
**Nível:** Médio     
**Plataforma:** CyLab    
**Autor:** Luis Pedro do Carmo Costa      

---

## Introdução

Este write-up mostra como resolvi o desafio **VaultDoor1**, da categoria de Engenharia Reversa (nível médio) no CyLab. O desafio foi proposto durante a escola de cibersegurança do Inatel.

O desafio entrega um arquivo em Java, o `VaultDoor1.java`, e o objetivo é encontrar a flag escondida dentro do código.

## Análise do código

Comecei lendo o código inteiro para entender o que o programa faz. Ele pede uma senha ao usuário e responde "Access granted." ou "Access denied!", então a flag é a senha que faz o programa liberar o acesso.

### A função `main`

Na `main`, o programa lê o que o usuário digitou e faz isto:

```java
String input = userInput.substring("academy{".length(),userInput.length()-1);
```

Essa linha remove o começo `academy{` e o último caractere `}`, ficando só com o conteúdo de dentro das chaves. Só esse conteúdo é enviado para a função `checkPassword`. Isso mostra que a flag segue o formato `academy{...}` e que o que importa descobrir é o que fica entre as chaves.

### A função `checkPassword`

Acima da função `checkPassword`, há um comentário de quem escreveu o código:

```java
// I came up with a more secure way to check the password without putting
// the password itself in the source code. I think this is going to be
// UNHACKABLE!! I hope Dr. Evil agrees...
```

O comentário diz que a senha não está escrita no código, mas a função retorna uma sequência de comparações ligadas por `&&`. Para a senha ser aceita, todas elas precisam ser verdadeiras:

- a primeira exige que a senha tenha exatamente **32 caracteres** (`password.length() == 32`);
- as outras 32 comparações têm o formato `password.charAt(posição) == 'letra'`, ou seja, dizem qual caractere deve estar em cada posição.

Então a senha está no código, só que **embaralhada**: as comparações aparecem fora de ordem (posição 0, depois 29, depois 4, depois 2 e assim por diante), o que dificulta ler a senha de cima para baixo.

## Resolução

Para resolver, não foi preciso executar o programa. Reorganizei as comparações pela posição, do índice 0 ao 31, e montei a senha caractere por caractere:

```text
 0:d   1:3   2:5   3:c   4:r   5:4   6:m   7:b
 8:l   9:3  10:_  11:t  12:H  13:3  14:_  15:c
16:H  17:4  18:r  19:4  20:c  21:T  22:3  23:r
24:5  25:_  26:e  27:3  28:f  29:f  30:6  31:3
```

Lendo da posição 0 até a 31, o resultado é `d35cr4mbl3_tH3_cH4r4cT3r5_e3ff63`. Como a `main` retira `academy{` e `}` antes de verificar, coloquei de volta o formato da flag no resultado final.

## Flag

```text
academy{d35cr4mbl3_tH3_cH4r4cT3r5_e3ff63}
```

---

## Conclusão

Esse desafio mostra que embaralhar a ordem das verificações não esconde a senha. Cada caractere continua escrito em texto puro no código, e quem lê o arquivo consegue recompor tudo. Qualquer senha que o programa precise comparar internamente fica exposta a quem tiver o código-fonte.
