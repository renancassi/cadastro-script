ascii_art ="""
@@@@@@@@@@@@@@@@@@@@@@@@@@&GYJ?YG@@@@@@@@@@@@@&#BB#&@@@@@@@@@@@@@@@@@#BP555G&@@@@@&GPG#@@@@@@B5Y5#@@
@@@&PJ7~~^^^~~75#@@@@@@@G7::^!!^.^G@@@@@@B5?!^:::::^!5&@@@@@@@@@#5?!^::^^~^::5@@&J::^::!G@@P~.^~.:5@
@&J:.~7JYYYYYJ!:.7P@@@G~ ^JPBBBBJ :#@@@5^.:~?Y5PGPPY!.:Y@@@@@@5~.:~?Y5PGGBB7 ^@@? ^PGGJ..PJ :YGBJ :&
@J ^PBBBBBBBBBY^ ^5@@Y..JGBGBBP?^.7&@@B. YGBBBBBBBBBB5: J@@@@? ^YGBBBBBBBP7.:P@&: YBGGBJ . ^PBGBY :#
@P:.!?YGGGGBY^.~P@@@5 :5BGGG5!.:?B@@@@5 :GBGGGGPPGGGGBY..#@@#..5BGGGBG5J~.:J#@@&^ JBGGGG~ :PBGGB7 !@
@@&P7 .PGGGB~ 7@@@@@~ ?BGGBP: ?@@@@@@@J ~GGGGG!. 7BGGBP..B@@G..PBGGG!:. . ^Y&@@@J ^GGGGBY.YBGGB5..G@
@@@@B..PBGGG^ Y@@@@@J :5BGGGJ.:Y@@@@@@? ~BGGGG:.!PBGGB7 ^&@@G :PGGGG!7J555~ !@@@&: ?BGGGG5BGGGG^ ?@@
@@@@G..PBGGG: P@@@@@@Y..JBGGB5~ ~B@@@@7 !BGGGG5PBBGBG? :B@@@G :PGGGGBBBBBP^ ?@@@@P .5BGGGBGGGB! ~&@@
@@@@G :PGGBP..G@@@@@@@G^ 7GGGBB7 ^&@@@7 !BGGGGBBBBPJ^ ~B@@@@G..PBGGGBG5J~.:Y@@@@@@Y :5BGGGGGB? :#@@@
@@@@5 :GGGB5..#@@@@@@@@P. 5BGGB5..B@@@? !BGGGGPY?~.:!P@@@@@@B..5BGGG7::^75&@@@@@@@@5..7GGGGBJ .G@@@@
@@@#~ 7BGGBP: 7B@@@@@&?..?GGGGB? ^@@@@? ~BGGGG~ ^?P&@@@@@@@@#: YBGBP. P@@@@@@@@@@@@5..YBGGBY..P@@@@@
@#!.:7GGGGGGPJ..Y@@@G: 7PBGGBBJ..G@@@@Y ^GGGBP. G@@@@@@@@@@@@~ ?BGB5..#@@@@@@@@@@@G..YBGGBY..P@@@@@@
@7 ~GBBBBBBBG5: J@@#. JBBBBBP! ^G@@@@@G .PBBB? ^@@@@@@@@@@@@@5 :5BB! !@@@@@@@@@@@@~ 7BGBB? .P@@@@@@@
@Y :7????7!^:.~P@@@B. ?5P5?~.:J&@@@@@@@! ^5P? :G@@@@@@@@@@@@@@Y..!^ ~#@@@@@@@@@@@@~ 7GG5~ ~B@@@@@@@@
@@GJ7!!!!7?YP#@@@@@@G7^^^^~7P&@@@@@@@@@@Y~::^?#@@@@@@@@@@@@@@@@#5JJP&@@@@@@@@@@@@@G~::::^Y&@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&#&@@@@@@@@@@@@@@@@##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#BB#@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ USER GENERATOR @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

bairros_beltrão = [
    "Bairro Água Branca",
    "Bairro Cango",
    "Bairro Centro",
    "Bairro Industrial",
    "Bairro Jardim Seminário",
    "Bairro Júpter",
    "Bairro Luther King",
    "Bairro Miniguaçu",
    "Bairro Novo Mundo",
    "Bairro Pinheirão",
    "Bairro Sadia",
    "Bairro São Francisco",
    "Bairro Vila Nova",
    "Comunidade Divisor",
    "Comunidade Km 23",
    "Comunidade Linha Eva e Linha Macagnan",
    "Comunidade Linha Hobold",
    "Comunidade Linha São Paula",
    "Comunidade Linha Volpato",
    "Comunidade Rio do Mato",
    "Comunidade Rio Guarapuava",
    "Comunidade Rio Tuna",
    "Comunidade São Francisco de Assis",
    "Comunidade São Pio X – Km 20",
    "Comunidade Secção Progresso",
    "Comunidade Vila Lobos",
    "Comunidade Volta Grande",
    "Bairro Alvorada",
    "Bairro Cantelmo",
    "Bairro Cristo Rei",
    "Bairro Jardim Floresta e Italia",
    "Bairro Jardim Virgínia",
    "Bairro Kennedy",
    "Bairro Marrecas",
    "Bairro Nossa Senhora Aparecida",
    "Bairro Padre Ulrico",
    "Bairro Pinheirinho",
    "Bairro São Cristovão",
    "Bairro São Miguel",
    "Comunidade Assentamento Missões",
    "Comunidade Jacutinga",
    "Comunidade Lageado Grande",
    "Comunidade Linha Formiga",
    "Comunidade Linha Santa Rosa – Km 08",
    "Comunidade Linha Triton",
    "Comunidade Nova Concórdia",
    "Comunidade Rio Erval – Km 15",
    "Comunidade Rio Pedreirinho",
    "Comunidade Santa Bárbara",
    "Comunidade São João",
    "Comunidade Secção Jacaré",
    "Comunidade Secção São Miguel",
    "Comunidade Vila Rural Gralha Azul"
]

bairros_doisVizinhos = [
    "Da Luz",
    "Das Torres",
    "Sagrada Família",
    "Santo Antônio",
    "Jardim da Colina",
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

bairros_patoBranco = [
    "Aeroporto",
    "Alto da Glória",
    "Alvorada",
    "Amadori",
    "Anchieta",
    "Baixada",
    "Bancários",
    "Bela Vista",
    "Bonatto",
    "Bortot",
    "Brasília",
    "Cadorin",
    "Centro",
    "Cristo Rei",
    "Dall Ross",
    "Fraron",
    "Gralha Azul",
    "Industrial",
    "Jardim Floresta",
    "Jardim Primavera",
    "Jardim das Américas",
    "La Salle",
    "Menino Deus",
    "Morumbi",
    "Novo Horizonte",
    "Pagnoncelli",
    "Parque do Som",
    "Parzianello",
    "Pinheirinho",
    "Pinheiros",
    "Planalto",
    "Sambugaro",
    "Santa Terezinha",
    "Santo Antônio",
    "São Cristóvão",
    "São Francisco",
    "São João",
    "São Luiz",
    "São Roque",
    "São Vicente",
    "Sudoeste",
    "Trevo da Guarany",
    "Veneza",
    "Vila Esperança",
    "Vila Isabel"
]

cidades = [
    "Dois Vizinhos",
    "Francisco Beltrão",
    "Pato Branco"
]

# Complementos
complementos = [
    "Casa",
    "Apartamento",
    "APTO",
    "Loja",
    "Sobrado",
    "Bloco",
    "Fundos"
]
