import unittest
from grafo_adj_nao_dir import Grafo


class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('J-C', 3)
        self.g_p.adicionaAresta('C-E', 1)
        self.g_p.adicionaAresta('C-E', 1)
        self.g_p.adicionaAresta('C-P', 2)
        self.g_p.adicionaAresta('C-P', 2)
        self.g_p.adicionaAresta('C-M', 3)
        self.g_p.adicionaAresta('C-T', 3)
        self.g_p.adicionaAresta('M-T', 2)
        self.g_p.adicionaAresta('T-Z', 2)

        # Grafos completos

        self.g_c = Grafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('J-C', 2)
        self.g_c.adicionaAresta('J-E', 3)
        self.g_c.adicionaAresta('J-P', 5)
        self.g_c.adicionaAresta('C-E', 7)
        self.g_c.adicionaAresta('C-P', 2)
        self.g_c.adicionaAresta('E-P', 1)

        self.g_c3 = Grafo(['J'])

        # Grafos com laco
        # self.g_l1 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-A', 'a2':'B-A', 'a3':'A-A'})
        self.g_l1 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('A-A', 1)
        self.g_l1.adicionaAresta('A-A', 1)
        self.g_l1.adicionaAresta('B-A', 3)
        # self.g_l2 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-B', 'a2':'B-B', 'a3':'B-A'})
        self.g_l2 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('A-B', 1)
        self.g_l2.adicionaAresta('B-B', 1)
        self.g_l2.adicionaAresta('B-A', 1)

        # self.g_l3 = Grafo(['A', 'B', 'C', 'D'], {'a1':'C-A', 'a2':'C-C', 'a3':'D-D'})
        self.g_l3 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('C-A', 1)
        self.g_l3.adicionaAresta('C-C', 1)
        self.g_l3.adicionaAresta('D-D', 1)

        # Grafos criados por nós

        self.g_1 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

        self.g_1.adicionaAresta('A-B', 2)
        self.g_1.adicionaAresta('B-C', 6)
        self.g_1.adicionaAresta('C-D', 2)
        self.g_1.adicionaAresta('D-E', 1)
        self.g_1.adicionaAresta('E-F', 4)
        self.g_1.adicionaAresta('F-G', 1)
        self.g_1.adicionaAresta('G-E', 8)
        self.g_1.adicionaAresta('E-C', 4)
        self.g_1.adicionaAresta('C-A', 2)

        self.g_2 = Grafo(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

        self.g_2.adicionaAresta('1-2', 2)
        self.g_2.adicionaAresta('1-5', 4)
        self.g_2.adicionaAresta('1-4', 2)
        self.g_2.adicionaAresta('4-5', 1)
        self.g_2.adicionaAresta('5-2', 9)
        self.g_2.adicionaAresta('2-3', 2)
        self.g_2.adicionaAresta('3-9', 6)
        self.g_2.adicionaAresta('6-8', 4)
        self.g_2.adicionaAresta('8-7', 2)
        self.g_2.adicionaAresta('7-6', 1)

        self.g_3 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

        self.g_3.adicionaAresta('A-B', 4)
        self.g_3.adicionaAresta('A-C', 5)
        self.g_3.adicionaAresta('B-D', 7)
        self.g_3.adicionaAresta('B-E', 1)
        self.g_3.adicionaAresta('C-E', 2)
        self.g_3.adicionaAresta('C-F', 5)
        self.g_3.adicionaAresta('D-E', 3)
        self.g_3.adicionaAresta('E-F', 7)
        self.g_3.adicionaAresta('B-C', 2)

        self.g_4 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

        self.g_4.adicionaAresta('A-D', 3)
        self.g_4.adicionaAresta('A-B', 1)
        self.g_4.adicionaAresta('C-A', 4)
        self.g_4.adicionaAresta('C-F', 5)
        self.g_4.adicionaAresta('C-D', 8)
        self.g_4.adicionaAresta('D-F', 5)
        self.g_4.adicionaAresta('B-D', 5)
        self.g_4.adicionaAresta('E-A', 2)
        self.g_4.adicionaAresta('E-C', 1)

        self.g_5 = Grafo(['A', 'B', 'C', 'D', 'E'])

        self.g_5.adicionaAresta('A-B', 7)
        self.g_5.adicionaAresta('A-C', 5)
        self.g_5.adicionaAresta('A-D', 2)
        self.g_5.adicionaAresta('C-D', 1)
        self.g_5.adicionaAresta('B-D', 1)
        self.g_5.adicionaAresta('B-E', 2)
        self.g_5.adicionaAresta('D-E', 3)

        self.g_7 = Grafo(['A', 'B', 'C', 'D', 'E'])

        self.g_7.adicionaAresta('A-B', 3)
        self.g_7.adicionaAresta('A-C', 2)
        self.g_7.adicionaAresta('A-D', 1)
        self.g_7.adicionaAresta('B-D', 3)
        self.g_7.adicionaAresta('D-C', 6)
        self.g_7.adicionaAresta('B-E', 7)
        self.g_7.adicionaAresta('C-E', 1)

        # Grafos Dijkstra
        self.g_8 = Grafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'])

        self.g_8.adicionaAresta('A-B', 2)
        self.g_8.adicionaAresta('B-D', 5)
        self.g_8.adicionaAresta('D-E', 2)
        self.g_8.adicionaAresta('E-C', 4)
        self.g_8.adicionaAresta('C-A', 10)
        self.g_8.adicionaAresta('A-T', 2)
        self.g_8.adicionaAresta('B-P', 1)
        self.g_8.adicionaAresta('D-F', 8)
        self.g_8.adicionaAresta('E-G', 5)
        self.g_8.adicionaAresta('C-Q', 2)
        self.g_8.adicionaAresta('T-R', 3)
        self.g_8.adicionaAresta('R-P', 6)
        self.g_8.adicionaAresta('P-J', 4)
        self.g_8.adicionaAresta('J-F', 6)
        self.g_8.adicionaAresta('F-H', 2)
        self.g_8.adicionaAresta('H-G', 9)
        self.g_8.adicionaAresta('G-K', 1)
        self.g_8.adicionaAresta('K-Q', 5)
        self.g_8.adicionaAresta('Q-S', 2)
        self.g_8.adicionaAresta('S-T', 3)
        self.g_8.adicionaAresta('R-O', 8)
        self.g_8.adicionaAresta('J-M', 1)
        self.g_8.adicionaAresta('H-I', 1)
        self.g_8.adicionaAresta('K-L', 5)
        self.g_8.adicionaAresta('S-N', 4)
        self.g_8.adicionaAresta('M-O', 2)
        self.g_8.adicionaAresta('O-N', 5)
        self.g_8.adicionaAresta('N-L', 9)
        self.g_8.adicionaAresta('L-I', 7)
        self.g_8.adicionaAresta('I-M', 2)

        self.g_10 = Grafo(['A', 'U', 'D', 'I', 'E', 'F', 'O', 'H', 'S', 'M', 'L', 'K', 'N'])

        self.g_10.adicionaAresta('A-U', 1)
        self.g_10.adicionaAresta('A-D', 2)
        self.g_10.adicionaAresta('U-D', 4)
        self.g_10.adicionaAresta('U-N', 2)
        self.g_10.adicionaAresta('D-K', 1)
        self.g_10.adicionaAresta('A-E', 2)
        self.g_10.adicionaAresta('I-E', 2)
        self.g_10.adicionaAresta('E-F', 5)
        self.g_10.adicionaAresta('F-K', 1)
        self.g_10.adicionaAresta('F-H', 1)
        self.g_10.adicionaAresta('F-O', 3)
        self.g_10.adicionaAresta('O-H', 2)
        self.g_10.adicionaAresta('H-S', 1)
        self.g_10.adicionaAresta('H-M', 3)
        self.g_10.adicionaAresta('K-L', 1)
        self.g_10.adicionaAresta('L-M', 4)
        self.g_10.adicionaAresta('N-M', 2)
        self.g_10.adicionaAresta('K-H', 2)
        self.g_10.adicionaAresta('I-S', 9)

        self.g_mprim = Grafo([], [])
        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            self.g_mprim.adicionaVertice(i)
        for i in [['a-b', 9], ['a-g', 4], ['b-c', 6], ['b-g', 10], ['b-h', 7], ['c-d', 8], ['c-e', 12], ['c-f', 8],
                  ['d-e', 14], ['e-f', 2], ['f-h', 2], ['f-g', 1]]:
            self.g_mprim.adicionaAresta(i[0], i[1])

        # Grafos Dijkstra

        self.g_D1 = Grafo([], [])
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g']:
            self.g_D1.adicionaVertice(i)
        for i in ['A-B', 'A-M', 'A-L', 'B-C', 'B-D', 'C-V', 'V-B', 'D-E', 'E-F', 'E-X', 'F-G', 'G-g', 'G-H', 'H-I',
                  'I-J', 'J-K', 'J-a', 'K-a', 'M-N', 'N-W', 'N-V', 'N-P', 'V-W', 'W-D', 'W-U', 'U-Y', 'U-T', 'U-X',
                  'X-Y', 'X-c', 'c-d', 'c-b', 'd-e', 'd-J', 'e-X', 'Y-Z', 'Y-F', 'Z-e', 'Z-f', 'Z-g', 'L-M', 'L-O',
                  'O-N', 'O-Q', 'Q-S', 'S-T', 'T-X', 'P-R', 'R-X']:
            self.g_D1.adicionaAresta(i)


    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-E', 'E-P', 'E-M', 'E-T', 'E-Z',
                          'P-P', 'P-M', 'P-T', 'P-Z', 'M-M', 'M-Z', 'T-T', 'Z-Z'])

        self.assertEqual(self.g_c.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), ['J-J'])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta uma única vez por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 3)
        self.assertEqual(self.g_l2.grau('B'), 3)
        self.assertEqual(self.g_l4.grau('D'), 1)

    def test_arestas_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())


    def test_arestas_sobre_vertice(self):
        # {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T',
        # 'a9': 'T-Z'}
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['J-C']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')),
                         set(['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['C-M', 'M-T']))

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        # self.assertTrue((self.g_c2.eh_completo())) não existe referência.
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertTrue((self.g_l4.eh_completo()))
        self.assertTrue((self.g_l5.eh_completo()))

    def test_caminhoEuleriano(self):
        self.assertFalse(self.g_p.caminhoEuleriano())
        self.assertTrue(self.g_1.caminhoEuleriano())
        self.assertFalse(self.g_2.caminhoEuleriano())
        self.assertTrue(self.g_3.caminhoEuleriano())
        self.assertTrue(self.g_4.caminhoEuleriano())
        self.assertTrue(self.g_5.caminhoEuleriano())
        self.assertFalse(self.g_p_sem_paralelas.caminhoEuleriano())
        self.assertFalse(self.g_c.caminhoEuleriano())
        self.assertTrue(self.g_l1.caminhoEuleriano())
        self.assertFalse(self.g_l2.caminhoEuleriano())
        self.assertTrue(self.g_l3.caminhoEuleriano())
        self.assertFalse(self.g_8.caminhoEuleriano())


    def test_fleury(self):
        self.assertEqual(self.g_1.fleury(), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'E', 'C', 'A'])
        self.assertFalse(self.g_2.fleury())
        self.assertEqual(self.g_3.fleury(), ['A', 'B', 'C', 'E', 'D', 'B', 'E', 'F', 'C', 'A'])
        self.assertEqual(self.g_4.fleury(), ['B', 'A', 'C', 'D', 'F', 'C', 'E', 'A', 'D', 'B'])
        self.assertEqual(self.g_5.fleury(), ['A', 'B', 'D', 'C', 'A', 'D', 'E', 'B'])
        self.assertFalse(self.g_p.fleury())
        self.assertFalse(self.g_p_sem_paralelas.fleury())
        self.assertFalse(self.g_c.fleury())
        self.assertEqual(self.g_l1.fleury(), ['A', 'B'])
        self.assertFalse(self.g_l2.fleury())
        self.assertEqual(self.g_l3.fleury(), ['A'])
        self.assertFalse(self.g_8.fleury())

    def test_ciclo_hamiltoniano(self):
        self.assertFalse(self.g_1.ciclo_hamiltoniano())
        self.assertFalse(self.g_2.ciclo_hamiltoniano())
        self.assertEqual(self.g_3.ciclo_hamiltoniano(), ['A', 'B', 'D', 'E', 'F', 'C', 'A'])
        self.assertEqual(self.g_4.ciclo_hamiltoniano(), ['A', 'B', 'D', 'F', 'C', 'E', 'A'])
        self.assertEqual(self.g_5.ciclo_hamiltoniano(), ['A', 'B', 'E', 'D', 'C', 'A'])
        self.assertEqual(self.g_7.ciclo_hamiltoniano(), ['A', 'B', 'E', 'C', 'D', 'A'])
        self.assertEqual(self.g_c.ciclo_hamiltoniano(), ['J', 'C', 'E', 'P', 'J'])
        self.assertFalse(self.g_l1.ciclo_hamiltoniano())
        self.assertFalse(self.g_l2.ciclo_hamiltoniano())
        self.assertFalse(self.g_l3.ciclo_hamiltoniano())
        self.assertEqual(self.g_8.ciclo_hamiltoniano(), ['A', 'B', 'D', 'E', 'C', 'Q', 'K', 'G', 'H', 'F', 'J', 'P', 'R', 'O', 'M', 'I', 'L', 'N', 'S', 'T', 'A'])

    def test_dijkstra(self):
        self.assertEqual(self.g_D1.dijkstra('A', 'a', ['Q', 'X', 'G', 'I', 'J'], 3, 4),
                         ['A', 'L', 'O', 'Q', 'S', 'T', 'X', 'c', 'd', 'J', 'a'])
        self.assertEqual(self.g_D1.dijkstra('A', 'a', ['G', 'I'], 5, 5),
                         ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'a'])
        self.assertEqual(self.g_p.dijkstra('J', 'Z', ['M'], 2, 2), ['J', 'C', 'M', 'T', 'Z'])
        self.assertEqual(self.g_7.dijkstra('A', 'E', ['D'], 1, 2), ['A', 'D', 'B', 'E'])
        self.assertEqual(self.g_4.dijkstra('F', 'B', ['C'], 1, 2), ['F', 'C', 'A', 'B'])
        self.assertEqual(self.g_1.dijkstra('B', 'G', ['A', 'D'], 1, 2), ['B', 'A', 'C','D', 'E', 'G'])

    def test_prim(self):
        self.assertEqual(self.g_mprim.prim(), ([('g', 'f', 1), ('f', 'e', 2), ('f', 'h', 2), ('g', 'a', 4), ('h', 'b', 7), ('b', 'c', 6), ('c', 'd', 8)], 30)) #GRAFO DO EXEMPLO DO PDF
        self.assertEqual(self.g_p.prim(), ([('E', 'C', 2), ('C', 'J', 3), ('C', 'M', 3), ('M', 'T', 2), ('T', 'Z', 2), ('C', 'P', 4)], 16))
        self.assertEqual(self.g_1.prim(), ([('E', 'D', 1), ('D', 'C', 2), ('C', 'A', 2), ('A', 'B', 2), ('E', 'F', 4), ('F', 'G', 1)], 12))
        self.assertEqual(self.g_2.prim(), ([('5', '4', 1), ('4', '1', 2), ('1', '2', 2), ('2', '3', 2), ('3', '9', 6)], 13))
        self.assertEqual(self.g_3.prim(), ([('E', 'B', 1), ('E', 'C', 2), ('E', 'D', 3), ('B', 'A', 4), ('C', 'F', 5)], 15))
        self.assertEqual(self.g_4.prim(), ([('B', 'A', 1), ('A', 'E', 2), ('E', 'C', 1), ('A', 'D', 3), ('C', 'F', 5)], 12))
        self.assertEqual(self.g_5.prim(), ([('D', 'B', 1), ('D', 'C', 1), ('D', 'A', 2), ('B', 'E', 2)], 6))
        self.assertEqual(self.g_7.prim(), ([('D', 'A', 1), ('A', 'C', 2), ('C', 'E', 1), ('D', 'B', 3)], 7))
        self.assertEqual(self.g_8.prim(),
                         ([('P', 'B', 1), ('B', 'A', 2), ('A', 'T', 2), ('T', 'R', 3), ('T', 'S', 3), ('S', 'Q', 2), ('Q', 'C', 2), ('P', 'J', 4), ('J', 'M', 1), ('M', 'I', 2), ('I', 'H', 1), ('M', 'O', 2), ('H', 'F', 2), ('S', 'N', 4), ('C', 'E', 4), ('E', 'D', 2), ('Q', 'K', 5), ('K', 'G', 1), ('K', 'L', 5)], 48))
        self.assertEqual(self.g_10.prim(),
                         ([('U', 'A', 1), ('U', 'N', 2), ('A', 'D', 2), ('D', 'K', 1), ('K', 'F', 1), ('K', 'L', 1), ('F', 'H', 1), ('H', 'S', 1), ('A', 'E', 2), ('N', 'M', 2), ('H', 'O', 2), ('E', 'I', 2)], 18))


