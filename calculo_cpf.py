def calcular_digito_verificador(cpf):
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = 11 - (soma % 11)
    if primeiro_digito >= 10:
        primeiro_digito = 0
    
    cpf += str(primeiro_digito)
    
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = 11 - (soma % 11)
    if segundo_digito >= 10:
        segundo_digito = 0
    
    return f"{primeiro_digito}{segundo_digito}"

def gerar_cpf_valido_formatado(numero_base):
    cpf_base = f"{numero_base:09d}"
    digitos_verificadores = calcular_digito_verificador(cpf_base)
    cpf_completo = f"{cpf_base}{digitos_verificadores}"
    cpf_formatado = f"{cpf_completo[:3]}.{cpf_completo[3:6]}.{cpf_completo[6:9]}-{cpf_completo[9:]}"
    return cpf_formatado
