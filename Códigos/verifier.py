# Exemplo de entrada:

# M é um grafo representado por uma matriz de adjacência:

# [[0, 1, 1, 1, 0], 
# [1, 0, 1, 0, 0], 
# [1, 1, 0, 0, 0], 
# [1, 0, 0, 0, 1], 
# [0, 0, 0, 1, 0]]

# k é um número inteiro positivo que representa o tamanho do clique

# 3

# certificado é um conjunto de vértices

# [0, 1, 2]

def verifiesClique(M, k, certificado):

    c = len(certificado)

    if k > c:
        return False
    else:

        for i in range(0, len(certificado) - 1):

            for j in range(i + 1, len(certificado)):

                if(M[certificado[i]][certificado[j]] == 0):

                    return False

    return True




result = verifiesClique([[0, 1, 1, 1, 0], 
                        [1, 0, 1, 0, 0], 
                        [1, 1, 0, 0, 0],
                        [1, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0]], 3, [1, 2, 0])