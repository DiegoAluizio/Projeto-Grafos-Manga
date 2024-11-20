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
![Grafo modelado](https://github.com/DiegoAluizio/Projeto-Grafos-Manga/blob/main/Imagens/ImagemGrafoProjeto.png)
Link: http://graphonline.ru/pt/?graph=tqCzhBfcJuJvvpTv

No grafo acima, as quatro “pontas” são os vértices de demografia. Ligados a eles, estão os mangás que pertencem à respectiva demografia. No centro temos os gêneros. Da maneira que o problema foi modelado, demografias e gêneros se ligam somente a mangás, ou seja, não há conexões diretas entre demografia e gêneros, sempre havendo um mangá entre ambos. Também não há ligações diretas entre vértices do mesmo “tipo”.

Dessa forma, podemos definir dois tipos de relação entre vértices (levando em conta que o grafo é não-direcionado): Mangá-Demografia e Mangá-Gênero.

Todos os vértices possuem labels respectivas aos seus nomes. Para demografia, Shounen, Seinen, Shoujo ou Josei, para mangás, seu título, e para gêneros, seu respectivo nome.

As conexões foram modeladas com base na catalogação do site Anilist (anilist.co)

# Objetivos ODS:

O projeto pode ser enquadrado no objetivo de número 4 “Educação de Qualidade”, pois parte fundamental de uma boa educação é a cultura, e, nesse quesito, recomendações podem incentivar ainda mais seu consumo e expansão de horizontes, elementos essenciais para o bom desenvolvimento intelectual.


# Testes de Execução:

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
