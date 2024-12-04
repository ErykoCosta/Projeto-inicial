# print("teste 1")
# print(3)
# print(3+4)
#print("olá"+ " "+ "pessoal")
#print("Olá," + input("Digite seu nome: ")+ "!")


#criando um programa que digita um nome e retorno o número de caracteres

#print(len(input("Digite seu nome: ")))

# print(int(input("Digite um número: ")) + int(input("Digite outro número: ")))

#quantidade de letras usando variável

# nome = input("Qual seu nome: ")
# quant_letras = len(nome)
# print(quant_letras)

#Cauculo de Bônus de Usuário
CONSTANTE_BONUS = 1000

nome = input("Digite seu nome: ")

if nome.isdigit():
    print("Erro - Vc digitou o nome errado!")
    exit()
elif len(nome) == 0:
    print("Erro - Você não digitou nada!")
    exit()
elif nome.isspace():
    print("Erro - Você digitou só espaço!")
    
salario = float(input("Digite seu salário: "))
bonus = float(input("Digite seu bônus: "))

valor_bonus = CONSTANTE_BONUS + salario * bonus

print(f"Olá {nome} você possui um bônus de {valor_bonus}")
