import pandas as pd

# Carregar o arquivo CSV
arquivo = './clientes/clientes_coordenadas_alteradas_cidades.csv'
df = pd.read_csv(arquivo)

# Verificar as linhas onde os endereços coincidem
filtro = (
    (df['ponto_end_rua'] == df['cliente_end_rua']) &
    (df['ponto_end_numero'] == df['cliente_end_numero']) &
    (df['ponto_end_bairro'] == df['cliente_end_bairro'])
)

print("Linhas que serão alteradas:")
print(df[filtro])

# Atualizar as coordenadas do cliente com as coordenadas do ponto
df.loc[filtro, 'cliente_end_latitude'] = df.loc[filtro, 'ponto_end_latitude']
df.loc[filtro, 'cliente_end_longitude'] = df.loc[filtro, 'ponto_end_longitude']

# Verificar as alterações
print("\nLinhas após a alteração:")
print(df[filtro])

# Salvar as alterações em um novo arquivo CSV
novo_arquivo = './clientes/clientes_coordenadas_atualizadas.csv'
df.to_csv(novo_arquivo, index=False)
