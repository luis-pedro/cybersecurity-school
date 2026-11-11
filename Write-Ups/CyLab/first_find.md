# First Find

**Categoria:** Misc   
**Plataforma:** CyLab     
**Autor:** Luis Pedro do Carmo Costa

---

## Introdução

Este write-up mostra como resolvi o desafio **First Find**, da categoria Misc no CyLab. O desafio foi proposto durante a escola de cibersegurança do Inatel.

O desafio entrega um arquivo compactado (`.zip`) com várias pastas e arquivos dentro, e o objetivo é encontrar o arquivo que guarda a flag.

---

## Resolução

### 1. Preparando o ambiente

Baixei o arquivo `.zip` do desafio e extraí o conteúdo com o comando `unzip`. Depois, dentro da pasta extraída, cliquei com o botão direito e escolhi a opção de abrir em um terminal, já que estou usando o Kali Linux. Assim o terminal já abre dentro da pasta certa (`~/Downloads/files`).

### 2. Procurando o arquivo

Procurar o arquivo abrindo uma pasta de cada vez seria demorado, porque há muitas pastas dentro de outras pastas. Por isso usei o comando `find`, que procura arquivos automaticamente:

```bash
find . -name "uber-secret.txt"
```

O que cada parte faz:

- `find` é o comando de busca;
- `.` indica que a busca começa na pasta atual e entra em todas as subpastas;
- `-name "uber-secret.txt"` procura um arquivo com exatamente esse nome.

O comando mostrou onde o arquivo estava:

```text
./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

O arquivo estava escondido bem no fundo de várias pastas aninhadas. Além disso, a pasta `.secret` começa com ponto, e no Linux isso a torna uma **pasta oculta**, que não aparece em uma listagem normal (`ls`) nem no gerenciador de arquivos. Usando o `find`, não precisei saber esse caminho de antemão.

### 3. Lendo o arquivo

Com o caminho em mãos, usei o `cat` para mostrar o conteúdo do arquivo no terminal:

```bash
cat ./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

<img width="1920" height="922" alt="imagem_terminal" src="https://github.com/user-attachments/assets/e0370106-7009-4d57-9de5-590d65a88a38" />

O conteúdo do arquivo é a flag.

---

## Flag

```text
academy{f1nd_15_f457_ab443fd1}
```

---

## Conclusão

Esse desafio mostra como o `find` ajuda a localizar um arquivo em uma estrutura grande de pastas sem precisar abrir uma por uma. Ele também chega em pastas ocultas (as que começam com `.`), que seriam fáceis de passar batido na navegação normal. O `find` combinado com o `cat` resolve o desafio em dois comandos, e a flag (`find is fast`, em leetspeak) fala justamente disso.
