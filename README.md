# Padrão MAO de Versionamento / MAO Versioning Standard

![Version](https://img.shields.io/badge/Version-1.0-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellowgreen)
![License](https://img.shields.io/badge/License-MIT-green)

**Creator:** Mario Antonio Oliveira  
**Date:** 20/10/2025  

## Introdução / Introduction

O Padrão MAO de Versionamento é um sistema inspirado no modelo do arXiv, projetado para gerenciar:  
The MAO Versioning Standard is a system inspired by arXiv, designed to manage:

- Trabalhos acadêmicos / Academic papers

- Relatórios e projetos / Reports and projects

- Scripts e códigos / Scripts and code

- Arquivos de design ou mídia / Design or media files

Ele organiza data, número do trabalho e versão, mantendo histórico completo e legível — ideal para quem gosta de organização nerd.  
It organizes date, work number, and version, keeping a complete and readable history — perfect for those who love nerdy organization.

## Estrutura do Código / Code Structure

`[código]-[ano][mes].[dia][número]v[versão]`  
`[code]-[year][month].[day][number]v[version]`

## Componentes / Components
```
| Field    | Example                | Description                                           |
|----------|------------------------|-------------------------------------------------------|
| `código` | 1tiapr, rel, nft, proj | Abreviação do projeto, disciplina ou tipo de trabalho |
| `code`   | 1tiapr, rel, nft, proj | Abbreviation of the project, course, or work type     |
| `ano`    | 25                     | Últimos 2 dígitos do ano (2025 → 25)                  |
| `year`   | 25                     | Last two digits of the year (2025 → 25)               |
| `mês`    | 10                     | Mês do ano (01–12)                                    |
| `month`  | 10                     | Month of the year (01–12)                             |
| `dia`    | 20                     | Dia do mês (01–31)                                    |
| `day`    | 20                     | Day of the month (01–31)                              |
| `número` | 1                      | Número sequencial do trabalho no dia                  |
| `number` | 1                      | Sequential number of the work for the day             |
| `v`      | v1, v2, v3             | Versão do arquivo / Version of the file               |
```
## Exemplos / Examples
```
| Code                | Significado / Meaning                                      |
|---------------------|------------------------------------------------------------|
| `1tiapr-2510.201v1` | Trabalho Integrador, 20/10/2025, primeiro do dia, versão 1 |
| `1tiapr-2510.201v1` | Integrative work, 20/10/2025, first of the day, version 1  |
| `1tiapr-2510.201v2` | Mesma tarefa, versão revisada                              |
| `1tiapr-2510.201v2` | Same work, revised version                                 |
| `rel-2510.202v1`    | Relatório criado em 20/10/2025, segundo do dia             |
| `rel-2510.202v1`    | Report created on 20/10/2025, second of the day            |
| `nft-2511.051v1`    | Projeto NFT, 05/11/2025, primeiro do dia                   |
| `nft-2511.051v1`    | NFT project, 05/11/2025, first of the day                  |
| `py-2512.301v3`     | Script Python, 30/12/2025, versão 3                        |
| `py-2512.301v3`     | Python script, 30/12/2025, version 3                       |
```

## Organização de Pastas
```
/Trabalhos/
├── 2025/
│ ├── 2510/
│ │ ├── 1tiapr-2510.201v1.pdf
│ │ ├── 1tiapr-2510.201v2.pdf
│ │ ├── rel-2510.202v1.docx
│ │ └── nft-2510.203v1.png
│ ├── 2509/
│ │ └── proj-2509.151v2.zip
```

## Boas Práticas / Best Practices

- Incrementar somente a versão (v1 → v2 → v3) ao revisar o mesmo trabalho / Increment only the version (v1 → v2 → v3) when revising the same work.

- Criar novo número sequencial quando fizer um novo trabalho no mesmo dia / Create a new sequential number for a new work on the same day.

- Nunca apagar versões antigas — mantém o histórico completo / Never delete old versions — keeps a full history.

- Sufixos de status opcionais: -draft, -final, -rev / Optional status suffixes: -draft, -final, -rev

  `1tiapr-2510.201v3-final`

- Organize arquivos em pastas por ano/mês para fácil acesso / Organize files in year/month folders for easy access.

## Script Automático / Automatic Script

Um script Python foi criado para gerar os códigos automaticamente, detectando a próxima versão disponível e criando um arquivo .txt com metadados / A Python script was created to generate codes automatically, detecting the next available version and creating a .txt file with metadata.

## Link do Script / Script link:
[generate_version.py](https://github.com/m4ntonio/mao-versioning/blob/main/generate_version.py)

## Uso / Usage:
`python gerar_codigo.py`

## Entrada / Input:

`Digite o código do projeto: 1tiapr / Enter the project code: 1tiapr`  
`Número do trabalho no dia: 1 / Work number for the day: 1`

## Saída / Output:

`Código gerado: 1tiapr-2510.201v1` / `Generated code: 1tiapr-2510.201v1`  
`Código salvo em '1tiapr-2510.201v1.txt'` / `Code saved as '1tiapr-2510.201v1.txt'`

O script incrementa automaticamente a versão se já houver arquivos existentes na pasta /  
The script automatically increments the version if files already exist in the folder.

## Estilo & Organização / Style & Organization

- Utilize emojis para diferenciar tipos de trabalho / Use emojis to differentiate work types

- Mantenha histórico de todas as versões / Keep all version history

- Utilize cabeçalhos para referência rápida / Use headings for quick reference

- Organize pastas por ano/mês para facilitar busca / Organize folders by year/month for easier search

## Licença / License

MIT License – livre para uso pessoal ou acadêmico / free for personal or academic use.

## Contribuições / Contributions

Se você quiser melhorar o padrão ou o script, sinta-se à vontade para enviar pull requests ou abrir issues no repositório /
If you want to improve the standard or the script, feel free to submit pull requests or open issues in the repository.
