# # 1
# nomeProprio = input("Digite seu nome:")
# print("Olá, "+ nomeProprio)
# apelido = input("Digite seu apelido:")
# print("Teu apelido é: "+ apelido)
# endereco = input("Digite seu endereço:")
# print("Teu endereço é: "+ endereco)
# cidadeCodigo = input("Digite sua cidade e código postal:")
# print("Tua cidade e código postal é: "+ cidadeCodigo)
# print(f"Teus dados são:{nomeProprio}, {apelido}, {endereco} e {cidadeCodigo}")
                                                                                                


# # 2
# nome = input("Digite seu nome: ")
# print("nome confirmado, "+ nome )
# ano = int(input("Digite seu ano: "))
# print("ano confirmado, ", ano)
# print(f"Em 2024 você terá: {2024 - ano}")
# print(f"{nome} é uma pessoa legal, nascida no ano de {ano}. Uma vez,{nome} acordou cedo para ir ao trabalho e aconteceu uma coisa inesperada")



# # 3
# cidade = "São Paulo"
# print("A cidade é: "+ cidade)
# cidade = "Rio de Janeiro"
# print("Cidade atualizada: "+ cidade)



# # 4
# variavelString = "String"
# print(f"Variavel 1 : {type(variavelString)}")
# variavelInteiro = 3
# print(f"Variavel 2 : {type(variavelInteiro)}")
# variavelFloat = 3.6
# print(f"Variavel 3 : {type(variavelFloat)}")




# # 5
# parte1 = "A vida"
# print("parte um da frase:"+ parte1)
# parte2 = " vale a pena?"
# print("parte dois da frase:"+ parte2)
# print(f"Frase completa: {parte1}{parte2}")







# # 6
# numero = int(input("Digite um número: "))
# calculo = numero * 5 
# print(f"{numero} vezes 5 é", calculo )







# # 7
# altura = float(input("Qual sua altura? "))
# peso = float(input("Qual seu peso? "))
# imc = peso / (altura / 100) ** 2
# print(f"O IMC é: {imc}")










# # 8
# nome = input("Digite seu nome: ")
# print("nome confirmado, "+ nome )
# ano = int(input("Digite seu ano: "))
# print("ano confirmado, ", ano)
# print(f"Olá {nome}, você fará {2024 - ano} anos no final de 2024")





# # 9
# preco = float(input("Digite preço do produto: "))
# porcentagem = float(input("Digite porcentagem: "))
# desconto = preco * porcentagem / 100
# print(f"O valor do desconto é {desconto} e o novo preço será {preco - desconto}")






# # 10
# preco = float(input("Digite preço do produto: "))
# porcentagem = float(input("Digite porcentagem: "))
# desconto = preco * porcentagem / 100
# print(f"O valor do desconto é {desconto} e o novo preço será {preco + desconto}")






# # 11
# valor = float(input("Digite um valor em reais: "))
# print(f"Em dólares o valor é de {round(valor / 5.45,2)}")









# # 12
# capital = float(input("Digite o capital inicial: "))
# taxa = float(input("Digite a taxa de de juros anual: "))
# tempoAnos = float(input("Digite o tempo em anos: "))
# juros = capital * taxa * tempoAnos
# print("Os juros são:", juros)






# # 13
# numero1 = float(input("Digite um numero: "))
# numero2 = float(input("Digite mais um numero: "))
# numero3 = float(input("Digite otro numero mais por gentileza: "))
# media = numero1 + numero2 + numero3 / 3
# print("A média aritmética é de:", media)





# # Exemplo
# largura = float(input("Digite uma largura de um retângulo x: "))
# altura = float(input("Digite uma altura para esse retângulo x: "))
# area = largura * altura
# perimetro = 2 *(largura + altura)
# print(f"A área do triângulo é de {area} e o perímetro é de {perimetro}")




# # 14
# temperaturaC = float(input("Digite uma temperatura em graus Celsius: "))
# temperaturaF = temperaturaC * 9 / 5 + 32
# print("A temperatura em Fahrenheit é", temperaturaF)





# # 15
# notas = []
# qtdNotas = int(input("Digite quantos notas você quer colocar: "))
# for i in range(qtdNotas):
#     num = float(input(f"Digite o {i+1}º: "))
#     notas.append(num)

# mediaNotas = sum(notas) / len(notas)
# print("A média aritmética é de:", mediaNotas)



