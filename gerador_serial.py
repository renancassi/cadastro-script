import random
import string

def gerador_serial():
    serial = "FTTH"
    for _ in range(3):
        serial += random.choice(string.digits)

    serial += random.choice(string.ascii_uppercase)
    
    for _ in range(2):
        serial += random.choice(string.digits)
    
    serial += random.choice(string.ascii_uppercase)
    serial += random.choice(string.digits)
    
    return serial
