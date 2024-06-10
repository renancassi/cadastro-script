### IMPORTANTE 
### IMPORTANTE 
### IMPORTANTE 
### IMPORTANTE 
### pip install faker
### pip install pandas openpyxl 
### pip install shapely
### pip install geopandas  
### pip install tqdm
### pip install fordev
### IMPORTANTE 
### IMPORTANTE 
### IMPORTANTE 
### IMPORTANTE 
from listas import *
from randomizar_coordenadas import *
from gerador_serial import gerador_serial


from tqdm import tqdm
from faker import Faker
from fordev import *
import pandas as pd
import random
import re
import os

fake_geral = Faker()
fake_cpf = Faker('pt_BR')

# Mapeamento das cidades para seus respectivos bairros e CEPs
cidade_bairros = {
    "Dois Vizinhos": bairros_doisVizinhos,
    "Francisco Beltrão": bairros_beltrão,
    "Pato Branco": bairros_patoBranco
}

cidade_ceps = {
    "Dois Vizinhos": "85660000",
    "Francisco Beltrão": "85601000",
    "Pato Branco": "85501000"
}



planos = {
    "Dois Vizinhos":"plano_100mb",
    "Francisco Beltrão": "plano_150mb",
    "Pato Branco":"plano_300mb"
}


def clean_name(name):
    return re.sub(r'^(Mr\.|Mrs\.|Ms\.|Miss|Dr\.)\s+', '', name)#Tira titulos gerados pelo faker (Senhor, senhora, doutor, etc..)

print(ascii_art)
#Remover arquivo clientes.xlsx caso existente
caminho_arquivo = 'clientes.xlsx'
print("------------------------------")
print("Procurando arquivo existente")
if os.path.exists(caminho_arquivo):
    os.remove(caminho_arquivo)
    print("------------------------------")
    print("O arquivo antigo foi removido!")
    print("------------------------------")
else:
    print("------------------------------")
    print("O arquivo não existe!")
    print("------------------------------")
    

while True:
    try:
        total_registros = int(input("Insira o número total de registros: "))
        break
    except ValueError:
        print("insira apenas números inteiros.")

data = []

with tqdm(total=total_registros, desc="Gerando dados", unit="registro") as pbar:
    for idx in range(total_registros): 
        cidade = random.choice(cidades)
        bairro = random.choice(cidade_bairros[cidade])
        cep = cidade_ceps[cidade]
        complemento = random.choice(complementos)
        plano = planos[cidade]
        vencimento = random.randint(5, 25)
        coordenadaY, coordenadaX = get_random_coordinates(cidade)
        nome_completo = clean_name(fake_geral.name())
        
        if random.random() < 0.40:
            contrato_observacao = random.choice(contrato_observacoes)
        else:
            contrato_observacao = ''

        if random.random() < 0.70:
            tipo_tecnologia = 'FTTH'
            fake_serial = gerador_serial()
        else:
            tipo_tecnologia = 'RADIO'
            fake_serial = ''

        # Definindo se o registro terá IE no lugar de RG (5% de chance)
        if random.random() < 0.05:
            rg_ie = generators.state_registration(uf_code='PR')
            cpf_cnpj = fake_cpf.cnpj()
            complemento = "Loja"
            tipo_pessoa = "PJ"
            tipo_tecnologia = 'FTTH'
            fake_serial = gerador_serial()
            if random.random() < 0.10:
                parceiro = 's'
            else:
                parceiro = 'n'
        else:
            rg_ie = fake_cpf.rg()
            cpf_cnpj = fake_cpf.cpf()
            tipo_pessoa = "PF"
            parceiro = 'n'
        
        # Valida se RG contém "X" no final, caso positivo, gera um novo RG
        while rg_ie[-1].upper() == 'X':
            rg_ie = fake_cpf.rg()
        
        data.append((
            idx + 1,
            nome_completo,
            rg_ie,
            cpf_cnpj,
            tipo_pessoa,
            fake_cpf.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y'),
            cep,
            cidade,
            fake_cpf.street_name(),
            fake_cpf.building_number(),
            bairro,
            complemento,
            fake_cpf.msisdn(),
            parceiro,
            contrato_observacao,
            plano,
            vencimento,
            fake_cpf.mac_address(),
            coordenadaY,
            coordenadaX,
            tipo_tecnologia,
            fake_serial
        ))
        pbar.update(1)

df = pd.DataFrame(data, columns=[
    'cliente_codigo',
    'cliente_nome',
    'cliente_rg_ie',
    'cliente_cpf_cnpj',
    'cliente_tipo_pessoa',
    'cliente_data_nascimento',
    'cliente_end_cep',
    'cliente_end_cidade',
    'cliente_end_rua',
    'cliente_end_numero',
    'cliente_end_bairro',
    'cliente_end_complemento',
    'cliente_telefones',
    'cliente_parceiro',
    'contrato_observacoes',
    'ponto_plano',
    'vencimento',
    'ponto_mac',
    'cliente_end_latitude',
    'cliente_end_longitude',
    'ponto_tecnologia',
    'ponto_serial'
])

# Gera coluna "cliente_apelido" com base na primeira coluna (cliente_nome)

df['cliente_apelido'] = df['cliente_nome'].apply(lambda name: name.split()[0])
#Gera coluna "ponto_emails" com base na primeira coluna (cliente_nome)
df['ponto_emails'] = df['cliente_nome'].apply(lambda name: f"{name.replace(' ', '.').lower()}@mailinator.com") 
df['ponto_ppp_usuario'] = df['cliente_nome'].apply(lambda name: f"{name.replace(' ', '.').lower()}@meuprovedor.com.br")


# Reordena as colunas
colunas_ordenadas = [
    'cliente_codigo',
    'cliente_nome',
    'cliente_apelido',
    'cliente_rg_ie',
    'cliente_cpf_cnpj',
    'cliente_tipo_pessoa',
    'cliente_data_nascimento',
    'cliente_end_cidade',
    'cliente_end_cep',
    'cliente_end_rua',
    'cliente_end_numero',
    'cliente_end_bairro',
    'cliente_end_complemento',
    'cliente_telefones',
    'ponto_emails',
    'cliente_parceiro',
    'contrato_observacoes',
    'ponto_plano',
    'vencimento',
    'cliente_end_latitude',
    'cliente_end_longitude',
    'ponto_ppp_usuario',
    'ponto_mac',
    'ponto_tecnologia',
    'ponto_serial'
]




df = df[colunas_ordenadas]
df.to_excel("clientes.xlsx", index=False)
print("------------------------------")
print("Arquivo gerado" + ' ./clientes.xlsx')
print("------------------------------")