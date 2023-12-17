def satToClique(satInstance):
    
    # cada literal é um vértice
    matrix = [[0] * len(satInstance[0]) * 3 for _ in range(len(satInstance) * 3)]
    
    # k é o número de cláusulas
    k = len(satInstance)
    
    for i in range(len(satInstance) - 1):
        
        for j in range(i + 1, len(satInstance)):
            
            for k in range(0, 3):
                
                for l in range(0, 3):
                    
                    if ((satInstance[i][k][0] != satInstance[j][l][0])
                    
                    or ((satInstance[i][k][1] == satInstance[j][l][1]) and (satInstance[i][k][0] == satInstance[j][l][0]))
                    
                    ):
                        
                        print(satInstance[i][k][0], satInstance[i][k][1], "entra no grafo", "conectado com",
                        satInstance[j][l][0] , satInstance[j][l][1])
                        
                        matrix[i][k] = 1
                        matrix[j][l] = 1

    return matrix, k