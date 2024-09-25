# Projeto por: Diego Oliveira Aluizio

class GrafoND:  # Classe para representar um grafo não direcionado
    def __init__(self):
        # Dicionário que mapeia o nome do vértice ao índice (usado para trabalhar com listas de adjacência)
        self.mapeamento = {}  
        
        # Dicionário inverso, que mapeia o índice de volta ao nome do vértice
        self.inverso_mapeamento = {}
        # Detalhe: com o uso do mapeamento, a criação do grafo foi alterada para facilitar a sua manipulação
        # Lista de adjacência onde cada índice armazena uma lista de adjacentes
        self.listaAdj = []  
        
        # Contador do número de vértices no grafo
        self.n = 0  
        
        # Contador do número de arestas no grafo
        self.m = 0  

    def adicionar_vertice(self, nome_vertice):
        # Adiciona um novo vértice se ele ainda não existe no grafo
        if nome_vertice not in self.mapeamento:
            # Mapeia o nome do vértice para o próximo índice disponível
            self.mapeamento[nome_vertice] = self.n
            
            # Faz o mapeamento inverso do índice para o nome
            self.inverso_mapeamento[self.n] = nome_vertice
            
            # Adiciona uma nova lista para armazenar as adjacências desse vértice
            self.listaAdj.append([])  
            
            # Incrementa o número de vértices
            self.n += 1  

    def adicionar_aresta(self, v, w):
        # Obtém os índices dos vértices v e w
        idx_v = self.mapeamento[v]
        idx_w = self.mapeamento[w]
        
        # Se w não está adjacente a v, adiciona w à lista de adjacências de v e vice-versa
        if idx_w not in self.listaAdj[idx_v]:
            self.listaAdj[idx_v].append(idx_w)
            self.listaAdj[idx_w].append(idx_v)
            
            # Incrementa o número de arestas
            self.m += 1  

    def remover_vertice(self, nome_vertice):
        # Verifica se o vértice existe no grafo
        if nome_vertice not in self.mapeamento:
            print(f"Vértice {nome_vertice} não encontrado.")
            return
        
        # Obtém o índice do vértice a ser removido
        idx = self.mapeamento[nome_vertice]

        # Quantidade de vértices removidos:
        removidos = 0
        
        # Remove o vértice das listas de adjacências de outros vértices
        adjacencias = self.listaAdj[idx]
        for adj in adjacencias:
            self.listaAdj[adj].remove(idx)
            removidos += 1

        
        # Remove o vértice da lista de adjacência e dos mapeamentos
        self.listaAdj.pop(idx)
        del self.inverso_mapeamento[idx]
        del self.mapeamento[nome_vertice]

        # Atualiza o número de vértices
        self.n -= 1

        # Atualiza o número de arestas
        self.m -= removidos
        
        # Ajusta os índices dos vértices que foram afetados pela remoção
        self.listaAdj = [ [v-1 if v > idx else v for v in adj] for adj in self.listaAdj ]
        self.inverso_mapeamento = {i-1 if i > idx else i: v for i, v in self.inverso_mapeamento.items()}
        self.mapeamento = {v: i for i, v in self.inverso_mapeamento.items()}

    def remover_aresta(self, v, w):
        # Verifica se ambos os vértices estão no grafo
        if v in self.mapeamento and w in self.mapeamento:
            idx_v = self.mapeamento[v]
            idx_w = self.mapeamento[w]
            
            # Remove a aresta entre v e w, se existir
            if idx_w in self.listaAdj[idx_v]:
                self.listaAdj[idx_v].remove(idx_w)
                self.listaAdj[idx_w].remove(idx_v)
                self.m -= 1
                
    def conexidade(self):
        # Verifica se o grafo é conexo utilizando uma busca em profundidade (DFS)
        visitado = [False] * self.n
        
        # Optei por declarar a função dfs internamente para não ter que modificar ainda mais o construtor
        def dfs(v):
            visitado[v] = True
            # O uso de lista permite uma abordagem "recursiva" para o dfs
            for w in self.listaAdj[v]:
                if not visitado[w]:
                    dfs(w)
        
        # Inicia a DFS a partir do vértice 0
        dfs(0)
        
        # Retorna True se todos os vértices forem visitados
        return all(visitado)

    def show(self):
        # Exibe o número de vértices e arestas
        print(f"\nNúmero de vértices: {self.n}, Número de arestas: {self.m}")
        
        # Exibe cada vértice e seus vértices adjacentes
        for nome_vertice in self.mapeamento:
            idx = self.mapeamento[nome_vertice]
            adjacencias = [self.inverso_mapeamento[adj] for adj in self.listaAdj[idx]]
            print(f"{nome_vertice}: {adjacencias}")
        print("\nFim da impressão do grafo.")

    def ler_arquivo(self, nome_arquivo="grafo.txt"):
        # Lê o grafo de um arquivo de texto
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                
                # Ignora comentários e linhas vazias
                if linha.startswith("#") or not linha:
                    continue

                # Separa os vértices da linha
                vertices = linha.split(';')
                vertice_principal = vertices[0]

                # Adiciona o vértice principal ao grafo se ainda não estiver presente
                if vertice_principal not in self.mapeamento:
                    self.adicionar_vertice(vertice_principal)

                # Adiciona os vértices adjacentes
                for vertice_adjacente in vertices[1:]:
                    if vertice_adjacente not in self.mapeamento:
                        self.adicionar_vertice(vertice_adjacente)

                    self.adicionar_aresta(vertice_principal, vertice_adjacente)

    def salvar_arquivo(self, nome_arquivo="grafo.txt"):
        # Salva o grafo em um arquivo de texto ao inserir todos os vértices seguidos de suas conexões, separados por ;
        with open(nome_arquivo, 'w') as arquivo:
            for vertice_principal in self.mapeamento:
                idx = self.mapeamento[vertice_principal]
                adjacentes = [self.inverso_mapeamento[adj] for adj in self.listaAdj[idx]]
                arquivo.write(f"{vertice_principal};" + ";".join(adjacentes) + "\n")
        # Não é a maneira mais efetiva de salvar, visto que haverá redundância, mas para seguir o prazo, esta é a solução provisória

