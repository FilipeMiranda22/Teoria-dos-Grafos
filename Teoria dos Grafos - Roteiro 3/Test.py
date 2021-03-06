from grafo import Grafo
from Casos import TestGrafo
g1 = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})#grafo da paraiba
g2 = Grafo(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'], {'1': 'A-B', '2': 'A-G', '3': 'A-J', '4': 'G-K', '5': 'J-K', '6': 'G-J', '7': 'J-I', '8': 'G-I', '9': 'G-H', '10': 'H-F', '11': 'F-B', '12': 'B-G', '13': 'B-C', '14': 'C-D', '15': 'D-E', '16': 'D-B', '17': 'E-B'})#grafo roteiro 2
g3 = Grafo(['A', 'B', 'C'], {'1': 'A-B', '2': 'B-B', '3': 'B-C', '4': 'C-A'}) # Triangulo com laço
g4 = Grafo(['A', 'B', 'C'], {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-A'}) # Triangulo
g5 = Grafo(['A', 'B', 'C', 'D'], {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-A'}) # Triangulo com um vértice isolado (Não conexo)
g6 = Grafo(['A', 'B', 'C', 'D', 'E'], {'a1': 'A-D', 'a2': 'A-E', 'a3': 'B-D', 'a4': 'B-E', 'a5': 'C-D', 'a6': 'C-E'}) #Grafo bijetor 3/2
g7 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'], {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-D', 'a4': 'D-E', 'a5': 'E-C', 'a6': 'C-A', 'a7': 'B-G', 'a8': 'G-F', 'a9': 'G-F'})#grafo normal
g8 = Grafo(['AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG'], {'a1': 'AAA-BBB', 'a2': 'BBB-CCC', 'a3': 'BBB-DDD', 'a4': 'AAA-EEE', 'a5': 'EEE-FFF', 'a6': 'EEE-GGG'}) #grafo 3 vertices
g9 = Grafo(['V1','V2','V3','V4','V5'], {'a1': 'V1-V2','a2': 'V1-V3','a3': 'V1-V3','a4': 'V2-V3','a5': 'V2-V5','a6': 'V5-V5','a7': 'V5-V3','a8': 'V3-V4'}) #grafo com paralelos
g11 = Grafo(['A'], {'1': 'A-A'}) # Grafo com 1 só vertice, que em laço
g12 = Grafo(['H','J','K','L'], {'1': 'H-K','2': 'H-J','3': 'J-L','4': 'L-H','5': 'L-K'})
g13 = Grafo(['V1','V2','V3','V4'], {'a1': 'V1-V2','a2': 'V2-V3','a3': 'V3-V4','a4': 'V4-V1','a5': 'V1-V3','a6': 'V2-V4'})#k4
g14 = Grafo(['V1','V2','V3','V4','V5'], {'a1': 'V1-V2','a2': 'V2-V3','a3': 'V3-V4','a4': 'V4-V5','a5': 'V5-V1','a7': 'V1-V3','a8': 'V1-V4','a9': 'V2-V5','a10': 'V2-V4','a6': 'V5-V3'})#k5
g15 = Grafo(['A', 'B', 'C','D'], {'a0':'D-A','a1': 'A-B', 'a2': 'B-C', 'a3': 'C-A'})#Triangulo com uma ponta
g16 = Grafo(['A', 'B', 'C','D','E','F'], {'a0':'D-A','a1': 'A-B', 'a2': 'B-C', 'a3': 'C-A','a4': 'D-E','a5': 'D-F'})# Triangulo com 2 pontas
g17 = Grafo(['A', 'B','C'], {'a1':'A-B','a2': 'A-B','a3': 'A-C','a4': 'A-C'})#Grafo somente com paralelas
g18 = Grafo(('A','B','C'),{'a1':'A-B','a2': 'A-C'})#Arvore simples
g19 = Grafo(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'),
            {'a1': 'A-B', 'a2': 'A-C', 'a3': 'D-E', 'a4': 'E-F', 'a5': 'F-G', 'a6': 'G-D',
             'a7': 'A-H'})  # NÃO CONEXO COM CICLO EM UM SUB GRAFO
g20 = Grafo(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'),
            {'a1': 'A-B', 'a2': 'A-C', 'a3': 'D-E', 'a4': 'E-F', 'a5': 'F-G', 'a7': 'A-H', 'a8': 'I-J', 'a9': 'J-K',
             'a10': 'K-I'})  # NÃO CONEXO EM 2 SUBGRAFOS E COM CICLO EM UM SUB GRAFO


print("Grafo 1", g1.caminho(4))
print("Grafo 2", g2.caminho(6))
print("Grafo 3", g3.caminho(3))
print("Grafo 4", g4.caminho(2))
print("Grafo 5", g5.caminho(1))
print("Grafo 6", g6.caminho(4))
print("Grafo 7", g7.caminho(5))
print("Grafo 8", g8.caminho(1))
print("Grafo 9", g9.caminho(3))
print("Grafo 11", g11.caminho(9))
print("Grafo 12", g12.caminho(3))
print("Grafo 13", g13.caminho(1))
print("Grafo 14", g14.caminho(0))
print('='*70)
print("Grafo 1", g1.ha_ciclo())
print("Grafo 2", g2.ha_ciclo())
print("Grafo 3", g3.ha_ciclo())
print("Grafo 11", g11.ha_ciclo())
print("Grafo 6", g6.ha_ciclo())
print("Grafo 13", g13.ha_ciclo())
print("="*70)
print(g18.caminho(2))








