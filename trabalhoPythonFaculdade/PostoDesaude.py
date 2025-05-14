#Andre Ferreira Monteiro 10737670




# Listas para guardar os dados dos exercícios
exercicios = []

# Frases para motivar o usuário
frases = [
    "Continue firme, você está indo muito bem!",
    "Cada treino te deixa mais forte!",
    "Não desista, o resultado está vindo!",
    "Seu corpo agradece cada minuto de exercício!",
    "Força! O progresso é feito de consistência!"
]

# Função para cadastrar um novo exercício
def cadastrar():
    nome = input("Nome do exercício: ")
    tempo = int(input("Tempo (minutos): "))
    calorias = int(input("Calorias gastas: "))
    dia = input("Dia da semana: ")
    exercicios.append([nome, tempo, calorias, dia])
    print("Exercício salvo!\n")

# Função para mostrar os exercícios de um dia específico
def relatorio():
    dia = input("Qual dia você quer ver? ")
    total_tempo = 0
    total_calorias = 0

    for e in exercicios:
        if e[3] == dia:
            print(f"{e[0]} - {e[1]}min - {e[2]} cal")
            total_tempo += e[1]
            total_calorias += e[2]

    print(f"Total de tempo: {total_tempo}min")
    print(f"Total de calorias: {total_calorias} cal\n")

# Função para calcular o IMC
def imc():
    peso = float(input("Seu peso (kg): ".replace(",",".")))
    altura = float(input("Sua altura (m): ".replace(",",".")))
    resultado = peso / (altura ** 2)

    if resultado < 18.5:
        status = "Abaixo do peso"
    elif resultado < 25:
        status = "Peso normal"
    elif resultado < 30:
        status = "Sobrepeso"
    else:
        status = "Obesidade"

    print(f"Seu IMC é {resultado:.2f} - {status}\n")

# Função para definir e comparar a meta de calorias da semana
def meta():
    objetivo = int(input("Meta de calorias na semana: "))
    total = 0

    for e in exercicios:
        total += e[2]

    print(f"Você queimou {total} calorias.")
    if total >= objetivo:
        print("Parabéns! Meta atingida!\n")
    else:
        print("Ainda não atingiu, mas continue firme!\n")

# Função para mostrar uma frase motivacional aleatória
def motivar():
    from random import choice
    print(choice(frases) + "\n")

# Função para calcular a média de calorias por exercício
def media():
    if not exercicios:
        print("Nenhum exercício registrado ainda.\n")
        return

    total = sum(e[2] for e in exercicios)
    media = total / len(exercicios)
    print(f"Média de calorias por exercício: {media:.1f}\n")

# Função que mostra um "gráfico de barras" no terminal com base nas calorias
def barras():
    for e in exercicios:
        print(f"{e[0]}: {'|' * e[2]}")
    print()

# Menu principal do programa
def menu():
    while True:
        print("""
==== MENU ====
1 - Adicionar exercício
2 - Ver exercícios de um dia
3 - Calcular IMC
4 - Verificar meta semanal
5 - Frase motivacional
6 - Ver média de calorias
7 - Mostrar gráfico de barras
8 - Sair
""")
        escolha = input("Escolha: ")

        if escolha == '1':
            cadastrar()
        elif escolha == '2':
            relatorio()
        elif escolha == '3':
            imc()
        elif escolha == '4':
            meta()
        elif escolha == '5':
            motivar()
        elif escolha == '6':
            media()
        elif escolha == '7':
            barras()
        elif escolha == '8':
            print("Até a próxima!")
            break
        else:
            print("Opção inválida. Tente de novo.\n")


menu()
