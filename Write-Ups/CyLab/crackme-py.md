# Crackme-py

**Categoria:** Engenharia Reversa     
**Nível:** Médio     
**Plataforma:** CyLab     
**Autor:** Luis Pedro do Carmo Costa    

---

## Introdução

Este write-up mostra como resolvi o desafio **Crackme-py**, da categoria de Engenharia Reversa (nível médio) no CyLab. O desafio foi proposto durante a escola de cibersegurança do Inatel.

O desafio entrega um arquivo em Python, o `crackme_gen.py`, e o objetivo é encontrar a flag escondida dentro do código.

## Análise do código

Comecei lendo o código inteiro, porque em Engenharia Reversa a primeira coisa a fazer é entender o que o programa tem e o que ele faz. Logo no início do arquivo, encontrei estes comentários e uma variável:

```python
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "24256>JL`>0c0Abc?FE02a_53e7fe7af5gN"
```

Os comentários dizem que o "número importante" está criptografado, e a variável `bezos_cc_secret` tem cara de texto cifrado: uma sequência de caracteres sem sentido, misturando letras, números e símbolos. Então o objetivo ficou claro: descobrir qual cifra foi usada e desfazê-la.

Continuando a leitura, encontrei duas coisas importantes:

1. A variável `alphabet`, que guarda todos os caracteres imprimíveis da tabela ASCII (de `!` até `~`), um total de 94 caracteres.
2. A função `decode_secret(secret)`, que tem na própria descrição a operação **ROT47**.

<img width="456" height="292" alt="Captura de tela 2026-11-04 144724" src="https://github.com/user-attachments/assets/5cd5beb3-1a29-40c5-8f07-9f91842a8475" />

Olhando o corpo da função, o que ela faz com cada caractere do texto é:

- procura a posição do caractere no `alphabet`;
- soma 47 a essa posição (`rotate_const = 47`);
- usa o resto da divisão por 94 (`% len(alphabet)`) para dar a volta quando passa do fim;
- pega o caractere que está na nova posição.

Esse é justamente o funcionamento do ROT47: uma cifra de rotação que desloca cada caractere em 47 posições dentro dos 94 caracteres imprimíveis. Como 47 é exatamente a metade de 94, aplicar a operação duas vezes devolve o texto original. Por isso o comentário do código diz que *encode* e *decode* são a mesma operação.

### Uma observação sobre o programa

Percebi que a função `decode_secret` **nunca é chamada**: no final do arquivo só a função `choose_greatest()` é executada, e ela só pede dois números ao usuário. Ou seja, rodar o programa não revela nada. A flag só aparece quando analisamos o código e entendemos o que ele esconde, o que é bem a ideia de um desafio de Engenharia Reversa.

---

## Resolução

Com a cifra identificada, não era preciso rodar o código. Usei o **CyberChef**, que já tem a operação ROT47 pronta:

1. Coloquei o texto de `bezos_cc_secret` no campo **Input**.
2. Adicionei a operação **ROT47** na receita, com o valor **Amount = 47**, o mesmo `rotate_const` do código.
3. O resultado apareceu no campo **Output**.

<img width="1917" height="762" alt="Captura de tela 2026-11-04 145639" src="https://github.com/user-attachments/assets/a7a162f4-dc46-46ea-a8b6-7884d71c0936" />

---

## Flag

```text
academy{1m_4_p34nut_a20db6f76f27d8}
```

---

## Conclusão

O ROT47 não é criptografia de verdade. Ele não usa chave secreta: o valor 47 é fixo e qualquer pessoa que reconheça a cifra consegue desfazê-la em segundos. Isso é ofuscação, não proteção. O próprio código chama o `rotate_const` de "Encryption key", mas ele é só o tamanho do deslocamento, e o desafio mostra bem por que guardar um dado sensível desse jeito dentro do código-fonte não é seguro.
