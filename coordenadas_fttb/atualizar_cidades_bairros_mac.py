import pandas as pd
import random

# Definição dos bairros por cidade
bairros_beltrao = [
    "Bairro Água Branca", "Bairro Centro", "Bairro Sadia"
]



bairros_pato_branco = [
    "Alvorada", "Centro", "São João"
]

cidades = ["Dois Vizinhos", "Francisco Beltrão", "Pato Branco"]

# Função para atribuir bairros aleatoriamente
def atribuir_bairro(cidade):
    if cidade == "Francisco Beltrão":
        return random.choice(bairros_beltrao)
    elif cidade == "Pato Branco":
        return random.choice(bairros_pato_branco)
    return None

# Ler os arquivos CSV
clientes_df = pd.read_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_fttb/ftth_pb_fb.csv')
# (Falta cadastrar FTTB beltrão/pato) torres_df = pd.read_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_radio/torres_radio_iface.csv')


for idx, row in clientes_df.iterrows():
    nova_cidade = random.choice(cidades)
    novo_bairro = atribuir_bairro(nova_cidade)
    clientes_df.at[idx, 'Cidade'] = nova_cidade
    clientes_df.at[idx, 'bairro'] = novo_bairro


clientes_grouped = clientes_df.groupby('bairro')
torres_grouped = torres_df.groupby('bairro')


def atribuir_mac(cliente_row):
    bairro = cliente_row['bairro']
    if bairro in torres_grouped.groups:
        macs_no_bairro = torres_grouped.get_group(bairro)['mac'].tolist()
        if macs_no_bairro:
            mac_escolhido = random.choice(macs_no_bairro)
            return mac_escolhido
    return cliente_row['mac']

# Aplicar a função para atribuir MACs aos clientes
clientes_df['mac'] = clientes_df.apply(atribuir_mac, axis=1)

# Salvar o resultado em um novo arquivo CSV
clientes_df.to_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_fttb/mac_bairro_FTTB_atualizado.csv', index=False)

print("MACs e bairros atribuídos aleatoriamente aos clientes e salvos em './mac_bairro_atualizado.csv'.")
