# Projeto de Teoria dos grafos: Recomendação de mangás
## Diego Oliveira Aluizio, RA: 10402412
# Link para o youtube: /placeholder/
# Título: Manga Oracle

O projeto visa modelar um sistema de recomendação de mangás em pequena escala, para testar a validade dos algoritmos para uma possível expansão.

# Modelagem:

## Demografias:
No mercado editorial japonês, é comum decidir em qual revista um mangá será publicado levando em conta a idade e gênero do público-alvo imaginado. Desta forma, no grafo teremos os vértices Shounen, Seinen, Shoujo e Josei que têm como alvo, respectivamente, jovens garotos, jovens homens, jovens garotas e jovens mulheres.

## Mangás:
São os quadrinhos japoneses. O objetivo do projeto é traçar pontos em comuns entre eles para criar um sistema de recomendação. Para tal, a intenção inicial é que o usuário digite um mangá presente na lista de vértices e o sistema utilizará um algoritmo que irá encontrar o(s) mangá(s) com maior compatibilidade com o selecionado como entrada, baseado na quantidade de “matches” de gêneros.

## Gêneros:
São categorias que dão uma ideia geral do que esperar de uma obra. Serão utilizados para encontrar a compatibilidade entre obras.

# Modelagem Graph Online:
## Grafo completo
![Grafo modelado](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/ImagemGrafoProjeto.png)

Link: http://graphonline.ru/pt/?graph=tqCzhBfcJuJvvpTv

## Grafo Reduzido Simplificado
![Grafo reduzido](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/ModelagemReduzida.png)

Link: http://graphonline.top/en/?graph=FdWGWwwCrGIOBwDn

No grafo acima, as “pontas” são os vértices de demografia. Ligados a eles, estão os mangás que pertencem à respectiva demografia. Da maneira que o problema foi modelado, demografias e gêneros se ligam somente a mangás, ou seja, não há conexões diretas entre demografia e gêneros, sempre havendo um mangá entre ambos. Também não há ligações diretas entre vértices do mesmo tipo.

Dessa forma, podemos definir dois tipos de relação entre vértices (levando em conta que o grafo é não-direcionado): Mangá-Demografia e Mangá-Gênero.

Todos os vértices possuem labels respectivas aos seus nomes. Para demografia, Shounen, Seinen, Shoujo ou Josei, para mangás, seu título, e para gêneros, seu respectivo nome. O programa identifica o tipo de um vértice (demografia, mangá ou gênero) através de seus vizinhos. Como as demografias são constantes, o programa verifica a label do vértice em que está, se for o nome de uma demografia, ele sabe que está em uma demografia. Se não, verifica-se os vizinhos. Se não houver um vértice com label de demografia, significa que é um gênero (pois gêneros não se ligam a demografias), se houver, é um mangá.

As conexões foram modeladas com base na catalogação do site Anilist (anilist.co) e obtidas através da página correspondente ao mangá, como a imagem a seguir mostra:

![Anilist](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/Anilist.png)

# Objetivos ODS:

O projeto pode ser enquadrado no objetivo de número 4 “Educação de Qualidade”, pois parte fundamental de uma boa educação é a cultura, e, nesse quesito, recomendações podem incentivar ainda mais seu consumo e expansão de horizontes, elementos essenciais para o bom desenvolvimento intelectual.


# Execução (Parte 1):

## Testes com um arquivo vazio:
![Print1](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print1.png)

Ao iniciar o programa, o grafo está vazio


![Print2](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print2.png)

Mostrando o arquivo vazio


![Print3](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print3.png)

Inserindo dois vértices


![Print4](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print4.png)

Grafo após a inserção


![Print5](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print5.png)

Inserindo uma aresta e mostrando o resultado


![Print6](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print6.png)

Gravando grafo no arquivo e mostrando seu conteúdo


![Print7](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print7.png)

Conexidade do grafo


![Print8](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print8.png)

Inserindo um vértice para torná-lo desconexo


![Print9](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print9.png)

Removendo esse vértice


![Print10](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print10.png)

Grafo após remoção do vértice

![Print11](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print11.png)

Removendo aresta mostrando conteúdo do grafo


![Print12](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print12.png)

Encerrando o programa

## Testes com parte do grafo modelado (a fim de evitar prints grandes):

![Print13](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print13.png)

Lendo um arquivo e mostrando o grafo


![Print14](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print14.png)

Removendo o vértice Action


![Print15](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print15.png)

Removendo a aresta 'Chainsaw Man-Shounen'


![Print16](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print16.png)

Gravando no arquivo e mostrando o conteúdo


![Print17](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print17.png)

Reinserindo o vértice Action


![Print18](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print18.png)

Inserindo a aresta 'Chainsaw Man-Action'

![Print19](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/print19.png)

Conexidade do grafo

# Parte 2 do Projeto:

## Foram realizadas as seguintes mudanças:
- Adição de 4 novos métodos
- Mudanças no menu

## Recomendar mangá:

Recomenda os mangás que tiverem a maior compatibilidade com um mangá presente no grafo passado como parâmetro. Seu funcionamento consiste em comparar a intersecção entre a lista de adjacência do mangá de entrada e a lista de adjacência de todos os outros mangás no grafo (ignorando demografia). A compatibilidade é medida através da proporção entre os gêneros do mangá de entrada e os gêneros do(s) mangá(s) com maior compatibilidade. Por exemplo, caso um mangá que se liga a 5 gêneros seja passado como parâmetro, e a maior compatibilidade seja com um mangá que possui 4 desses 5 gêneros, o programa irá recomendar esse mangá, indicar o índice de compatibilidade (80% nesse exemplo) e dizer quais gêneros em comum com a entrada a recomendação possui.

## Gênero mais popular:

Indica qual o gênero que possui mais ligações na sua lista de adjacências.

## Mangá com mais gêneros:

Indica qual mangá possui mais ligações de gênero em sua lista de adjacências.

## Demografia mais diversa:

Para cada demografia é criada uma lista de gêneros. Em seguida, o programa verifica a lista de adjacência de cada mangá ligado a ela e adiciona um gênero a cada vez que ele é encontrado na lista de gêneros da demografia. Em seguida, o programa verifica qual demografia tem o maior número de gêneros e lista os gêneros presentes nela.

## Alterações no menu:

Para comportar as novas funções e facilitar a seleção, as opções válidas vão de 1 a 13, como mostra a imagem a seguir:

![Menu Novo](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/Menu.png)

# Execução dos novos métodos:

## Recomendação
![Recomendacao](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/Recomendacao.png)

## Gênero mais popular
![GeneroPopular](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/GeneroPopular.png)

## Mangá com mais gêneros
![MangaMais](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/MangaMais.png)

## Demografia mais diversa
![DemografiaDiversa](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/DemografiaDiversa.png)
