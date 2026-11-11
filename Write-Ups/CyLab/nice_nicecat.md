# nice netcat...

**Categoria:** Misc    
**Plataforma:** CyLab    
**Autor:** Luis Pedro do Carmo Costa

---

## Introdução

Este write-up mostra como resolvi o desafio **nice netcat...**, da categoria Misc no CyLab. O desafio foi proposto durante a escola de cibersegurança do Inatel.

O desafio não entrega nenhum arquivo. Ele aponta para um servidor remoto, e o objetivo é descobrir o que esse servidor responde e encontrar a flag.

---

## Análise do enunciado

O enunciado diz:

> There is a nice program that you can talk to by using this command in a shell: `$ nc xebec.cylabacademy.net 25784`, but it doesn't speak English...

Duas partes do texto me deram pistas:

1. **O comando `nc`:** é o *netcat*, uma ferramenta que abre uma conexão de rede (host e porta) e deixa conversar com o programa do outro lado pelo terminal. Aqui, o host é `xebec.cylabacademy.net` e a porta é `25784`.
2. **"it doesn't speak English":** o programa não responde em texto legível. Isso indica que a resposta vem em algum outro formato, e preciso descobrir qual.

---

## Resolução

### 1. Conectando ao servidor

Executei o comando do enunciado no próprio terminal do CyLab:

```bash
nc xebec.cylabacademy.net 25784
```

Em vez de uma frase, o servidor respondeu com uma lista de números, um por linha:

```text
97
99
97
100
101
109
121
123
103
48
48
100
95
107
49
116
116
121
33
95
110
49
99
51
95
107
49
116
116
121
33
95
51
53
101
48
99
125
10
```

### 2. Identificando o formato

Observei colocando na análise de código do site **dCode**, percebi que o código fornecido estava no formato *ASCII Code*, onde pesquisando um pouco mais, descobri que os números apresentados ficavam entre 33 e 125 justamente por esse motivo, com exceção do último número (10).

### 3. Decodificando

Usei novamente o site **dCode** com a ferramenta *ASCII Code*, colei a lista de números e ela decodificou o texto. O site tenta vários formatos ao mesmo tempo (decimal, binário, octal...), e só a linha de decimal (DEC) retornou texto legível. As outras linhas ficaram só com caracteres sem sentido.

<img width="1920" height="922" alt="Screenshot_2026-11-11_08_51_47" src="https://github.com/user-attachments/assets/fb6cc5f6-09a1-441b-ab07-1229a9d44419" />


O último número `10`, é o código da quebra de linha (`\n`), ou seja, é só o servidor terminando a linha e não faz parte da flag.

---

## Flag

```text
academy{g00d_k1tty!_n1c3_k1tty!_35e0c}
```

---

## Conclusão

O servidor não estava criptografando nada. Ele só enviava os caracteres na forma de números, o que bastou para "não falar inglês". O desafio ensina duas coisas: como usar o `nc` para conversar com um serviço remoto e como reconhecer um código ASCII em decimal, quando os valores ficam entre 32 e 126. A flag (`g00d k1tty! n1c3 k1tty!`) é uma brincadeira com o nome do netcat, que lembra "cat", gato em inglês.