# # 16
# numero = int(input("Digite um número inteiro: "))
# if numero < 0:
#   print(f"O número multiplicado por -1 é: {numero * -1}")
# else:
#   print("Teu número é:", numero)

























# num = int(input("Digite um número: "))
# numero = num % 2

# if numero == 0:
#    print("Seu número é par")
# else:
#     print("Seu número é ímpar")









# # 17
# nome = input("Digite seu nome:")

# if nome != "Jerry":
#   numero = int(input("Digite o número de porções:"))
#   preco = numero * 5.90
#   print(f"Custo total é de: {preco}")
































# numeros = []
# qtdNum = int(input("Digite quantos números você quer colocar: "))
# for i in range(qtdNum):
#     num = float(input(f"Digite o {i+1}º: "))
#     numeros.append(num)

# maiorNum =  numeros[0]   
# for item in len(numeros):
#     maior = []
#     maior > maiorNum
# print("O maior número é: ", maiorNum)




# # 18
# numero = int(input("Digite um número inteiro: "))
# if numero < 1000:
#     text1 = "Este número é menor que 1000"
#     print(text1, "Obg!")

#     if numero < 100:
#         text2 = "Este número é menor que 100"
#         print(text1, text2, "Obg!")
    
#         if numero < 10:
#             text3 = "Este número é menor que 10"
#             print(text1, text2, text3, "Obg!")
        























# ptos = float(input("Digite quantos ptos no cartão tem: "))
# bonus10 = ptos  / 10
# if ptos < 100:
#     print(f"Bônus final do seu ano é: {bonus10}")



# # 19
# nome = input("Digite seu nome: ")
# if nome == "Salome":
#     print("Vc mora na cidade Curitiba, estado Paraná e cep 8264219")
# else:
#     print("esse usuário não existe em nossas bases de dados")















# # Exemplo
# while True:
#    codigo = input("por favor, insira o PIN: ")
#    if codigo == "1234":
#     break
# print("Errado!...tente de novo")
# print("Programa encerrado, Obg!")




# # 20
# num1 = float(input("Digite um número: "))
# num2 = float(input("Digite mais um número: "))
# operacao = input("Escolhe uma operação: somar, multiplicar ou subtrair.  ")
# somar = num1 + num2
# multiplicar = num1 * num2
# subtrair = num1 - num2
# if operacao == "somar" or operacao == "Somar":
#     print(f"A soma dos seus números deu: {somar}") 
# if operacao == "multiplicar" or operacao == "Multiplicar":
#     print(f"A multiplicação dos seus números deu: {multiplicar}")
# if operacao == "subtrair" or operacao == "Subtrair":
#     print(f"A subtração dos seus números deu: {subtrair}")



# # 21
# temperaturaF = float(input("Digite uma temperatura em graus Fahrenheit: "))
# temperaturaC = (temperaturaF - 32) * 5 / 9
# print(f"A temperatura em graus celsius é de {temperaturaC} ºC")
# if temperaturaC < 0:
#     print("Brr! Está frio aqui!!")





# # 22
# salarioXhora = float(input("Digite seu salário por hora: "))
# horasTrabalhadas = float(input("Digite as horas trabalhadas: "))
# diaDaSemana = input("Digite o dia da semana: ")
# salarioDiario = salarioXhora * horasTrabalhadas
# if diaDaSemana == "Domingo" or diaDaSemana == "domingo":
#     print(f"Seu salário o domingo devido a mais horas trabalhadas é: {salarioXhora * (horasTrabalhadas * 2)}")
# else:
#     print("Seu salário diário é:", salarioDiario)






# # 23

# pontosCartao = float(input("digite a quantidade de pessoas:"))
# if pontosCartao< 100:
#     taxadebonus= 0.12
# if pontosCartao > 100:
#     taxadebonus= 0.16
# bonus = pontosCartao * taxadebonus
# print(f"O bonus é de :{bonus} pontos")
 





# # 24
# temperatura = int(input("Digite a temperatura: "))
# chuva = input("Vai chover: ")

# if temperatura > 20:
#    print("Roupa leve")
# elif temperatura > 10:
#    print("Se abriga um pouco")
# elif temperatura > 5:
#    print("Se abriga bem")

# if chuva.lower() == "não":
#    print("Leva guardachuva")





