tabuleiro = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def pode_colocar(tabuleiro, linha, coluna, numero):
    # Verificar linha
    if numero in tabuleiro[linha]:
        return False
    
    # Verificar coluna
    for i in range(9):
        if tabuleiro[i][coluna] == numero:
            return False
    
    # Verificar quadrado 3x3
    inicio_linha = (linha // 3) * 3
    inicio_coluna = (coluna // 3) * 3
    for i in range(inicio_linha, inicio_linha + 3):
        for j in range(inicio_coluna, inicio_coluna + 3):
            if tabuleiro[i][j] == numero:
                return False
    
    return True




def resolver(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:  # Se a caixinha estiver vazia
                for numero in range(1, 10):  # Tentando números de 1 a 9
                    if pode_colocar(tabuleiro, linha, coluna, numero):
                        tabuleiro[linha][coluna] = numero
                        if resolver(tabuleiro):
                            return True
                        tabuleiro[linha][coluna] = 0  # Desfazer se não funcionar
                return False
    return True


resolver(tabuleiro)

for linha in tabuleiro:
    print(linha)
