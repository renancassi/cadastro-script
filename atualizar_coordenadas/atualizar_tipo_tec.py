import pandas as pd
import random
import string

# Função para gerar ponto_serial
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

# Carregar o arquivo CSV
arquivo = 'clientes\clientes_coordenadas_alteradas.csv'
df = pd.read_csv(arquivo)

# Verificar as linhas que serão alteradas
filtro = df['ponto_end_cidade'].isin(['Dois Vizinhos', 'Pato Branco'])
print("Linhas que serão alteradas:")
print(df[filtro])

# Alterar o ponto_tecnologia para FTTH e gerar um novo ponto_serial
df.loc[filtro, 'ponto_tecnologia'] = 'FTTH'
df.loc[filtro, 'ponto_serial'] = df.loc[filtro, 'ponto_serial'].apply(lambda x: gerador_serial())

# Verificar as alterações
print("\nLinhas após a alteração:")
print(df[filtro])

# Salvar as alterações em um novo arquivo CSV
novo_arquivo = './clientes/clientes_coordenadas_alteradas_cidades.csv'
df.to_csv(novo_arquivo, index=False)