# # 25
# idade = int(input("Digite sua idade :"))
# if idade > 18:
#     print("maior de idade")
# else:
#     print("menor de idade")















# # # 26
# num1 = float(input("Digite uma nota:"))
# num2 = float(input("Digite mais uma nota:"))
# num3 = float(input("Digite mais uma nota:"))
# num4 = float(input("Digite uma ultima nota:"))
# media = (num1 + num2 + num3 + num4)/4
# print("A media dessas notas é", media)



















# # 27
# gasto = int(input("Digite seu gasto: "))
# if 0<gasto<50:
#     print("economico")
# elif 99>gasto>50:
#     print("intermediario")
# elif gasto>100:
#     print("clase executiva")  
# else:
#     print("Não gastou")

     
      







# # 28
# idade = int(input("Digite sua idade :"))
# if idade > 16:
#     print("pode votar")
# else:
#     print("não pode votar")











# # 29
# numMes = int(input("Digite um número e agora te mostro o mês correspondente: "))
# if numMes == 1:
#     print("Janeiro")
# elif numMes == 2:
#     print("Fevereiro")
# elif numMes == 3:
#     print("Março")
# elif numMes == 4:
#     print("Abril")
# elif numMes == 5:
#     print("Maio")
# elif numMes == 6:
#     print("Junho")
# elif numMes == 7:
#     print("Julho")
# elif numMes == 8:
#     print("Agosto")
# elif numMes == 9:
#     print("Setembro")
# elif numMes == 10:
#     print("Outubro")
# elif numMes == 11:
#     print("Novembro")
# elif numMes == 12:
#     print("Decembro")
# else:
#     print("Mês inválido")








# # 30
# num1 = float(input("Digite um número: "))
# num2 = float(input("Digite mais um número: "))
# if num1 > num2:
#     print(f"{num1} é maior que{num2}")
# elif num2 > num1:
#        print(f"{num2} é maior que{num1}")
# else:
#     print("São iguais")





# # 31
# nome1 = input("Digite um nome: ")
# idade1 = int(input("Digite uma idade para ele: "))
# nome2 = input("Digite mais um nome: ")
# idade2 = int(input("Digite uma idade para ele: "))
# if idade1>idade2:
#     print(f"{nome1} é mais velho")
# elif idade2>idade1:
#         print(f"{nome2} é mais velho")
# else:
#     print("Tem a mesma idade")











# # 32
# # nao tem





# # 33
# idade = int(input("Digite sua idade: "))
# if 0 <idade <= 5:
#         print("Suspeito q ainda não sabe escrever")
# elif idade > 5:
#         print(f"Vc tem {idade} anos")
# else:
#     print("Idade inválida")




# # 34
# nome = input("Digite um nome: ")
# donald1 = "Enrique"
# donald2 = "Eduardo"
# donald3 = "Edgar"

# mickey1 = "Alex"
# mickey2 = "Wilson"

# if nome == donald1 or nome == donald2 or nome == donald3:
#     print("É irmão d Donald")
# elif nome == mickey1 or nome == mickey2:
#     print("É irmão d Mickey")
# else:
#     print("Beleza")





# # # 35
# pontosCursos = float(input("Digite seus pontos: "))
 
# if pontosCursos < 0:
#   print("Inválido")
 
# elif pontosCursos > 0 or pontosCursos < 49:
#   print("Falhou")
 
# elif pontosCursos > 50 or pontosCursos < 59:
#   print("Sua nota é: 1")
 
# elif pontosCursos > 60 or pontosCursos < 69:
#   print("Sua nota é: 2")
 
# elif pontosCursos > 70 or pontosCursos < 79:
#   print("Sua nota é: 3")
 
# elif pontosCursos > 80 or pontosCursos < 89:
#   print("Sua nota é: 4")
 
# elif pontosCursos > 90 or pontosCursos < 99:
#   print("Sua nota é: 5")
 
# else:
#   print("Inválido")




# # 36
# num = int(input("Digite um número: "))

# if num % 3 == 0:
#   print("Fizz")

# elif num % 5 == 0:
#   print("Buzz")
  
# elif num % 3 == 0 and num % 5 == 0:
#   print("FizzBuzz")








# # 37
# ano = int(input("Digite um ano: "))
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#   print("Ano bissexto")
# else:
#   print("Não é ano bissexto")








