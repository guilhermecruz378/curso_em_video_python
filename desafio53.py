# Detector de palindrómo
n = (input('Digite um nome ou uma palavra: ')).strip()
separa = n.split()
junta = n.join('')

inverso = junta[::-1]

print(junta)
print(inverso)
