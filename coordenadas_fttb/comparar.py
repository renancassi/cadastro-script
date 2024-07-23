import pandas as pd

def compare_csv_columns(file1, file2):
    # Ler os arquivos CSV
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Garantir que os arquivos têm as mesmas colunas
    if df1.columns.tolist() != df2.columns.tolist():
        raise ValueError("Os arquivos CSV têm colunas diferentes")
    
    # Identificar as diferenças
    different_columns = []
    for column in df1.columns:
        if not df1[column].equals(df2[column]):
            different_columns.append(column)
    
    # Imprimir as colunas com diferenças, uma por linha
    if different_columns:
        print("Colunas com Atualizadas:")
        for col in different_columns:
            print(col)
    else:
        print("Nenhuma diferença encontrada nas colunas.")

# Exemplo de uso
compare_csv_columns('./coordenadas_fttb/clientes_doisVizinhos.csv', './coordenadas_fttb/ClientesDv.csv')
