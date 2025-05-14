
lista1 = []
lista2 = []
soma_listas = []

print("Digite 5 números inteiros da lista1:")
for i in range(5):
    numero = int(input())
    lista1.append(numero)

print("\nDigite 5 números inteiros da lista2:")
for i in range(5):
    numero = int(input())
    lista2.append(numero)

for i in range(5):
    soma = lista1[i] + lista2[i]
    soma_listas.append(soma)

print("\nLista1:", lista1)
print("Lista2:", lista2)
print("Soma:  ", soma_listas)
