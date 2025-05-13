
exercicios = []
tempo = []
calorias = []
frases_motivacionais = [
    "Continue firme, você está indo muito bem!",
    "Cada treino te deixa mais forte!",
    "Não desista, o resultado está vindo!",
    "Seu corpo agradece cada minuto de exercício!",
    "Força! O progresso é feito de consistência!"
]

def cadastrar_exercicio():
    nome = input("Digite o nome do exercício: ")
    t = int(input("Digite o tempo em minutos: "))
    c = int(input("Digite as calorias queimadas: "))
    dia = input("Digite o dia da semana: ")
    exercicios.append([nome, t, c, dia])
    print("Exercício cadastrado com sucesso!\n")

def relatorio_dia():
    dia = input("Digite o dia que deseja ver o relatório: ")
    total_tempo = 0
    total_calorias = 0
    for ex in exercicios:
        if ex[3] == dia:
            print(f"Exercício: {ex[0]}, Tempo: {ex[1]} min, Calorias: {ex[2]}")
            total_tempo += ex[1]
            total_calorias += ex[2]
    print(f"Tempo total: {total_tempo} min, Calorias totais: {total_calorias}\n")

def calcular_imc():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = peso / (altura * altura)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"
    print(f"Seu IMC é {imc:.2f} - {classificacao}\n")

def definir_meta():
    meta = int(input("Digite sua meta de calorias por semana: "))
    total = 0
    for ex in exercicios:
        total += ex[2]
    print(f"Total de calorias queimadas: {total}")
    if total >= meta:
        print("Parabéns! Você atingiu sua meta!\n")
    else:
        print("Continue tentando! Você vai conseguir!\n")

def mostrar_frase():
    from random import randint
    pos = randint(0, len(frases_motivacionais)-1)
    print(frases_motivacionais[pos] + "\n")

def media_calorias():
    if len(exercicios) == 0:
        print("Nenhum exercício registrado ainda.\n")
        return
    soma = 0
    for ex in exercicios:
        soma += ex[2]
    media = soma / len(exercicios)
    print(f"Média de calorias por exercício: {media:.1f}\n")

def codigo_barras():
    for ex in exercicios:
        print(f"{ex[0]}: {'|'*ex[2]}")
    print()

def menu():
    while True:
        print("""
------ MENU ------
1. Cadastrar Exercício
2. Relatório Diário
3. Calcular IMC
4. Definir Meta Semanal
5. Ver Frase Motivacional
6. Média de Calorias por Exercício
7. Código de Barras no Terminal
8. Sair
""")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_exercicio()
        elif opcao == '2':
            relatorio_dia()
        elif opcao == '3':
            calcular_imc()
        elif opcao == '4':
            definir_meta()
        elif opcao == '5':
            mostrar_frase()
        elif opcao == '6':
            media_calorias()
        elif opcao == '7':
            codigo_barras()
        elif opcao == '8':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida!\n")

menu()
