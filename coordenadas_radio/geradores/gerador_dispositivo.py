from faker import Faker
import os
serialFake = Faker()


os.system('cls')

for i in range(20):
    print(f'{i} Ip: ' + serialFake.ipv4_private())
    print(f'{i} Usuário: ' + serialFake.user_name())
    print(f'{i} Senha: ' + serialFake.password(special_chars=False, length=8, upper_case=False))
    print(f'{i} Serial: ' + serialFake.mac_address())
    print(f'{i} Serial: ' + serialFake.mac_address())
    print('\n')
    