# # 38
# while True:
#    pergunta = input("Quer continuar: ")
#    if pergunta == "não":
#       break
# print("OK")
      




# # 39
# from math import sqrt
# while True:
#    numero = int(input("Escreva um número inteiro: "))
#    if numero < 0:
#       print("Inválido")
#    elif numero > 0:
#       print("sqrt"(numero))  
#    elif numero == 0: 
#       break




# # 40
# num = 5
# print("contagem regressiva!")
# while True:
#       print(num)
#       num = num -1
#       if num == 0:
#        break
# print("agora!")






# # 41
# senha = input("pro favor, digite uma senha: ")
# while True:
#      confSenha = input("Digite a senha de novo: ")
#      if confSenha == senha:
#          print("senha acertada!")
#          break
#      else:
#          print("senha errada. Tente d novo")





# # 42 
# codigo = "1234"
# tentativas = 0
# while True:
#    pin = input("digite seu PIN: ")
   
#    if pin == codigo:
#       print("PIN correto incerido!")
#       break
#    else:
#     tentativas += 1
#     print("Incorreto...tente novamente")

# print(f"Você tentou {tentativas} vzs... ")







# # 43
# ano = int(input("Digite um ano: "))
# def bissexto(ano):
#    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
#        return True
#    else:
#        return False
# Xbissexto = ano + 1
# while not bissexto(Xbissexto):
#    Xbissexto += 1
# print(f"O próximo ano bissexto é {Xbissexto}")





# # 44
# numero = 0
# while numero < 30:
#    print(numero)
#    numero += 2
# print("Execução finalizada")





# # 45
# print("Está pronto? ")
# num = int(input("Digite um numero: "))
# while True:
#     num = num - 1
#     if num == 0: 
#         break
#     print(num)
# print("agora!")






# # 46
# num = int(input("Digite um numero: "))
# if num > 1:
#    for i in range(1, num)
#      print(i)




# # 47
# num = int(input("Digite um numero como limite: "))
# numInicial = 1
# while numInicial <= num:
#    print(numInicial)
#    numInicial *= 2




# # 48
# num = int(input("Digite um numero como limite: "))
# base =  int(input("Digite a base q será multiplicada: "))
# numInicial = 1
# while numInicial <= num:
#    print(numInicial)
#    numInicial *= base





# # 49
# # duplicada com a 47




# # 50
# soma = 0
# while soma <=100:
#    num = int(input("Digite um numero: "))
#    soma += num
# print(f"A soma é {soma}")





# # 51
# import re
# def senha(senha):
#    if len(senha) < 8:
#       return False
#    if not re.search("[A-Z]", senha)
#       return False
#    if not re.search("[a-z]", senha)
#       return False
#    if not re.search("[0-9]", senha)
#       return False







# # 52
# import random
# numeroSecreto = random.randint(1,100)
# while True:
#    tent= int(input("Adivinhe o numero: "))
#    if tent < numeroSecreto:
#       print("O número secreto é maior do que seu numero")
#    elif tent > numeroSecreto:
#       print("O número secreto é menor do que seu numero")
#    else:
#       print("Adivinhou parabens")
#       break




# # 53
# saldo = 1000
# def validez(valor, saldo):
#     if valor % 10 != 0:
#        print("O valor deve ser multiplo de 10")
#        return False
#     if valor > saldo:
#        print("O valor não está disponivel")
#        return False
#     return True
# while True:
#     try:
#         Valor = int(input("Digite o valor de saque: R$"))
#         if validez(Valor, saldo):
#          print(f"Saque de R${Valor} realizado com sucesso!")
#          break
#     except ValueError:
#        print("Plis, digite um valor válido")




# # 54
# while True:
#    palavra1 = input("Digite a primeira palavra: ")
#    palavra2 = input("Digite a segunda palavra: ")
#    if len(palavra1) == len(palavra2):
#        print("tem a mesma quantidade de letras")
#        break
#    else:
#       print("são diferentes a quantidade de letras das palavras, faz novamente")






# # 55
# palavra = str(input("Digite uma palavra com o numero de caracteres escolhidos: "))
# print("#"* len(palavra))


# # 56
# string = input("Digite uma string: ")
# while len(string) != 0:
#    tracos = "-" * len(string)
#    print(string)
#    print(tracos)
#    string = input("Digite uma string: ")


# # 57
# string = input("Digite uma string: ")
# string20 = string.rjust(20, "*")
# print(string20)




