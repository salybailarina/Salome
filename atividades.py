
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

