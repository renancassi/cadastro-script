from faker import Faker
import pandas as pd

fake_name = Faker()
fake_cpf = Faker('pt_BR')

data = [(fake_name.name(), fake_cpf.cpf()) for _ in range(50)]

for name, cpf in data[:10]:
    print(f"Nome: {name}, CPF: {cpf}")

df = pd.DataFrame(data, columns=['Nome Completo', 'CPF'])

df.to_excel("nomes_e_cpfs_cadastro.xlsx", index=False)
