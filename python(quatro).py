
lista = [13, 41, 13, 8, 21, 7, 79]

print(lista)

numero_procurado = int(input("Digite o número a ser pesquisado na lista: "))

maior = lista[0]
for num in lista:
    if num > maior:
        maior = num

menor = lista[0]
for num in lista:
    if num < menor:
        menor = num

quantidade = 0
for num in lista:
    if num == numero_procurado:
        quantidade += 1

# Mostrando os resultados
print("Maior elemento:", maior)
print("Menor elemento:", menor)
print(f"Número de ocorrências do número {numero_procurado} na lista: {quantidade}")