# # 58
# text1 = input("Digite uma string: ")
# text2 = ""
# Xtext = text2.rjust(30, "*")
# print(Xtext)
# print(text1)
# print(Xtext)









# # Exemplo:
# while True: # Inicia um loop infinito
#    num = int(input("Por favor, digite um número: ")) # Solicita ao usuário para digitar um número
#    if num == -1: # Verifica se o númerp digitado é -1
#       break # Se for -1, interrompe o loop
#    while num > 0: # Continua o loop enquanto o número for maior que 0
#       print(num) # Imprime o número
#       num -= 1 # Decrementa o número em 1




# # ex:
# def menssagem():
#    print("Essa é minha função")

   
# def menssagem():
#    print("Essa é minha própria função")
# menssagem()   



# # Exercício:
# def seteIrmaos():
#    print("Alex")
#    print("Belkis")
#    print("Camila")
#    print("Daniela")
#    print("Edgar")
#    print("Francis")
#    print("Gustavo")

# seteIrmaos()
  









# # Exercício 1:
# def media(num1, num2, num3):
 
#    print(f"A média aritmética é {(num1 + num2 + num3) / 3}")
 

# media(2,3,5)
  





# # Exercício 2:
# def printaVariasVezes(texto, vzs):
 
#    print(f"{texto * (vzs)}")
 

# printaVariasVezes("laalalalla", 10)
  


# Exercício 3:

# def quadradoHashtag(tamanho):
#    contador = 1
#    while True:
#       print('#'* tamanho)
#       if contador == tamanho:
#          break
#       contador += 1

# quadradoHashtag(5)
  



# # Exercício 4:
# def mesaXadrez(tamanho):
#    x = 0
#    while x < tamanho:
#       y = 0
#       while y < tamanho:
#          if(x + y) % 2 == 0:
#             print('1', end = ' ')
#          else:
#             print('0', end = ' ')
#          y += 1
#       print()
#       x += 1         
# mesaXadrez(9)











# # Exercício 5:
# def quadradoString(string, inteiro):
#    x = 0
#    while x < inteiro:
#       y = 0
#       while y < inteiro:
#          if(x + y) % 2 == 0:
#             print('1', end = ' ')
#          else:
#             print('0', end = ' ')
#          y += 1
#       print()
#       x += 1         
# quadradoString()






# # Exercício 6:









# # Exemplo:
# def cumprimentar(nome):
#   print("Olá,", nome) 
# def cumprimentarVariasVezes(nome, vezes):
#       while vezes < 0:
#         cumprimentar(nome) 
#         vezes -= 1
# cumprimentarVariasVezes("Elsa", 9)



                               
# # Exercício 7:













































# # Recebe uma lista como parametro
# showTamanhos = [45, 44, 36, 39, 40]
# def mediana(minhaLista: list):
#    ordenada = sorted(minhaLista)
#    centroLista = len(ordenada) // 2
#    return ordenada[centroLista]
   
# print("A mediana é", mediana(showTamanhos))

# idades =[1, 56, 34, 22, 5, 77, 5]
# print("A mediana das idades é", mediana(idades))








# # retorna uma lista
# def entradaNumeros():
#    numeros = []
#    while True:
#       entradaUsuario = input("Por favor, digite um número inteiro, deixe em branco para sair: ")
#       if len(entradaUsuario) == 0:
#          break
#       numeros.append(int(entradaUsuario))
#    return numeros






# minhaLista = [3, 2, 4, 5, 2]
# for item in minhaLista:
#    print(item)





# minha_lista = "python"

# for item in minha_lista:
#    print(f"{item} * ", end = "")











# for i in range(5):
#     print(i)




# for i in range(3, 7):
#    print(i)








# for i in range(1, 9, 2):
#     print(i)




# for i in range(6, 2, -1):
#    print(i)








# numeros = list(range(2, 7))
# print(numeros)





# Atividade 4:
def lista_estrelas(lista):
    for numero in lista:
        print('*' * numero)

lista_estrelas([3, 5, 2, 1, 9])











# # # Atividade 5:
# # def lista
# # return sorted
# # print(anagramas("tame", "meta")) # Verdadeiro
# # print(anagramas("tame", "mate")) # Verdadeiro
# # print(anagramas("tame", "team")) # Verdadeiro
# # print(anagramas("tabby", "batty")) # Falso
# # print(anagramas("python", "java")) # Falso
















