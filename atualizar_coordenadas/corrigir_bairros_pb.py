import pandas as pd
import random

# Lista de bairros válidos em Pato Branco
bairros_patoBranco = [
    "Aeroporto", "Alto da Glória", "Alvorada", "Amadori", "Anchieta", "Baixada",
    "Bancários", "Bela Vista", "Bonatto", "Bortot", "Brasília", "Cadorin", "Centro",
    "Cristo Rei", "Dall Ross", "Fraron", "Gralha Azul", "Industrial", "Jardim Floresta",
    "Jardim Primavera", "Jardim das Américas", "La Salle", "Menino Deus", "Morumbi",
    "Novo Horizonte", "Pagnoncelli", "Parque do Som", "Parzianello", "Pinheirinho",
    "Pinheiros", "Planalto", "Sambugaro", "Santa Terezinha", "Santo Antônio",
    "São Cristóvão", "São Francisco", "São João", "São Luiz", "São Roque", "São Vicente",
    "Sudoeste", "Trevo da Guarany", "Veneza", "Vila Esperança", "Vila Isabel"
]

# Carregar o arquivo CSV
arquivo = './clientes/clientes_coordenadas_atualizadas.csv'
df = pd.read_csv(arquivo)

# Verificar as linhas onde a cidade é Pato Branco e o bairro não está na lista de bairros válidos
filtro = (df['ponto_end_cidade'] == 'Pato Branco') & (~df['ponto_end_bairro'].isin(bairros_patoBranco))
print("Linhas que serão alteradas:")
print(df[filtro])

# Atualizar o ponto_end_bairro com um bairro aleatório da lista de bairros válidos
df.loc[filtro, 'ponto_end_bairro'] = df.loc[filtro, 'ponto_end_bairro'].apply(lambda x: random.choice(bairros_patoBranco))

# Verificar as alterações
print("\nLinhas após a alteração:")
print(df[filtro])

# Salvar as alterações em um novo arquivo CSV
novo_arquivo = './clientes/clientes_coordenadas_bairros_atualizados.csv'
df.to_csv(novo_arquivo, index=False)
