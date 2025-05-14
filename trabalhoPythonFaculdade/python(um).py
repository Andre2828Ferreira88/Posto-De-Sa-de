numeros = []

for i in range(10):
    numero = int(input("Digite um numero: "))
    numeros.append(numero)
    
maior = max(numeros)

menor = min(numeros)

quantidade_pares = 0
for numero in numeros:
        if numero % 2 == 0:
            quantidade_pares += 1

soma = sum(numeros)
media = soma / 10

menores_que_media = []
for numero in numeros:
    if numero < media:
        menores_que_media.append(numero)

print("maior numero: ", maior)
print("menor numero: ", menor)
print("Quantidade de numeros pares: ", quantidade_pares)
print("Media numeros: ", media)
print("Numero menores que a média: ", menores_que_media)