# Exemplo de entrada:

# A fórmula booleana (x1 + x2 + !x3) . (!x1 + !x2 + x4) . (x2 + x3 + !x4)
# seria representada desta forma:

#    [
    
#    [["x1", True], ["x2", True], ["x3", False]],
    
#    [["x1", False], ["x2", False], ["x4", True]],
    
#    [["x2", True], ["x3", True], ["x4", False]]
    
#    ]

# Os elementos da lista são as cláusulas;
# Os elementos que compõem as cláusulas são os literais;
# Os elementos que compõem os literais são seus nomes e seus valores.

def satToClique(satInstance):
    
    # Cada literal é um vértice:
    matrix = [[0] * len(satInstance[0]) * 3 for _ in range(len(satInstance) * 3)]
    
    # k é o número de cláusulas:
    k = len(satInstance)
    
    for i in range(len(satInstance) - 1):
        
        for j in range(i + 1, len(satInstance)):
            
            # Percore os elementos das cláusulas i
            for k in range(0, 3):
                
                # Percore os elementos das cláusulas j
                for l in range(0, 3):
                    
                    # Se os nomes dos literais são diferentes:
                    if ((satInstance[i][k][0] != satInstance[j][l][0])
                    
                    # Se os nomes dos literais são iguais e se os seus valores são iguais, isto é,
                    # se o valor de um literal de mesmo nome não é o complemento do outro:
                    or ((satInstance[i][k][1] == satInstance[j][l][1]) and (satInstance[i][k][0] == satInstance[j][l][0]))
                    
                    ):
                        
                        print(satInstance[i][k][0], satInstance[i][k][1], "entra no grafo", "conectado com",
                        satInstance[j][l][0] , satInstance[j][l][1])
                        
                        # Preenche a matriz
                        matrix[i][k] = 1
                        matrix[j][l] = 1

    return matrix, k