# minhaString = "Quantas madeiras um esquilo poderia empilhar se um esquilo pudesse empilhar madeira"
# print(minhaString.count("ma"))

# minha_lista = [1, 2, 3, 1, 4, 5, 1, 6]
# print(minha_lista.count(1))



# minhaString = "Oi"
# novaString = minhaString.replace("Oi", "Olá")
# print(novaString)










# # Atividade 9:
# def sem_vogal(text):
#    vogais = ["a", "e", "i", "o", "u"]
#    for i in text:
#       if vogais.count(1) == 0:
#          print(1, end='')

# sem_vogal("Lalalala")






# minha_lista = [[1,2,3][4,5,6][7,8,9]]
# print(minha_lista)
# print(minha_lista[1])
# print(minha_lista[1][0])





# minhaMatriz = [[1,2,3][3,2,1][4,5,6]]
# print(minhaMatriz[0][1])
# minhaMatriz[1][0] = 10 
# print(minhaMatriz)




# # Atividade :
# pessoas = [["Betty", 10, 1.37],["Pedro", 7, 1.25]["Emily", 32, 1.35]]

# for pessoa in pessoas:
#    nome = pessoas[0]
#    idade = pessoas[1]
#    altura = pessoas[2]





# # Atividade 10:
# def jogue_o_jogo(mesa: list, x: int, y: int, caracter: str):
#    if not (0 <= x <= 2 and 0 <= y <= 2):
#      if caracter not in ['X', 'O']:
#       if mesa[x][y] != ' ':
#        mesa[x][y] = caracter
# mesa = [['O', 'X', 'O'], ['O', 'O', 'X'],['X', 'X', 'O']]


# jogue_o_jogo(mesa, 1, 1, 'X')
# for linha in mesa:
#     print(linha)








meu_dicionario = {}
meu_dicionario["apina"] = "macaco"
meu_dicionario["banaani"] = "banana"
meu_dicionario["cembalo"] = "cravo"
print(meu_dicionario)
print(meu_dicionario["apina"])
palavra = input("Por favor, digite uma palavra: ")
if palavra in meu_dicionario:
   print("Tradução: ", meu_dicionario[palavra])
else:
   print("Palavra não encontrada") 




resultados = {}
resultados["Mary"] = 4
resultados["Alice"] = 5
resultados["Larry"] = 2

lists = {}
lists[5] = [1, 2 ,3]
lists[42] = [5, 4, 5, 4, 5]
lists[100] = [5, 2 ,3]









meu_dicionario = {}

meu_dicionario["apina"] = "macaco"
meu_dicionario["banaani"] = "banana"
meu_dicionario["cembalo"] = "cravo"

for chave in meu_dicionario:
    print("chave:", chave)
    print("valor:", meu_dicionario[chave])











lista_palavras = [
  "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
  "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
  "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
]

def contagens(minha_lista):
    palavras = {}
    for palavra in minha_lista:
      #   se a palavra ainda não está no dicionário, inicialize o valor como zero
        if palavra not in palavras:
            palavras[palavra] = 0
            # incrementa o valor
        palavras[palavra] += 1
        return palavras
   #  chama a função
    print(contagens(lista_palavras))    









# import random

# numeroSecreto = random.randint(1,100)

# print(numeroSecreto)






# import re

# print(re.search("[A-Z]", "Senha"))
# print(re.search("[a-z]", "Senha"))
# print(re.search("[0-9]", "Senha"))




# import random

# numeroSecreto = random.randint(1,100)

# print(numeroSecreto)



















# numero = int(input("entre com um número: "))

# if numero < 0:
#     print("esse número é negativo")
# if numero > 0:
#     print("esse número é positivo")
# if numero == 0:
#     print("O número é 0")










# numero = int(input("Digite um número inteiro: "))
# if numero == 1984:
#   print("Digitou o número 1984 Orwall")
  





















































# tentativas = 0
# while True:
#    codigo = input("Por favor, digite seu PIN: ")
#    tentativas += 1
#    if codigo == "1234":
#       sucesso = True
#       break
#    if tentativas == 3:
#        sucesso = False
#        break
#    print("Incorreto...tente novamente")
# if sucesso:
#    print("PIN correto incerido!")
# else:
#    print("muitas tentativas... ")











