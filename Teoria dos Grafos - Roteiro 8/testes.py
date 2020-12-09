from grafo_test import Grafo


g_1 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

g_1.adicionaAresta('A-B',4)
g_1.adicionaAresta('B-C',3)
g_1.adicionaAresta('C-D',4)
g_1.adicionaAresta('D-E',3)
g_1.adicionaAresta('E-F',19)
g_1.adicionaAresta('F-G',1)
g_1.adicionaAresta('G-E',2)
g_1.adicionaAresta('E-C',5)
g_1.adicionaAresta('C-A',9)

g_D1 = Grafo([], [])
for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g']:
    g_D1.adicionaVertice(i)
for i in ['A-B', 'A-M', 'A-L', 'B-C', 'B-D', 'C-V', 'V-B', 'D-E', 'E-F', 'E-X', 'F-G', 'G-g', 'G-H', 'H-I', 'I-J',
          'J-K', 'J-a', 'K-a', 'M-N', 'N-W', 'N-V', 'N-P', 'V-W', 'W-D', 'W-U', 'U-Y', 'U-T', 'U-X', 'X-Y', 'X-c',
          'c-d', 'c-b', 'd-e', 'd-J', 'e-X', 'Y-Z', 'Y-F', 'Z-e', 'Z-f', 'Z-g', 'L-M', 'L-O', 'O-N', 'O-Q', 'Q-S',
          'S-T', 'T-X', 'P-R', 'R-X']:
    g_D1.adicionaAresta(i)

g_prim = Grafo([],[])
for i in ['a','b','c','d','e','f','g','h']:
    g_prim.adicionaVertice(i)
for i in [['a-h',5],['a-b',17],['a-e',14],['b-g',18],['b-h',13],['c-e',20],['c-f',2],['d-g',8],['d-e',19],['f-g',1],['f-h',13],['g-e',12]]:
    g_prim.adicionaAresta(i[0],i[1])

g_mprim = Grafo([],[])
for i in ['a','b','c','d','e','f','g','h']:
    g_mprim.adicionaVertice(i)
for i in [['a-b',9],['a-g',4],['b-c',6],['b-g',10],['b-h',7],['c-d',8],['c-e',12],['c-f',8],['d-e',14],['e-f',2],['f-h',2],['f-g',1]]:
    g_mprim.adicionaAresta(i[0],i[1])

g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p.adicionaAresta('J-C', 3)
g_p.adicionaAresta('C-E', 1)
g_p.adicionaAresta('C-E', 1)
g_p.adicionaAresta('C-P', 2)
g_p.adicionaAresta('C-P', 2)
g_p.adicionaAresta('C-M', 3)
g_p.adicionaAresta('C-T', 3)
g_p.adicionaAresta('M-T', 2)
g_p.adicionaAresta('T-Z', 2)

# Grafos completos

g_c = Grafo(['J', 'C', 'E', 'P'])
g_c.adicionaAresta('J-C', 2)
g_c.adicionaAresta('J-E', 3)
g_c.adicionaAresta('J-P', 5)
g_c.adicionaAresta('C-E', 7)
g_c.adicionaAresta('C-P', 2)
g_c.adicionaAresta('E-P', 1)

g_c3 = Grafo(['J'])

# Grafos com laco
# self.g_l1 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-A', 'a2':'B-A', 'a3':'A-A'})
g_l1 = Grafo(['A', 'B', 'C', 'D'])
g_l1.adicionaAresta('A-A', 1)
g_l1.adicionaAresta('A-A', 1)
g_l1.adicionaAresta('B-A', 3)
# self.g_l2 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-B', 'a2':'B-B', 'a3':'B-A'})
g_l2 = Grafo(['A', 'B', 'C', 'D'])
g_l2.adicionaAresta('A-B', 1)
g_l2.adicionaAresta('B-B', 1)
g_l2.adicionaAresta('B-A', 1)

# self.g_l3 = Grafo(['A', 'B', 'C', 'D'], {'a1':'C-A', 'a2':'C-C', 'a3':'D-D'})
g_l3 = Grafo(['A', 'B', 'C', 'D'])
g_l3.adicionaAresta('C-A', 1)
g_l3.adicionaAresta('C-C', 1)
g_l3.adicionaAresta('D-D', 1)


# Grafos criados por nós

g_1 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

g_1.adicionaAresta('A-B', 2)
g_1.adicionaAresta('B-C', 6)
g_1.adicionaAresta('C-D', 2)
g_1.adicionaAresta('D-E', 1)
g_1.adicionaAresta('E-F', 4)
g_1.adicionaAresta('F-G', 1)
g_1.adicionaAresta('G-E', 8)
g_1.adicionaAresta('E-C', 4)
g_1.adicionaAresta('C-A', 2)

