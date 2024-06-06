from faker import Faker
import pandas as pd
import random

fake_geral = Faker()
fake_cpf = Faker('pt_BR')


fake_cep = '85660000'
fake_cidade = 'Dois Vizinhos - PR'

bairros = [
    "Da Luz",
    "Das Torres",
    "Sagrada Família",
    "Santo Antônio",
    "Jardim da colina",
    "Jardim Marcante",
    "São Francisco de Assis",
    "Esperança",
    "Santa Luzia",
    "Centro Sul",
    "Centro",
    "Centro Norte",
    "São Francisco Xavier",
    "Alto da Colina",
    "São Judas Tadeu",
    "Vitória"
]

data = [(
    idx + 1,
    fake_geral.name(),
    fake_cpf.cpf(),
    fake_cpf.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y'),
    fake_cep,
    fake_cidade,
    fake_cpf.street_name(),
    fake_cpf.building_number(),
    random.choice(bairros)
    ) for idx in range(50)] # Se quiser gerar mais que 50, troca esse 50 xD


df = pd.DataFrame(data, columns=[
    'cliente_codigo',
    'cliente_nome',
    'cliente_cpf_cnpj',
    'cliente_data_nascimento',
    'cliente_end_cep',
    'cliente_end_cidade',
    'cliente_end_rua',
    'cliente_end_numero',
    'cliente_end_bairro'])


df.to_excel("nomes_cpfs_enderecos_registro.xlsx", index=False)