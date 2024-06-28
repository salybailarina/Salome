
nomeProprio = input("Digite seu nome:")
print("Olá, "+ nomeProprio)
apelido = input("Digite seu apelido:")
print("Teu apelido é: "+ apelido)
endereco = input("Digite seu endereço:")
print("Teu endereço é: "+ endereco)
cidadeCodigo = input("Digite sua cidade e código postal:")
print("Tua cidade e código postal é: "+ cidadeCodigo)
print(f"Teus dados são:{nomeProprio}, {apelido}, {endereco} e {cidadeCodigo}")
                                                                                                



nome = input("Digite seu nome: ")
print("nome confirmado, "+ nome )
ano = int(input("Digite seu ano: "))
print("ano confirmado, ", ano)
print(f"Em 2024 você terá: {2024 - ano}")
print(f"{nome} é uma pessoa legal, nascida no ano de {ano}. Uma vez,{nome} acordou cedo para ir ao trabalho e aconteceu uma coisa inesperada")




cidade = "São Paulo"
print("A cidade é: "+ cidade)
cidade = "Rio de Janeiro"
print("Cidade atualizada: "+ cidade)




variavelString = "String"
print(f"Variavel 1 : {type(variavelString)}")
variavelInteiro = 3
print(f"Variavel 2 : {type(variavelInteiro)}")
variavelFloat = 3.6
print(f"Variavel 3 : {type(variavelFloat)}")





parte1 = "A vida"
print("parte um da frase:"+ parte1)
parte2 = " vale a pena?"
print("parte dois da frase:"+ parte2)
print(f"Frase completa: {parte1}{parte2}")






altura = float(input("Qual sua altura? "))
peso = float(input("Qual seu peso? "))
imc = peso / (altura / 100) ** 2
print(f"O IMC é: {imc}")




numero = int(input("Digite um número: "))
calculo = numero * 5 
print(f"{numero} vezes 5 é", calculo )






nome = input("Digite seu nome: ")
print("nome confirmado, "+ nome )
ano = int(input("Digite seu ano: "))
print("ano confirmado, ", ano)
print(f"Olá {nome}, você fará {2024 - ano} anos no final de 2024")




preco = float(input("Digite preço do produto: "))
porcentagem = float(input("Digite porcentagem: "))
desconto = preco * porcentagem / 100
print(f"O valor do desconto é {desconto} e o novo preço será {preco - desconto}")




preco = float(input("Digite preço do produto: "))
porcentagem = float(input("Digite porcentagem: "))
desconto = preco * porcentagem / 100
print(f"O valor do desconto é {desconto} e o novo preço será {preco + desconto}")





valor = float(input("Digite um valor em reais: "))
print(f"Em dólares o valor é de {round(valor / 5.45,2)}")








capital = float(input("Digite o capital inicial: "))
taxa = float(input("Digite a taxa de de juros anual: "))
tempoAnos = float(input("Digite o tempo em anos: "))
juros = capital * taxa * tempoAnos
print("Os juros são:", juros)







numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite mais um numero: "))
numero3 = float(input("Digite otro numero mais por gentileza: "))
media = numero1 + numero2 + numero3 / 3
print("A média aritmética é de:", media)






largura = float(input("Digite uma largura de um retângulo x: "))
altura = float(input("Digite uma altura para esse retângulo x: "))
area = largura * altura
perimetro = 2 *(largura + altura)
print(f"A área do triângulo é de {area} e o perímetro é de {perimetro}")





temperaturaC = float(input("Digite uma temperatura em graus Celsius: "))
temperaturaF = temperaturaC * 9 / 5 + 32
print("A temperatura em Fahrenheit é", temperaturaF)






notas = []
qtdNotas = int(input("Digite quantos notas você quer colocar: "))
for i in range(qtdNotas):
    num = float(input(f"Digite o {i+1}º: "))
    notas.append(num)

mediaNotas = sum(notas) / len(notas)
print("A média aritmética é de:", mediaNotas)




num = int(input("Digite um número: "))
numero = num % 2

if numero == 0:
   print("Seu número é par")
else:
    print("Seu número é ímpar")










numeros = []
qtdNum = int(input("Digite quantos números você quer colocar: "))
for i in range(qtdNum):
    num = float(input(f"Digite o {i+1}º: "))
    numeros.append(num)

maiorNum =  numeros[0]   
for item in len(numeros):
    maior = []
    maior > maiorNum
print("O maior número é: ", maiorNum)


























































numero = int(input("entre com um número: "))

if numero < 0:
    print("esse número é negativo")
if numero > 0:
    print("esse número é positivo")
if numero == 0:
    print("O número é 0")










numero = int(input("Digite um número inteiro: "))
if numero == 1984:
  print("Digitou o número 1984 Orwall")
  







numero = int(input("Digite um número inteiro: "))
if numero < 0:
  print(f"O número multiplicado por -1 é: {numero * -1}")
else:
  print("Teu número é:", numero)







nome = input("Digite seu nome:")

if nome != "Jerry":
  numero = int(input("Digite o número de porções:"))
  preco = numero * 5.90
  print(f"Custo total é de: {preco}")



















numero = int(input("Digite um número inteiro: "))
if numero < 1000:
    text1 = "Este número é menor que 1000"
    print(text1, "Obg!")

    if numero < 100:
        text2 = "Este número é menor que 100"
        print(text1, text2, "Obg!")
    
        if numero < 10:
            text3 = "Este número é menor que 10"
            print(text1, text2, text3, "Obg!")
        



nome = input("Digite seu nome: ")
if nome == "Salome":
    print("Vc mora na cidade Curitiba, estado Paraná e cep 8264219")
else:
    print("esse usuário não existe em nossas bases de dados")




num1 = float(input("Digite um número: "))
num2 = float(input("Digite mais um número: "))
operacao = input("Escolhe uma operação: somar, multiplicar ou subtrair.  ")
somar = num1 + num2
multiplicar = num1 * num2
subtrair = num1 - num2
if operacao == "somar" or operacao == "Somar":
    print(f"A soma dos seus números deu: {somar}") 
if operacao == "multiplicar" or operacao == "Multiplicar":
    print(f"A multiplicação dos seus números deu: {multiplicar}")
if operacao == "subtrair" or operacao == "Subtrair":
    print(f"A subtração dos seus números deu: {subtrair}")










temperaturaF = float(input("Digite uma temperatura em graus Fahrenheit: "))
temperaturaC = (temperaturaF - 32) * 5 / 9
print(f"A temperatura em graus celsius é de {temperaturaC} ºC")
if temperaturaC < 0:
    print("Brr! Está frio aqui!!")



salarioXhora = float(input("Digite seu salário por hora: "))
horasTrabalhadas = float(input("Digite as horas trabalhadas: "))
diaDaSemana = input("Digite o dia da semana: ")
salarioDiario = salarioXhora * horasTrabalhadas
if diaDaSemana == "Domingo" or diaDaSemana == "domingo":
    print(f"Seu salário o domingo devido a mais horas trabalhadas é: {salarioXhora * (horasTrabalhadas * 2)}")
else:
    print("Seu salário diário é:", salarioDiario)

