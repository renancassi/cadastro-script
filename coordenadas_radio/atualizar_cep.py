import pandas as pd


cidade_ceps = {
    "Dois Vizinhos": "85660000",
    "Francisco Beltrão": "85601000",
    "Pato Branco": "85501000"
}

clientes_df = pd.read_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_radio/mac_bairro_atualizado.csv')

def atribuir_cep(cidade):
    return cidade_ceps.get(cidade, "")

clientes_df['cep'] = clientes_df['Cidade'].apply(atribuir_cep)

clientes_df.to_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_radio/pronto/cliente_cep.csv', index=False)

print("CEPs atualizados com base na cidade e salvos em 'clientes_cep.csv'.")