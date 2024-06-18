def calcular_digito_verificador_cnpj(cnpj):
    pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[i]) * pesos[i] for i in range(12))
    primeiro_digito = 11 - (soma % 11)
    if primeiro_digito >= 10:
        primeiro_digito = 0
    
    cnpj += str(primeiro_digito)
    
    
    pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[i]) * pesos[i] for i in range(13))
    segundo_digito = 11 - (soma % 11)
    if segundo_digito >= 10:
        segundo_digito = 0
    
    return f"{primeiro_digito}{segundo_digito}"

def gerar_cnpj_valido_formatado(numero_base):
    cnpj_base = f"{numero_base:012d}"
    digitos_verificadores = calcular_digito_verificador_cnpj(cnpj_base)
    cnpj_completo = f"{cnpj_base}{digitos_verificadores}"
    cnpj_formatado = f"{cnpj_completo[:2]}.{cnpj_completo[2:5]}.{cnpj_completo[5:8]}/{cnpj_completo[8:12]}-{cnpj_completo[12:]}"
    return cnpj_formatado


cnpj_inicial = 999999990001  # Exemplo de CNPJ inicial, ajuste conforme necessário

gerar_cnpj_valido_formatado(cnpj_inicial)