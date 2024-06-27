import pandas as pd

# Carregar o arquivo CSV
arquivo = './clientes/clientes_coordenadas.csv'
df = pd.read_csv(arquivo)

# Lista de bairros para alterar ponto_tecnologia
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


filtro = (df['ponto_end_bairro'].isin(bairros_radio)) & (df['ponto_end_cidade'] == 'Francisco Beltrão')
print("Linhas que serão alteradas:")
print(df[filtro])


df.loc[filtro, 'ponto_tecnologia'] = 'RADIO'


print("\nLinhas após a alteração:")
print(df[filtro])

df.loc[df['ponto_tecnologia'] == 'RADIO', 'ponto_serial'] = ''


print("\nLinhas com ponto_tecnologia = 'RADIO' após limpar ponto_serial:")
print(df[df['ponto_tecnologia'] == 'RADIO'])


novo_arquivo = './clientes/clientes_coordenadas_alteradas.csv'
df.to_csv(novo_arquivo, index=False)
