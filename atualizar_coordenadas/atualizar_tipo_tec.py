import pandas as pd
import random
import string

# Carregar o arquivo CSV
arquivo = './clientes/clientes_coordenadas_finalizado.csv'
df = pd.read_csv(arquivo)

# Lista de bairros para alterar ponto_tecnologia para 'RADIO'
bairros_radio = [
    "Comunidade Linha Santa Rosa - Km 08",
    "Comunidade São João",
    "Comunidade Santa Bárbara",
    "Comunidade Linha Formiga",
    "Comunidade Rio do Mato",
    "Comunidade Rio Erval – Km 15",
    "Bairro Água Branca",
    "Comunidade Rio Guarapuava",
    "Comunidade Linha Volpato",
    "Comunidade Rio Pedreirinho",
    "Comunidade Vila Rural Gralha Azul",
    "Comunidade Secção Progresso",
    "Comunidade Vila Lobos",
    "Comunidade Linha Triton",
    "Comunidade Lageado Grande",
    "Comunidade Jacutinga",
    "Comunidade Assentamento Missões",
    "Comunidade Divisor",
    "Comunidade São Francisco de Assis",
    "Comunidade Secção São Miguel",
    "Comunidade São Pio X – Km 20",
    "Comunidade Secção Jacaré"
]

# Função para gerar um novo serial
def gerador_serial():
    serial = "FTTH"
    for _ in range(3):
        serial += random.choice(string.digits)
    serial += random.choice(string.ascii_uppercase)
    for _ in range(2):
        serial += random.choice(string.digits)
    serial += random.choice(string.ascii_uppercase)
    serial += random.choice(string.digits)
    return serial

# Filtro para bairros que precisam ser alterados para 'RADIO' na cidade de Francisco Beltrão
filtro_radio = (df['ponto_end_bairro'].isin(bairros_radio)) & (df['ponto_end_cidade'] == 'Francisco Beltrão')
print("Linhas que serão alteradas para 'RADIO':")
print(df[filtro_radio])

# Alterar para 'RADIO'
df.loc[filtro_radio, 'ponto_tecnologia'] = 'RADIO'

# Limpar ponto_serial onde ponto_tecnologia é 'RADIO'
df.loc[df['ponto_tecnologia'] == 'RADIO', 'ponto_serial'] = ''

# Filtro para bairros que não estão na lista e precisam ser alterados para 'FTTH' na cidade de Francisco Beltrão
filtro_ftth = (~df['ponto_end_bairro'].isin(bairros_radio)) & (df['ponto_end_cidade'] == 'Francisco Beltrão')
print("\nLinhas que serão alteradas para 'FTTH':")
print(df[filtro_ftth])

# Alterar para 'FTTH'
df.loc[filtro_ftth, 'ponto_tecnologia'] = 'FTTH'

# Gerar novos seriais para 'FTTH' onde ponto_serial está vazio
filtro_ftth_serial_vazio = (df['ponto_tecnologia'] == 'FTTH') & (df['ponto_serial'].isna() | (df['ponto_serial'] == ''))
df.loc[filtro_ftth_serial_vazio, 'ponto_serial'] = df.loc[filtro_ftth_serial_vazio, 'ponto_serial'].apply(lambda x: gerador_serial())

print("\nLinhas após as alterações:")
print(df)

# Salvar o arquivo CSV atualizado
novo_arquivo = './clientes/clientes_coordenadas_alteradas_cidades.csv'
df.to_csv(novo_arquivo, index=False)
