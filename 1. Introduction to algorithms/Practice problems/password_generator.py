# Problem Descripion: Escriba un algoritmo para generar una contraseña de longitud n. La contraseña debe generarse aleatoriamente y debe contener al menos una letra mayúscula, al menos una letra minúscula, al menos un número y al menos un carácter especial.

import random
import string

def generate_password(n):
  assert n >= 4, "La longitud de la contraseña debe ser al menos 4"
  
  password = []
  password.append(random.choice(string.ascii_uppercase))
  password.append(random.choice(string.ascii_lowercase))
  password.append(random.choice(string.digits))
  password.append(random.choice(string.punctuation))
  
  for i in range(n - 4):
    # Escogemos un número aleatorio entre 0 y 3
    random_choice = random.choice([0, 1, 2, 3])
    # Si el número aleatorio es 0, añadimos una letra mayúscula a la lista y así sucesivamente...
    if random_choice == 0:
      password.append(random.choice(string.ascii_uppercase))
    elif random_choice == 1:
      password.append(random.choice(string.ascii_lowercase))
    elif random_choice == 2:
      password.append(random.choice(string.digits))
    else:
      password.append(random.choice(string.punctuation))
  
  # Mezclamos la lista password
  random.shuffle(password)
  # Retornamos la lista password como un string
  return "".join(password)

print(generate_password(8))