def menu():
    # Função de menu que controla a interação com o usuário
    grafo = GrafoND()  # Cria uma instância do grafo não direcionado
    
    # Loop infinito até o usuário escolher encerrar
    while True:
        # Exibe o menu de opções
        print("\n------Manga Oracle------")
        print("\nMenu de opções:")
        print("a) Ler dados do arquivo grafo.txt")
        print("b) Gravar dados no arquivo grafo.txt")
        print("c) Inserir vértice")
        print("d) Inserir aresta")
        print("e) Remover vértice")
        print("f) Remover aresta")
        print("g) Mostrar conteúdo do arquivo")
        print("h) Mostrar grafo")
        print("i) Conexidade do grafo")
        print("j) Encerrar")

        # Lê a opção do usuário
        opcao = input("Escolha uma opção: ").lower()

        # Executa a opção escolhida pelo usuário
        if opcao == 'a':
            grafo.ler_arquivo("grafo.txt")
        elif opcao == 'b':
            grafo.salvar_arquivo("grafo.txt")
        elif opcao == 'c':
            vertice = input("Digite o nome do vértice a ser inserido: ")
            grafo.adicionar_vertice(vertice)
        elif opcao == 'd':
            v1 = input("Digite o nome do primeiro vértice: ")
            v2 = input("Digite o nome do segundo vértice: ")
            grafo.adicionar_aresta(v1, v2)
        elif opcao == 'e':
            vertice = input("Digite o nome do vértice a ser removido: ")
            grafo.remover_vertice(vertice)
        elif opcao == 'f':
            v1 = input("Digite o nome do primeiro vértice: ")
            v2 = input("Digite o nome do segundo vértice: ")
            grafo.remover_aresta(v1, v2)
        elif opcao == 'g':
            # Mostra o conteúdo do arquivo grafo.txt
            with open("grafo.txt", "r") as arquivo:
                print(arquivo.read())
        elif opcao == 'h':
            grafo.show()  # Exibe o grafo
        elif opcao == 'i':
            # Verifica se o grafo é conexo
            if grafo.conexidade():
                print("O grafo é conexo.")
            else:
                print("O grafo não é conexo.")
        elif opcao == 'j':
            print("Encerrando programa...")
            break
        else:
            print("Comando inválido! Tente novamente")

menu()
