from faker import Faker
import pandas as pd

fake_geral = Faker()
fake_cpf = Faker('pt_BR')


fake_cep = '85660000'
fake_cidade = 'Dois Vizinhos - PR'



data = [(
    idx + 1,
    fake_geral.name(),
    fake_cpf.cpf(),
    fake_cpf.date_of_birth(minimum_age=18, maximum_age=70).strftime('%d/%m/%Y'),
    fake_cep,
    fake_cidade,
    fake_cpf.street_name(),
    fake_cpf.building_number())
    for idx in range(50)]


df = pd.DataFrame(data, columns=[
    'cliente_codigo',
    'cliente_nome',
    'cliente_cpf_cnpj',
    'cliente_data_nascimento',
    'cliente_end_cep',
    'cliente_end_cidade',
    'cliente_end_rua',
    'cliente_end_numero'])


df.to_excel("nomes_cpfs_enderecos_registro.xlsx", index=False)