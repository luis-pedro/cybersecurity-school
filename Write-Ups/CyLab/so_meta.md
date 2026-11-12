# So Meta

**Categoria:** OSINT     
**Nível:** Fácil   
**Plataforma:** CyLab    
**Autor:** Luis Pedro do Carmo Costa    

---

## Introdução

Este write-up mostra como resolvi um desafio de **OSINT** no CyLab, proposto durante a escola de cibersegurança do Inatel. O desafio entrega uma imagem, a `pico_img.png`, e pede para encontrar a flag escondida nela.

O enunciado vinha com duas dicas:

> 1. What does meta mean in the context of files?
> 2. Ever heard of metadata?

As dicas já apontavam o caminho: a resposta não estava na parte visível da imagem, e sim nos **metadados** do arquivo.

---

## Análise do enunciado

No começo eu fiquei na dúvida, porque o desafio é da categoria **OSINT** e a minha primeira ideia foi procurar a imagem na internet (busca reversa, pesquisar o nome do arquivo, etc.). Mas isso não faria sentido aqui por dois motivos:

1. A flag de um desafio é uma string única, gerada só para aquele desafio (no CyLab elas têm o formato `academy{...}`). Ou seja, ela não existe em lugar nenhum da internet — foi escrita **dentro do arquivo**.
2. As duas dicas falavam diretamente em **metadata**.

Aí a ficha caiu: extrair metadados de um arquivo **também é OSINT**. OSINT não é só "procurar no Google" — é coletar informação de fontes abertas, e os dados escondidos dentro de um arquivo (autor, software usado, data, comentários) são exatamente isso. Muitas vezes é o primeiro lugar que a gente olha.

---

## Resolução

Metadados são informações que ficam gravadas no arquivo além da imagem em si: quem criou, com qual programa, quando, comentários, nome do autor, etc. A ferramenta padrão para ler isso é o **exiftool**, que já vem na Kali.

No terminal, dentro da pasta onde baixei a imagem, rodei:

```bash
exiftool pico_img.png
```

O `exiftool` listou todos os campos de metadados do arquivo. A maioria era coisa normal de uma imagem feita no Photoshop:

- `Software: Adobe ImageReady`
- um bloco grande de **XMP** com IDs internos do Adobe

Mas um campo chamou a atenção, porque tinha um conteúdo que claramente não era o nome de um artista de verdade:

```
Artist: academy{s0_m3ta_45015e26}
```

A flag estava ali, em texto limpo, sem codificação nenhuma, dentro do campo **`Artist`**.

Para quem preferir, dá para achar a mesma coisa com o `strings`, que lista todos os trechos de texto legível dentro do arquivo binário:

```bash
strings pico_img.png | grep academy
```

E ele devolve direto:

```
academy{s0_m3ta_45015e26}
```

---

## Flag

```text
academy{s0_m3ta_45015e26}
```

---

## Conclusão

O próprio nome da flag é uma brincadeira: **`s0_m3ta`** ("so meta"), confirmando que o objetivo era justamente olhar os **meta**dados.

O campo `Artist` é um lugar totalmente legítimo dos metadados de uma imagem — serve para gravar o nome do autor. E é exatamente por isso que ele funciona bem como esconderijo: passa despercebido porque "parece normal" para quem só bate o olho na imagem.

A lição que fica é simples: em qualquer desafio que envolva uma imagem (ou qualquer arquivo), vale sempre rodar o `exiftool` antes de assumir que não tem nada escondido. Muita informação que parece invisível está a um comando de distância.
