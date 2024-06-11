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
from randomizar_datas import *

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

valores_plano = {
    "plano_100mb": {
        "adesao": '300',
        "rescisao": '400',
        "mensalidade": '150'
    },
    "plano_150mb": {
        "adesao": '349.90',
        "rescisao": '500',
        "mensalidade": '200'
    },
    "plano_300mb": {
        "adesao": '189.90',
        "rescisao": '700',
        "mensalidade": '299.90'
    }
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
        carteira = random.choice(contrato_carteira)
        data_cadastro = randomizar_datas_cadastro()
        data_adesao = randomizar_datas_adesao(data_cadastro)
        data_ativacao = randomizar_datas_ativacao(data_adesao)

        valor_adesao = valores_plano[plano]["adesao"]
        valor_rescisao = valores_plano[plano]["rescisao"]
        valor_mensalidade = valores_plano[plano]["mensalidade"]


        if random.random() < 0.05:
            data_rescisao = randomizar_datas_rescisao(data_adesao)
            data_rescisao_formatado = data_rescisao.strftime('%d/%m/%Y')
        else:
            data_rescisao_formatado = ''

        if random.random() < 0.10:
            contrato_nfe2x_tipo_lancamento = random.choice(contratos_nfe2x_tipos)
            contrato_faturavel = 'n'
            contrato_tipo_faturamento = 'manual'
            if data_rescisao_formatado == '':
                contrato_fidelidade = random.randint(0,18)
            else:
                contrato_fidelidade = ''
        else:
            contrato_nfe2x_tipo_lancamento = 'auto'
            contrato_faturavel = 's'
            contrato_tipo_faturamento = 'auto'
            contrato_fidelidade = ''

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
            data_cadastro.strftime('%d/%m/%Y'),
            data_adesao.strftime('%d/%m/%Y'),
            data_rescisao_formatado,
            contrato_fidelidade,
            valor_adesao,
            valor_rescisao,
            valor_mensalidade,
            contrato_faturavel,
            contrato_tipo_faturamento,
            contrato_nfe2x_tipo_lancamento,
            parceiro,
            carteira,
            contrato_observacao,
            plano,
            vencimento,
            data_ativacao.strftime('%d/%m/%Y'),
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
    'cliente_data_cadastro',
    'cliente_data_adesao',
    'cliente_data_recisao',
    'contrato_fidelidade',
    'contrato_valor_adesao',
    'contrato_valor_rescisão',
    'contrato_valor_mensal',
    'contrato_faturavel',
    'contrato_tipo_faturamento',
    'contrato_nfe2x_tipo_lancamento',
    'cliente_parceiro',
    'contrato_carteira',
    'contrato_observacoes',
    'ponto_plano',
    'contrato_dia_vencimento',
    'ponto_data_ativacao',
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
df['ponto_nome'] = df['cliente_end_complemento']

probabilidade_contrato_endereco = 0.2
probabilidade_ponto_endereco_igual = 0.7

def preencher_endereco(row):
    if random.random() < probabilidade_contrato_endereco:
        row['contrato_end_cidade'] = row['cliente_end_cidade']
        row['contrato_end_cep'] = row['cliente_end_cep']
        row['contrato_end_rua'] = row['cliente_end_rua']
        row['contrato_end_numero'] = row['cliente_end_numero']
        row['contrato_end_bairro'] = row['cliente_end_bairro']
        row['contrato_end_complemento'] = row['cliente_end_complemento']
        row['contrato_end_latitude'] = row['cliente_end_latitude']
        row['contrato_end_longitude'] = row['cliente_end_longitude']
    else:
        row['contrato_end_cidade'] = None
        row['contrato_end_cep'] = None
        row['contrato_end_rua'] = None
        row['contrato_end_numero'] = None
        row['contrato_end_bairro'] = None
        row['contrato_end_complemento'] = None
        row['contrato_end_latitude'] = None
        row['contrato_end_longitude'] = None

    if random.random() < probabilidade_ponto_endereco_igual:
        row['ponto_end_cidade'] = row['cliente_end_cidade']
        row['ponto_end_cep'] = row['cliente_end_cep']
        row['ponto_end_rua'] = row['cliente_end_rua']
        row['ponto_end_numero'] = row['cliente_end_numero']
        row['ponto_end_bairro'] = row['cliente_end_bairro']
        row['ponto_end_complemento'] = row['cliente_end_complemento']
        row['ponto_end_latitude'] = row['cliente_end_latitude']
        row['ponto_end_longitude'] = row['cliente_end_longitude']
    else:
        row['ponto_end_cidade'] = random.choice(cidades)
        row['ponto_end_cep'] = cidade_ceps[cidade]
        row['ponto_end_rua'] = fake_cpf.street_name()
        row['ponto_end_numero'] = fake_cpf.building_number()
        row['ponto_end_bairro'] = random.choice(bairro)
        row['ponto_end_complemento'] = random.choice(complementos)
        row['ponto_end_latitude'], row['ponto_end_longitude'] = get_random_coordinates(row['ponto_end_cidade'])
    return row

df = df.apply(preencher_endereco, axis=1)


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
    'cliente_end_latitude',
    'cliente_end_longitude',
    'cliente_telefones',
    'ponto_emails',
    'cliente_data_cadastro',
    'cliente_parceiro',
    'contrato_carteira',
    'cliente_data_adesao',
    'cliente_data_recisao',
    'contrato_fidelidade',
    'contrato_valor_adesao',
    'contrato_valor_rescisão',
    'contrato_valor_mensal',
    'contrato_dia_vencimento',
    'contrato_observacoes',
    'contrato_faturavel',
    'contrato_tipo_faturamento',
    'contrato_nfe2x_tipo_lancamento',
    'contrato_end_cidade',
    'contrato_end_cep',
    'contrato_end_rua',
    'contrato_end_numero',
    'contrato_end_bairro',
    'contrato_end_complemento',
    'contrato_end_latitude',
    'contrato_end_longitude',
    'ponto_plano',
    'ponto_nome',
    'ponto_ppp_usuario',
    'ponto_end_cidade',
    'ponto_end_cep',
    'ponto_end_rua',
    'ponto_end_numero',
    'ponto_end_bairro',
    'ponto_end_complemento',
    'ponto_end_latitude',
    'ponto_end_longitude',
    'ponto_data_ativacao',
    'ponto_mac',
    'ponto_tecnologia',
    'ponto_serial'
]




df = df[colunas_ordenadas]
df.to_excel("clientes.xlsx", index=False)
print("------------------------------")
print("Arquivo gerado" + ' ./clientes.xlsx')
print("------------------------------")