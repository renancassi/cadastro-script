import hashlib

teste = 'teste'

hash_object = hashlib.sha256()

hash_object.update(teste.encode('utf-8'))

hash_hex = hash_object.hexdigest()

print(hash_hex)