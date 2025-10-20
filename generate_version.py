import os
from datetime import datetime

AUTOR = "MAO"

# Função que converte número para texto (1 → "Versão inicial", 2 → "Segunda versão", etc.)
def status_por_versao(v):
    status_map = {
        1: "Versão inicial",
        2: "Segunda versão",
        3: "Terceira versão",
        4: "Quarta versão",
        5: "Quinta versão",
        6: "Sexta versão",
        7: "Sétima versão",
        8: "Oitava versão",
        9: "Nona versão",
        10: "Décima versão",
    }
    return status_map.get(v, f"Versão {v}")

def gerar_codigo(codigo_projeto, numero_trabalho):
    hoje = datetime.now()
    ano = str(hoje.year)[2:]
    mes = f"{hoje.month:02d}"
    dia = f"{hoje.day:02d}"

    base_nome = f"{codigo_projeto}-{ano}{mes}.{dia}{numero_trabalho}"
    versao = 1

    # Verifica versões anteriores
    arquivos_existentes = [f for f in os.listdir() if f.startswith(base_nome)]
    if arquivos_existentes:
        versoes = []
        for arq in arquivos_existentes:
            if "v" in arq:
                try:
                    v = int(arq.split("v")[-1].split(".")[0])
                    versoes.append(v)
                except:
                    pass
        if versoes:
            versao = max(versoes) + 1

    return f"{base_nome}v{versao}", versao

def criar_txt(nome_codigo, versao, descricao):
    data = datetime.now().strftime("%d/%m/%Y")
    status = status_por_versao(versao)

    conteudo = f"""{nome_codigo}
Data: {data}
Status: {status}
Descrição: {descricao}
Autor: {AUTOR}
"""

    with open(f"{nome_codigo}.txt", "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"✅ Arquivo '{nome_codigo}.txt' criado com sucesso!")

if __name__ == "__main__":
    print("=== MAO Versioning Standardo ===")
    codigo = input("Digite o nome do projeto (ex: 1tiapr, rel, nft): ").strip()
    numero = input("Número do trabalho no dia (ex: 1): ").strip()
    descricao = input("Digite uma breve descrição: ").strip() or "---"

    codigo_gerado, versao = gerar_codigo(codigo, numero)
    print(f"\n🆔 Código gerado: {codigo_gerado}")
    criar_txt(codigo_gerado, versao, descricao)
