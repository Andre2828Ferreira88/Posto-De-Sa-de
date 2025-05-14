caracteres = []
vogais = "aeiouAEIOU"
qtd_vogais = 0
qtd_consoantes = 0

for i in range(10):
    char = input(f"Digite o {i+1}º caractere: ")
    
    if char.isalpha() and len(char) == 1:
        caracteres.append(char)
        
        if char in vogais:
            qtd_vogais += 1
        else:
            qtd_consoantes += 1
    else:
        print("Caractere inválido. Digite apenas uma letra.")
        i -= 1

print("\nVetor de entrada:", caracteres)
print("Quantidade de vogais:", qtd_vogais)
print("Quantidade de consoantes:", qtd_consoantes)
