frase = 'Curso em Video Python'
print(frase.count('o'))
print(frase.upper())
print(len(frase))
print(frase.replace('Python', 'Android'))
frase = frase.replace('Python', 'Android')
print(frase)
print(frase.find('video'))
print(frase.lower().find('video'))

dividido = frase.split()
print(dividido[2][3])