### IMPORTANTE 
### IMPORTANTE 
### IMPORTANTE 
### IMPORTANTE 
### pip install faker
### pip install pandas openpyxl 
### IMPORTANTE 
### IMPORTANTE 
### IMPORTANTE 
### IMPORTANTE 
from print_ascii import *
from faker import Faker
import pandas as pd
import random
import re
import os

fake_geral = Faker()
fake_cpf = Faker('pt_BR')
fake_phone = '46999999999'


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


data = []


for idx in range(1000): # Se quiser gerar mais que 50 cadastros, troca esse valor ai xD

    def clean_name(name):
        return re.sub(r'^(Mr\.|Mrs\.|Ms\.|Miss|Dr\.)\s+', '', name)#Tira titulos gerados pelo faker (Senhor, senhora, doutor, etc..)
    
    cidade = random.choice(cidades)
    bairro = random.choice(cidade_bairros[cidade])
    cep = cidade_ceps[cidade]
    complemento = random.choice(complementos)
    plano = planos[cidade]
    vencimento = random.randint(5,25)

    data.append((
        idx + 1,
        fake_geral.name(),
        fake_cpf.cpf(),
        fake_cpf.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y'),
        cep,
        cidade,
        fake_cpf.street_name(),
        fake_cpf.building_number(),
        bairro,
        complemento,
        fake_phone,
        plano,
        vencimento,
        fake_cpf.mac_address()
    ))

df = pd.DataFrame(data, columns=[
    'cliente_codigo',
    'cliente_nome',
    'cliente_cpf_cnpj',
    'cliente_data_nascimento',
    'cliente_end_cep',
    'cliente_end_cidade',
    'cliente_end_rua',
    'cliente_end_numero',
    'cliente_end_bairro',
    'cliente_end_complemento',
    'cliente_telefones',
    'ponto_plano',
    'vencimento',
    'ponto_mac'
])

#Gera coluna "ponto_emails" com base na primeira coluna (cliente_nome)
df['ponto_emails'] = df['cliente_nome'].apply(lambda name: f"{name.replace(' ', '.').lower()}@mailinator.com") 


# Reordena as colunas
colunas_ordenadas = [
    'cliente_codigo',
    'cliente_nome',
    'cliente_cpf_cnpj',
    'cliente_data_nascimento',
    'cliente_end_cidade',
    'cliente_end_cep',
    'cliente_end_rua',
    'cliente_end_numero',
    'cliente_end_bairro',
    'cliente_end_complemento',
    'cliente_telefones',
    'ponto_emails',
    'ponto_plano',
    'vencimento',
    'ponto_mac'
]

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


df = df[colunas_ordenadas]
df.to_excel("clientes.xlsx", index=False)
print("Arquivo gerado")
print("------------------------------")