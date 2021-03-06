class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not (self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not (i == len(self.A) - 1):  # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str

    def vertices_nao_adjacentes(self):
        lista = []
        for t in range(len(self.N)):
            for v in range(len(self.N)):
                string = self.N[t] + "-" + self.N[v]
                string2 = self.N[v] + "-" + self.N[t]
                comp = self.existeAresta(string)
                comp2 = self.existeAresta(string2)
                if (comp == False) and (comp2 == False):
                    lista.append(string)
        return lista

    def ha_laco(self):
        jk = False
        for t in range(len(self.N)):
            for v in range(len(self.N)):
                stri1 = self.N[t] + "-" + self.N[v]
                comp = self.existeAresta(stri1)
                if (self.N[t] == self.N[v]) and (comp == True):
                    jk = True
        return jk

    def ha_paralelas(self):
        lista = []
        check = False
        for t in range(len(self.A)):
            cont = 0
            item1 = list(self.A.items())[t][1]
            for v in range(len(self.A)):
                item2 = list(self.A.items())[v][1]
                if (item1 == item2):
                    cont = cont + 1
                    if cont == 2:
                        check = True
        return check

    def grau(self, v):
        cont = 0
        for t in range(len(self.A)):
            item = list(self.A.items())[t][1]
            if (item[2] == v):
                cont = cont + 1
            elif (item[0] == v):
                cont = cont + 1
        return cont

    def arestas_sobre_vertice(self, N):
        lista = []
        for t in range(len(self.A)):
            item = list(self.A.items())[t][1]
            item2 = None
            if item[0] == N:
                item2 = item[0]
                lista.append(list(self.A.items())[t][0])
            elif item[2] == N:
                item2 = item[2]
                lista.append(list(self.A.items())[t][0])
        return lista

    def eh_completo(self):
        lista = []
        for t in range(len(self.N)):
            for v in range(len(self.N)):
                string = self.N[t] + "-" + self.N[v]
                string2 = self.N[v] + "-" + self.N[t]
                comp = self.existeAresta(string)
                comp2 = self.existeAresta(string2)
                if (comp == False) and (comp2 == False) and (string != string2):
                    lista.append(string)
        if (len(lista) == 0):
            return True
        else:
            return False

    def aresta_entre_vertices(self, aresta):
        for c in range(len(self.A)):
            aux = list(self.A.items())[c][1].split('-');
            a = aux[0]+'-'+aux[1]
            a_inverso = aux[1]+'-'+aux[0]
            if aresta == a:
                return list(self.A.items())[c][0]
            elif aresta == a_inverso:
                return list(self.A.items())[c][0]


    def vizinhos_do_vertice(self, vertice):
        vizinhos = []
        for t in range(len(self.A)):
            arestas = list(self.A.items())[t][1].split('-')
            if arestas[0] == vertice and arestas[1] not in vizinhos:
                vizinhos.append(arestas[1])
            elif arestas[1] == vertice and arestas[0] not in vizinhos:
                vizinhos.append(arestas[0])
        return vizinhos

    def dfs_recursiva(grafo, vertice, visitados):
        visitados.append(vertice)
        for vizinho in grafo.vizinhos_do_vertice(vertice):
            if vizinho not in visitados:
                for t in range(len(grafo.A)):
                    item = list(grafo.A.items())[t][1].split('-')
                    if item[0] == vertice and list(grafo.A.items())[t][0] not in visitados:
                        s1 = item[0]+'-'+vizinho
                        visitados.append(grafo.aresta_entre_vertices(s1))
                        break
                    elif item[1] == vertice and list(grafo.A.items())[t][0] not in visitados:
                        s2 = item[1] + '-' + vizinho
                        visitados.append(grafo.aresta_entre_vertices(s2))
                        break
                grafo.dfs_recursiva(vizinho, visitados)

    def dfs(grafo, vertice):
        visitados = []
        arestas = grafo.A.items()
        grafo.dfs_recursiva(vertice, visitados)
        for x in grafo.N:
            if x not in visitados:
                return -1
        return visitados