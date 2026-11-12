# Mod 26

**Categoria:** Criptografia   
**Nível:** Fácil    
**Plataforma:** CyLab    
**Autor:** Luis Pedro do Carmo Costa

---

## Introdução

Este write-up mostra como resolvi o desafio **Mod 26**, da categoria Criptografia no CyLab. O desafio foi proposto durante a escola de cibersegurança do Inatel.

O enunciado diz:

> Cryptography can be easy, do you know what ROT13 is?

O desafio entrega um arquivo, o `values.txt`, e o objetivo é descobrir a flag escondida nele.

---

## Análise do enunciado

O enunciado já dá a principal pista: pergunta se eu sei o que é **ROT13**. O ROT13 é uma cifra de substituição muito simples, em que cada letra é trocada pela letra que fica 13 posições à frente no alfabeto. Como o alfabeto tem 26 letras, 13 é exatamente a metade, então aplicar o ROT13 duas vezes devolve o texto original. Isso significa que **cifrar e decifrar são a mesma operação**.

Outro detalhe importante é que o ROT13 só mexe nas **letras**. Números e símbolos (como `{`, `_` e `'`) ficam exatamente como estão.

---

## Resolução

### 1. Abrindo o arquivo

Baixei o arquivo e abri o `values.txt`. Dentro dele havia apenas esta linha:

```text
npnqrzl{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_5p5s5o36}
```

O texto parece uma flag no formato `palavra{...}`, mas as letras não formam palavras. Além disso, o começo `npnqrzl` tem 7 letras, o mesmo tamanho de `academy`, o início das flags da plataforma, o que indica que as letras foram trocadas por uma substituição.

### 2. Decifrando com o dCode

Copiei o texto e colei no **dCode**, que identificou a cifra como ROT13. Usei a própria ferramenta de decifrar ROT13 do site (*ROT13 Decoder*) e o resultado apareceu no campo de resultados.

<img width="1920" height="922" alt="imagem_dcode" src="https://github.com/user-attachments/assets/8c2a33b3-9beb-45f3-af21-de473d38dc97" />

---

## Flag

```text
academy{next_time_I'll_try_2_rounds_of_rot13_5c5f5b36}
```

---

## Conclusão

A flag mostra a brincadeira do desafio: *"next time I'll try 2 rounds of ROT13"* ("da próxima vez vou tentar 2 rodadas de ROT13"). Isso faz sentido porque aplicar o ROT13 duas vezes cancela a cifra e devolve o texto original, então cifrar duas vezes seria o mesmo que não cifrar nada. O ROT13 não é uma criptografia segura: não tem chave, e qualquer pessoa que reconheça a cifra consegue desfazê-la em segundos.
