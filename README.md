# Image to JPEG Converter (Processador de Imagens Pro)

Um aplicativo simples com interface gráfica, feito em Python utilizando CustomTkinter, para converter diversos formatos de imagem para o formato JPEG. 
Ele suporta a conversão de múltiplas imagens em lote.

## Funcionalidades

- Conversão de vários formatos de imagem modernos e nativos para `.jpg`.
- Suporte a transparência (imagens com fundo transparente ganham um fundo apropriado e conservam as cores quando convertidas para JPG).
- Processamento em Lote: selecione uma ou dezenas de imagens e processe todas simultaneamente, salvando-as em um diretório alvo.
- Interface Moderna: O design e estilo gráfico foram criados com `customtkinter`.

## Formatos Suportados

Atualmente, o app consegue ler e converter os seguintes formatos para JPEG:

* **Padrões da Web / Desktop:** PNG, WEBP, JPEG (.jpg, .jpeg)
* **Alta Eficiência / Mobile:** HEIF, HEIC (.heif, .heic)
* **Formato Crú / Fotografia (RAW):** RAW, CR2, NEF, ORF, SR2, DNG, ARW
* **Padrões de Alta Qualidade:** TIFF (.tiff, .tif)
* **Gráficos Vetoriais:** SVG (.svg)

## Requisitos e Instalação

Você precisará do **Python 3** instalado em seu sistema e das bibliotecas abaixo para rodar o aplicativo.

Abra o terminal na pasta do projeto e execute este comando para instalar todas as dependências de uma vez:

```bash
pip install customtkinter pillow pillow-heif rawpy svglib reportlab
```

### O que cada biblioteca faz?
* `customtkinter`: Usada para criar uma interface de usuário moderna.
* `Pillow` (PIL): Motor principal de abertura, manipulação e salvamento das imagens.
* `pillow-heif`: Adiciona o suporte à leitura do codec `.heic` e `.heif` pela biblioteca Pillow.
* `rawpy`: Interpretador de arquivos `RAW` de diversas câmeras fotográficas (ex: `.cr2`, `.nef`, `.dng`).
* `svglib` e `reportlab`: Lidam com a leitura e rasterização de vetores matemáticos `.svg` para imagens tradicionais (bitmap).

## Como Executar

Simplesmente execute o arquivo principal usando o seu Python via terminal/Prompt de Comando:

```bash
python imagem.py
```
