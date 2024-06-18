def calcular_digito_verificador_rg(rg_base):
    pesos = [2, 3, 4, 5, 6, 7, 8, 9]
    soma = sum(int(digito) * peso for digito, peso in zip(rg_base, pesos))
    resto = soma % 11
    if resto == 0:
        return '0'
    elif resto == 1:
        return 'X'
    else:
        return str(11 - resto)

def gerar_rg_valido_formatado(rg_base_numero):
    rg_base = f"{rg_base_numero:07d}"
    digito_verificador = calcular_digito_verificador_rg(rg_base)
    return f"{rg_base}-{digito_verificador}"

#print(gerar_rg_valido_formatado(88888888))