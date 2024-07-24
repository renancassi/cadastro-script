import pandas as pd
import random

# Definição dos bairros por cidade
bairros_beltrao = [
    "Bairro Água Branca", "Bairro Cango", "Bairro Centro", "Bairro Industrial", "Bairro Jardim Seminário",
    "Bairro Júpter", "Bairro Luther King", "Bairro Miniguaçu", "Bairro Novo Mundo", "Bairro Pinheirão",
    "Bairro Sadia", "Bairro São Francisco", "Bairro Vila Nova", "Comunidade Divisor", "Comunidade Km 23",
    "Comunidade Linha Eva e Linha Macagnan", "Comunidade Linha Hobold", "Comunidade Linha São Paula",
    "Comunidade Linha Volpato", "Comunidade Rio do Mato", "Comunidade Rio Guarapuava", "Comunidade Rio Tuna",
    "Comunidade São Francisco de Assis", "Comunidade São Pio X – Km 20", "Comunidade Secção Progresso",
    "Comunidade Vila Lobos", "Comunidade Volta Grande", "Bairro Alvorada", "Bairro Cantelmo", "Bairro Cristo Rei",
    "Bairro Jardim Floresta e Italia", "Bairro Jardim Virgínia", "Bairro Kennedy", "Bairro Marrecas",
    "Bairro Nossa Senhora Aparecida", "Bairro Padre Ulrico", "Bairro Pinheirinho", "Bairro São Cristovão",
    "Bairro São Miguel", "Comunidade Assentamento Missões", "Comunidade Jacutinga", "Comunidade Lageado Grande",
    "Comunidade Linha Formiga", "Comunidade Linha Santa Rosa – Km 08", "Comunidade Linha Triton",
    "Comunidade Nova Concórdia", "Comunidade Rio Erval – Km 15", "Comunidade Rio Pedreirinho",
    "Comunidade Santa Bárbara", "Comunidade São João", "Comunidade Secção Jacaré", "Comunidade Secção São Miguel",
    "Comunidade Vila Rural Gralha Azul"
]

bairros_dois_vizinhos = [
    "Da Luz", "Das Torres", "Sagrada Família", "Santo Antônio", "Jardim da Colina", "Jardim Marcante",
    "São Francisco de Assis", "Esperança", "Santa Luzia", "Centro Sul", "Centro", "Centro Norte",
    "São Francisco Xavier", "Alto da Colina", "São Judas Tadeu", "Vitória"
]

bairros_pato_branco = [
    "Aeroporto", "Alto da Glória", "Alvorada", "Amadori", "Anchieta", "Baixada", "Bancários", "Bela Vista",
    "Bonatto", "Bortot", "Brasília", "Cadorin", "Centro", "Cristo Rei", "Dall Ross", "Fraron", "Gralha Azul",
    "Industrial", "Jardim Floresta", "Jardim Primavera", "Jardim das Américas", "La Salle", "Menino Deus",
    "Morumbi", "Novo Horizonte", "Pagnoncelli", "Parque do Som", "Parzianello", "Pinheirinho", "Pinheiros",
    "Planalto", "Sambugaro", "Santa Terezinha", "Santo Antônio", "São Cristóvão", "São Francisco", "São João",
    "São Luiz", "São Roque", "São Vicente", "Sudoeste", "Trevo da Guarany", "Veneza", "Vila Esperança",
    "Vila Isabel"
]

cidades = ["Dois Vizinhos", "Francisco Beltrão", "Pato Branco"]

# Função para atribuir bairros aleatoriamente
def atribuir_bairro(cidade):
    if cidade == "Dois Vizinhos":
        return random.choice(bairros_dois_vizinhos)
    elif cidade == "Francisco Beltrão":
        return random.choice(bairros_beltrao)
    elif cidade == "Pato Branco":
        return random.choice(bairros_pato_branco)
    return None

# Ler os arquivos CSV
clientes_df = pd.read_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_radio/clientes_pontos_radios.csv')
torres_df = pd.read_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_radio/torres_radio_iface.csv')

# Atualizar cidade e bairro de alguns clientes aleatoriamente
for idx, row in clientes_df.iterrows():
    if row['Cidade'] != "Francisco Beltrão" or row['bairro'] not in bairros_beltrao:
        if random.random() < 1:
            nova_cidade = random.choice(cidades)
            if nova_cidade != row['Cidade']:
                clientes_df.at[idx, 'Cidade'] = nova_cidade
                clientes_df.at[idx, 'bairro'] = atribuir_bairro(nova_cidade)

# Agrupar clientes e MACs por cidade
clientes_grouped = clientes_df.groupby('Cidade')
torres_grouped = torres_df.groupby('Cidade')

# Função para atribuir MACs aleatoriamente
def atribuir_mac(cliente_row):
    cidade = cliente_row['Cidade']
    if cidade in torres_grouped.groups:
        macs_na_cidade = torres_grouped.get_group(cidade)['mac'].tolist()
        if macs_na_cidade:
            mac_escolhido = random.choice(macs_na_cidade)
            return mac_escolhido
    return cliente_row['mac']

# Aplicar a função para atribuir MACs aos clientes
clientes_df['mac'] = clientes_df.apply(atribuir_mac, axis=1)

# Salvar o resultado em um novo arquivo CSV
clientes_df.to_csv('C:/Users/Marketing/Documents/vscode/script/cadastro-script/coordenadas_radio/cidade_teste.csv', index=False)

print("MACs e bairros atribuídos aleatoriamente aos clientes e salvos em 'cidade_teste.csv'.")
