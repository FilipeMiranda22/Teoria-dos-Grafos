from grafo import Grafo
from Casos import TestGrafo
g1 = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})
g2 = Grafo(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'], {'1': 'A-B', '2': 'A-G', '3': 'A-J', '4': 'G-K', '5': 'J-K', '6': 'G-J', '7': 'J-I', '8': 'G-I', '9': 'G-H', '10': 'H-F', '11': 'F-B', '12': 'B-G', '13': 'B-C', '14': 'C-D', '15': 'D-E', '16': 'D-B', '17': 'E-B'})
g3 = Grafo(['A', 'B', 'C'], {'1': 'A-B', '2': 'B-B', '3': 'B-C', '4': 'C-A'}) # Triangulo com laço
g4 = Grafo(['A', 'B', 'C'], {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-A'}) # Triangulo
g5 = Grafo(['A', 'B', 'C', 'D'], {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-A'}) # Triangulo com um vértice isolado (Não conexo)
g6 = Grafo(['A', 'B', 'C', 'D', 'E'], {'a1': 'A-D', 'a2': 'A-E', 'a3': 'B-D', 'a4': 'B-E', 'a5': 'C-D', 'a6': 'C-E'}) #Grafo bijetor 3/2
g7 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'], {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-D', 'a4': 'D-E', 'a5': 'E-C', 'a6': 'C-A', 'a7': 'B-G', 'a8': 'G-F', 'a9': 'G-F'})
g8 = Grafo(['AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF', 'GGG'], {'a1': 'AAA-BBB', 'a2': 'BBB-CCC', 'a3': 'BBB-DDD', 'a4': 'AAA-EEE', 'a5': 'EEE-FFF', 'a6': 'EEE-GGG'})


print("Grafo 1", g1.dfs('J'))
print("Grafo 2", g2.dfs('K'))
print("Grafo 3", g3.dfs('A'))
print("Grafo 4", g4.dfs('C'))
print("Grafo 5", g5.dfs('A'))
print("Grafo 6", g6.dfs('A'))
print("Grafo 7", g7.dfs('A'))
print("Grafo 8", g8.dfs('EEE'))




