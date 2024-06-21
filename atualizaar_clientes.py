import pandas as pd


# Carregar os dados do CSV
csv_file = 'clientes/clientes_import.csv'
client_data = pd.read_csv(csv_file)


tipo_tecnologia = client_data[['ponto_tecnologia']].values.tolist()

print(tipo_tecnologia)

# Salvar o DataFrame atualizado em um novo arquivo CSV
#client_data.to_csv('clientes/clientes_tecnologia_atualizados.csv', index=False)

