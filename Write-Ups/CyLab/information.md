# Information

**Categoria:** Forense    
**Nível:** Fácil    
**Plataforma:** CyLab    
**Autor:** Luis Pedro do Carmo Costa

---

## Introdução

Este write-up mostra como resolvi o desafio **Information**, da categoria Forense (nível fácil) no CyLab. O desafio foi proposto durante a escola de cibersegurança do Inatel.

O desafio entrega um arquivo de imagem, o `cat.jpg` (uma foto de um gatinho), e o enunciado diz:

> Files can always be changed in a secret way. Can you find the flag?

O objetivo é descobrir onde a flag foi escondida dentro do arquivo.

---

## Análise do enunciado

A frase "files can always be changed in a secret way" diz que o arquivo foi alterado de forma escondida. Olhando a imagem, não há nada diferente à vista. Isso indica que a flag não está no desenho da foto, e sim em algum outro lugar do arquivo.

Em arquivos de imagem, os lugares mais comuns para esconder informação são os **metadados**, ou seja, os dados que ficam guardados junto com a imagem, como autor, câmera, data e licença. Por isso comecei por eles.

---

## Resolução

### 1. Primeira tentativa: site online

Primeiro tentei um site online de visualização de metadados, mas não encontrei nada de útil. Sites desse tipo costumam mostrar só os campos básicos, então passei a usar uma ferramenta que mostra tudo.

### 2. Listando os metadados com o `exiftool`

No terminal do Kali, dentro da pasta do arquivo, usei o `exiftool`, que lista todos os metadados de um arquivo:

```bash
exiftool cat.jpg
```

Os campos `Copyright Notice` e `Rights` só mostram `PicoCTF`, que não ajuda. Já o campo **License** chamou a atenção:

```text
License : YWNhZGVteXt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```

Um campo de licença normalmente guarda um texto ou um link, e este tem uma sequência sem sentido de letras e números.

### 3. Confirmando com o `strings`

Para confirmar que o valor realmente está dentro do arquivo, usei o `strings`, que mostra os textos legíveis de um arquivo, junto com o `grep` para filtrar pela palavra "license":

```bash
strings cat.jpg | grep -i license
```

O resultado foi a linha do bloco de metadados XMP, com o mesmo valor:

```text
<cc:license rdf:resource='YWNhZGVteXt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'/>
```

### 4. Decodificando

Essa sequência só tem letras maiúsculas, minúsculas e números, e tem 44 caracteres, formato típico de **Base64**, uma forma de representar texto usando só caracteres comuns.

Na primeira vez, rodei o `base64` sem nenhuma opção. Em vez de decodificar, o comando **codificou** o texto de novo, e a saída (`WVdOaFpH...`) continuou sem sentido. Para decodificar, é preciso usar a opção `-d` (de *decode*):

```bash
echo 'YWNhZGVteXt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9' | base64 -d
```

Com o `-d`, o resultado foi a flag.

<img width="1920" height="922" alt="imagem_terminal03" src="https://github.com/user-attachments/assets/41cf0170-06ef-43be-b00c-9b99e7153f78" />

---

## Flag

```text
academy{the_m3tadata_1s_modified}
```

---

## Conclusão

A flag estava escondida nos metadados da imagem, dentro do campo de licença, e não na imagem em si. O próprio texto da flag (`the metadata is modified`) diz isso. O desafio mostra que é preciso olhar além do que se vê em um arquivo, e que um campo com um valor que não combina com o nome dele (como uma "licença" que não é um link) merece atenção. Também mostra que Base64 não é criptografia: é só uma forma de escrever o texto, e qualquer pessoa consegue desfazê-la com um comando.
