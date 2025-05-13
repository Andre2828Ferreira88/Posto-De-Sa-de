
pesos = []
alturas = []
imcs = []

for i in range(3):
    print(f"\nDigite os dados da {i + 1}ª pessoa:")
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))
    
    pesos.append(peso)
    alturas.append(altura)

    imc = peso / (altura ** 2)
    imcs.append(imc)

print("\n--- Resultados ---\n")
for i in range(3):
    print(f"{i + 1}ª pessoa: peso = {pesos[i]:.1f}, altura = {alturas[i]:.2f} e imc = {imcs[i]:.2f}")
