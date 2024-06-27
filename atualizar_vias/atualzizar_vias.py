import pandas as pd

# Carregar os arquivos CSV
clientes_arquivo = 'atualizar_vias/clientes_coordenadas_finalizado.csv'
splitter_arquivo = 'atualizar_vias/spliter_cto.csv'

clientes_df = pd.read_csv(clientes_arquivo)
splitter_df = pd.read_csv(splitter_arquivo)

# Criar uma cópia do DataFrame de clientes para não alterar o original
clientes_df_copy = clientes_df.copy()

# Criar uma nova coluna "Vias" na cópia do DataFrame de clientes
clientes_df_copy['id_vias'] = None

# Conjunto para rastrear id_via usados
id_vias_usados = set()

# Atribuir id_via do arquivo spliter_cto ao arquivo clientes_coordenadas
for index, cliente in clientes_df_copy.iterrows():
    cto_matches = splitter_df[
        (splitter_df['cto_cidade'] == cliente['ponto_end_cidade']) &
        (splitter_df['cto_bairro'] == cliente['ponto_end_bairro'])
    ]
    
    for _, cto in cto_matches.iterrows():
        if cto['id_via'] not in id_vias_usados:
            clientes_df_copy.at[index, 'Vias'] = cto['id_via']
            id_vias_usados.add(cto['id_via'])
            break

# Verificar as alterações
print(clientes_df_copy.head())

# Salvar as alterações em um novo arquivo CSV
novo_arquivo = './clientes_vias.csv'
clientes_df_copy.to_csv(novo_arquivo, index=False)
