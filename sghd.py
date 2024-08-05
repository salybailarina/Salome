import random

def criar_tabuleiro():
    
    return [[0] * 9 for _ in range(9)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(str(num) if num != 0 else '.' for num in linha))
    

def pode_colocar(tabuleiro, linha, coluna, numero):
    """ Verifica se é possível colocar um número na posição especificada """
    # Verifica a linha
    if numero in tabuleiro[linha]:
        return False
    
    # Verifica a coluna
    for i in range(9):
        if tabuleiro[i][coluna] == numero:
            return False
    
    return True

def fazer_movimento(tabuleiro, linha, coluna, numero):
    """ Tenta fazer um movimento no tabuleiro """
    if pode_colocar(tabuleiro, linha, coluna, numero):
        tabuleiro[linha][coluna] = numero
        return True
    return False

def preencher_linha(tabuleiro, linha):
    """ Preenche automaticamente uma linha com números válidos """
    for coluna in range(9):
        if tabuleiro[linha][coluna] == 0:
            numero = random.randint(1, 9)
            while not pode_colocar(tabuleiro, linha, coluna, numero):
                numero = random.randint(1, 9)
            tabuleiro[linha][coluna] = numero

def preencher_coluna(tabuleiro, coluna):
    """ Preenche automaticamente uma coluna com números válidos """
    for linha in range(9):
        if tabuleiro[linha][coluna] == 0:
            numero = random.randint(1, 9)
            while not pode_colocar(tabuleiro, linha, coluna, numero):
                numero = random.randint(1, 9)
            tabuleiro[linha][coluna] = numero

def preencher_subgrade(tabuleiro, linha_inicio, coluna_inicio):
    """ Preenche automaticamente uma subgrade (3x3) com números válidos """
    for linha in range(linha_inicio, linha_inicio + 3):
        for coluna in range(coluna_inicio, coluna_inicio + 3):
            if tabuleiro[linha][coluna] == 0:
                numero = random.randint(1, 9)
                while not pode_colocar(tabuleiro, linha, coluna, numero):
                    numero = random.randint(1, 9)
                tabuleiro[linha][coluna] = numero

def limpar_tabuleiro(tabuleiro):
    """ Limpa o tabuleiro """
    for linha in range(9):
        for coluna in range(9):
            tabuleiro[linha][coluna] = 0

def preencher_com_predefinidos(tabuleiro):
    """ Preenche o tabuleiro com números predefinidos """
    predefinidos = [
        (0, 0, 5), (0, 1, 3), (0, 4, 7),
        (1, 0, 6), (1, 3, 1), (1, 4, 9), (1, 5, 5),
        (2, 1, 9), (2, 2, 8), (2, 7, 6),
        (3, 0, 8), (3, 4, 6), (3, 8, 3),
        (4, 0, 4), (4, 3, 8), (4, 5, 3), (4, 8, 1),
        (5, 0, 7), (5, 4, 2), (5, 8, 6),
        (6, 1, 6), (6, 6, 2), (6, 7, 8),
        (7, 3, 4), (7, 4, 1), (7, 5, 9), (7, 8, 5),
        (8, 4, 8), (8, 7, 7), (8, 8, 9)
    ]
    for linha, coluna, numero in predefinidos:
        tabuleiro[linha][coluna] = numero

def jogo_sudoku():
    """ Função principal para jogar o Sudoku """
    tabuleiro = criar_tabuleiro()
    preencher_com_predefinidos(tabuleiro)
    
    while True:
        imprimir_tabuleiro(tabuleiro)
        try:
            acao = input("Escolha uma ação: Adicionar (a), Preencher Linha (l), Preencher Coluna (c), Preencher Subgrade (s), Limpar (t) ou Sair (e): ").strip().lower()

            if acao == 'a':
                linha = int(input("Digite a linha (0-8): "))
                coluna = int(input("Digite a coluna (0-8): "))
                numero = int(input("Digite o número (1-9): "))
                
                if 0 <= linha < 9 and 0 <= coluna < 9 and 1 <= numero <= 9:
                    if fazer_movimento(tabuleiro, linha, coluna, numero):
                        print("Número adicionado com sucesso!")
                    else:
                        print("Número não pode ser colocado aqui.")
                else:
                    print("Entrada inválida. Tente novamente.")
            
            elif acao == 'l':
                linha = int(input("Digite a linha (0-8) para preencher: "))
                if 0 <= linha < 9:
                    preencher_linha(tabuleiro, linha)
                    print("Linha preenchida com sucesso!")
                else:
                    print("Linha inválida. Tente novamente.")
            
            elif acao == 'c':
                coluna = int(input("Digite a coluna (0-8) para preencher: "))
                if 0 <= coluna < 9:
                    preencher_coluna(tabuleiro, coluna)
                    print("Coluna preenchida com sucesso!")
                else:
                    print("Coluna inválida. Tente novamente.")
            
            elif acao == 's':
                linha_inicio = int(input("Digite a linha inicial da subgrade (0, 3, 6): "))
                coluna_inicio = int(input("Digite a coluna inicial da subgrade (0, 3, 6): "))
                if linha_inicio in (0, 3, 6) and coluna_inicio in (0, 3, 6):
                    preencher_subgrade(tabuleiro, linha_inicio, coluna_inicio)
                    print("Subgrade preenchida com sucesso!")
                else:
                    print("Posição inválida. Deve ser 0, 3 ou 6.")
            
            elif acao == 't':
                limpar_tabuleiro(tabuleiro)
                print("Tabuleiro limpo com sucesso!")
            
            elif acao == 'e':
                print("Saindo do jogo.")
                break
            
            else:
                print("Opção inválida. Escolha uma ação válida.")
        
        except ValueError:
            print("Entrada inválida. Use números inteiros.")

# Iniciar o jogo de Sudoku
jogo_sudoku()

