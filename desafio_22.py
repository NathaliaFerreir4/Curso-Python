nome = str(input('Digite o seu nome completo: '))
print(nome.upper())
print(nome.lower())

sem_espacos = nome.replace(" ", "")
print(len(sem_espacos))

dividido = nome.split()
print(len(dividido[0]))