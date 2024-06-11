import random
from datetime import datetime, timedelta

def randomizar_datas_cadastro():
    dia = random.randint(1, 25)
    mes = random.randint(1, 6)
    ano = 2023
    data_cadastro = datetime(ano, mes, dia)
    return data_cadastro

def randomizar_datas_adesao(data_cadastro):
    dias_para_adesao = random.randint(0, 10)  # Adesão pode ser no mesmo dia ou até 30 dias depois do cadastro
    data_adesao = data_cadastro + timedelta(days=dias_para_adesao)
    return data_adesao

def randomizar_datas_ativacao(data_adesao):
    dias_para_ativacao = random.randint(2, 7) 
    data_ativacao = data_adesao + timedelta(days=dias_para_ativacao)
    return data_ativacao

def randomizar_datas_rescisao(data_adesao):
    dias_para_rescisao = random.randint(30, 365)
    data_rescisao = data_adesao + timedelta(days=dias_para_rescisao)
    return data_rescisao
