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

    def recomendar_manga(self, manga):
        if manga not in self.mapeamento:
            print(f"O mangá '{manga}' não foi encontrado no grafo.")
            return

        idx_manga = self.mapeamento[manga]
        generos_manga = set()

        # Identificar os gêneros do mangá dado
        for adj in self.listaAdj[idx_manga]:
            adj_nome = self.inverso_mapeamento[adj]
            if adj_nome.lower() not in ["shounen", "shoujo", "seinen", "josei"]:
                generos_manga.add(adj_nome)

        if not generos_manga:
            print(f"O mangá '{manga}' não está conectado a nenhum gênero.")
            return

        maior_compatibilidade = 0
        melhores_recomendacoes = []

        # Percorre todos os outros mangás
        for outro_manga, idx in self.mapeamento.items():
            if outro_manga == manga:
                continue

            generos_outro = set()

            # Identificar os gêneros do outro mangá
            for adj in self.listaAdj[idx]:
                adj_nome = self.inverso_mapeamento[adj]
                if adj_nome.lower() not in ["shounen", "shoujo", "seinen", "josei"]:
                    generos_outro.add(adj_nome)

            # Calcula a compatibilidade entre os dois mangás
            generos_comuns = generos_manga.intersection(generos_outro)
            if generos_comuns:
                compatibilidade = (len(generos_comuns) / len(generos_manga)) * 100

                # Atualiza a lista de melhores recomendações
                if compatibilidade > maior_compatibilidade:
                    maior_compatibilidade = compatibilidade
                    melhores_recomendacoes = [(outro_manga, generos_comuns)]
                elif compatibilidade == maior_compatibilidade:
                    melhores_recomendacoes.append((outro_manga, generos_comuns))

        # Exibe as recomendações
        if melhores_recomendacoes:
            print(f"Se você gosta de {manga}, você pode gostar dos seguintes mangás com compatibilidade de {maior_compatibilidade:.2f}%:")
            for nome, generos_comuns in melhores_recomendacoes:
                generos_lista = ', '.join(generos_comuns)
                print(f"  - {nome}, por também ser dos gêneros: {generos_lista}")
        else:
            print(f"Nenhum mangá recomendado para '{manga}'.")


    def genero_mais_popular(self):
        contagem = {}
        for vertice, idx in self.mapeamento.items():
            if vertice.lower() not in ["shounen", "shoujo", "seinen", "josei"]:
                # Verifica se o vértice é um gênero
                contagem[vertice] = sum(
                    1
                    for adj in self.listaAdj[idx]
                    if self.inverso_mapeamento[adj].lower() not in ["shounen", "shoujo", "seinen", "josei"]
                )
        max_conexoes = max(contagem.values(), default=0)
        populares = [g for g, c in contagem.items() if c == max_conexoes]
        print(f"Gênero(s) com mais mangás ligados ({max_conexoes}): {', '.join(populares)}")

    def manga_mais_generos(self):
        contagem = {}

        for vertice, idx in self.mapeamento.items():
            # Um mangá deve estar conectado a pelo menos uma demografia e a um ou mais gêneros
            if any(
                self.inverso_mapeamento[adj].lower() in ["shounen", "shoujo", "seinen", "josei"]
                for adj in self.listaAdj[idx]
            ):
                contagem[vertice] = sum(
                    1
                    for adj in self.listaAdj[idx]
                    if self.inverso_mapeamento[adj].lower()
                    not in ["shounen", "shoujo", "seinen", "josei"]
                )

        max_generos = max(contagem.values(), default=0)
        mangas = [m for m, c in contagem.items() if c == max_generos]

        if max_generos > 0:
            print(f"Mangá(s) com mais gêneros ligados ({max_generos}): {', '.join(mangas)}")
        else:
            print("Nenhum mangá encontrado com gêneros conectados.")


    def demografia_mais_diversa(self):
        diversidade = {}  # Dicionário para armazenar a lista de gêneros por demografia

        # Itera sobre os vértices, buscando as demografias
        for vertice, idx in self.mapeamento.items():
            if vertice.lower() in ["shounen", "shoujo", "seinen", "josei"]:
                generos = set()  # Armazena os gêneros únicos da demografia
                # Percorre os mangás conectados à demografia
                for adj in self.listaAdj[idx]:
                    for genero_adj in self.listaAdj[adj]:
                        genero_nome = self.inverso_mapeamento[genero_adj]
                        # Adiciona somente os gêneros (exclui outras demografias ou o próprio mangá)
                        if genero_nome.lower() not in ["shounen", "shoujo", "seinen", "josei"] and genero_nome != vertice:
                            generos.add(genero_nome)
                diversidade[vertice] = generos

        # Identifica a demografia com mais gêneros distintos
        max_diversidade = max((len(g) for g in diversidade.values()), default=0)
        demografias = [d for d, g in diversidade.items() if len(g) == max_diversidade]

        if max_diversidade > 0:
            for demografia in demografias:
                generos = ', '.join(diversidade[demografia])
                print(f"A demografia mais diversa é {demografia}, com {max_diversidade} gêneros: [{generos}]")
        else:
            print("Nenhuma demografia encontrada com gêneros conectados.")


def menu():
    grafo = GrafoND()
    while True:
        print("\n---MANGA ORACLE---")
        print("1. Carregar grafo de arquivo")
        print("2. Salvar grafo em arquivo")
        print("3. Inserir vértice")
        print("4. Inserir aresta")
        print("5. Remover vértice")
        print("6. Remover aresta")
        print("7. Mostrar grafo")
        print("8. Conexidade do grafo")
        print("9. Recomendar mangá baseado em outro")
        print("10. Gênero com mais mangás")
        print("11. Mangá com mais gêneros")
        print("12. Demografia mais diversa")
        print("13. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome_arquivo = input("Digite o nome do arquivo: ")
            grafo.ler_arquivo(nome_arquivo)
        elif opcao == "2":
            nome_arquivo = input("Digite o nome do arquivo: ")
            grafo.salvar_arquivo(nome_arquivo)
        elif opcao == "3":
            vertice = input("Digite o nome do vértice: ")
            grafo.adicionar_vertice(vertice)
        elif opcao == "4":
            v1 = input("Digite o primeiro vértice: ")
            v2 = input("Digite o segundo vértice: ")
            grafo.adicionar_aresta(v1, v2)
        elif opcao == "5":
            vertice = input("Digite o vértice a ser removido: ")
            grafo.remover_vertice(vertice)
        elif opcao == "6":
            v1 = input("Digite o primeiro vértice: ")
            v2 = input("Digite o segundo vértice: ")
            grafo.remover_aresta(v1, v2)
        elif opcao == "7":
            grafo.show()
        elif opcao == "8":
            grafo.conexidade()
        elif opcao == "9":
            manga = input("Digite o mangá: ")
            grafo.recomendar_manga(manga)
        elif opcao == "10":
            grafo.genero_mais_popular()
        elif opcao == "11":
            grafo.manga_mais_generos()
        elif opcao == "12":
            grafo.demografia_mais_diversa()
        elif opcao == "13":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