g_2 = Grafo(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

g_2.adicionaAresta('1-2', 2)
g_2.adicionaAresta('1-5', 4)
g_2.adicionaAresta('1-4', 2)
g_2.adicionaAresta('4-5', 1)
g_2.adicionaAresta('5-2', 9)
g_2.adicionaAresta('2-3', 2)
g_2.adicionaAresta('3-9', 6)
g_2.adicionaAresta('6-8', 4)
g_2.adicionaAresta('8-7', 2)
g_2.adicionaAresta('7-6', 1)

g_3 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

g_3.adicionaAresta('A-C', 5)
g_3.adicionaAresta('B-D', 7)
g_3.adicionaAresta('A-B', 4)
g_3.adicionaAresta('B-E', 1)
g_3.adicionaAresta('C-E', 2)
g_3.adicionaAresta('C-F', 5)
g_3.adicionaAresta('D-E', 3)
g_3.adicionaAresta('E-F', 7)
g_3.adicionaAresta('B-C', 2)

g_4 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

g_4.adicionaAresta('A-D', 3)
g_4.adicionaAresta('A-B', 1)
g_4.adicionaAresta('C-A', 4)
g_4.adicionaAresta('C-F', 5)
g_4.adicionaAresta('C-D', 8)
g_4.adicionaAresta('D-F', 5)
g_4.adicionaAresta('B-D', 5)
g_4.adicionaAresta('E-A', 2)
g_4.adicionaAresta('E-C', 1)

g_5 = Grafo(['A', 'B', 'C', 'D', 'E'])

g_5.adicionaAresta('A-B', 7)
g_5.adicionaAresta('A-C', 5)
g_5.adicionaAresta('A-D', 2)
g_5.adicionaAresta('C-D', 1)
g_5.adicionaAresta('B-D', 1)
g_5.adicionaAresta('B-E', 2)
g_5.adicionaAresta('D-E', 3)

g_7 = Grafo(['A', 'B', 'C', 'D', 'E'])

g_7.adicionaAresta('A-B', 3)
g_7.adicionaAresta('A-C', 2)
g_7.adicionaAresta('A-D', 1)
g_7.adicionaAresta('B-D', 3)
g_7.adicionaAresta('D-C', 6)
g_7.adicionaAresta('B-E', 7)
g_7.adicionaAresta('C-E', 1)

# Grafos Dijkstra
g_8 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'])

g_8.adicionaAresta('A-B', 2)
g_8.adicionaAresta('B-D', 5)
g_8.adicionaAresta('D-E', 2)
g_8.adicionaAresta('E-C', 4)
g_8.adicionaAresta('C-A', 10)
g_8.adicionaAresta('A-T', 2)
g_8.adicionaAresta('B-P', 1)
g_8.adicionaAresta('D-F', 8)
g_8.adicionaAresta('E-G', 5)
g_8.adicionaAresta('C-Q', 2)
g_8.adicionaAresta('T-R', 3)
g_8.adicionaAresta('R-P', 6)
g_8.adicionaAresta('P-J', 4)
g_8.adicionaAresta('J-F', 6)
g_8.adicionaAresta('F-H', 2)
g_8.adicionaAresta('H-G', 9)
g_8.adicionaAresta('G-K', 1)
g_8.adicionaAresta('K-Q', 5)
g_8.adicionaAresta('Q-S', 2)
g_8.adicionaAresta('S-T', 3)
g_8.adicionaAresta('R-O', 8)
g_8.adicionaAresta('J-M', 1)
g_8.adicionaAresta('H-I', 1)
g_8.adicionaAresta('K-L', 5)
g_8.adicionaAresta('S-N', 4)
g_8.adicionaAresta('M-O', 2)
g_8.adicionaAresta('O-N', 5)
g_8.adicionaAresta('N-L', 9)
g_8.adicionaAresta('L-I', 7)
g_8.adicionaAresta('I-M', 2)

g_10 = Grafo(['A', 'U', 'D', 'I', 'E', 'F', 'O', 'H', 'S', 'M', 'L', 'K', 'N'])

g_10.adicionaAresta('A-U', 1)
g_10.adicionaAresta('A-D', 2)
g_10.adicionaAresta('U-D', 4)
g_10.adicionaAresta('U-N', 2)
g_10.adicionaAresta('D-K', 1)
g_10.adicionaAresta('A-E', 2)
g_10.adicionaAresta('I-E', 2)
g_10.adicionaAresta('E-F', 5)
g_10.adicionaAresta('F-K', 1)
g_10.adicionaAresta('F-H', 1)
g_10.adicionaAresta('F-O', 3)
g_10.adicionaAresta('O-H', 2)
g_10.adicionaAresta('H-S', 1)
g_10.adicionaAresta('H-M', 3)
g_10.adicionaAresta('K-L', 1)
g_10.adicionaAresta('L-M', 4)
g_10.adicionaAresta('N-M', 2)
g_10.adicionaAresta('K-H', 2)
g_10.adicionaAresta('I-S', 9)

print(g_mprim.prim())
print(g_2.prim())
print(g_3.prim())
print(g_4.prim())
print(g_5.prim())
print(g_7.prim())
print(g_8.prim())
print(g_10.prim())










