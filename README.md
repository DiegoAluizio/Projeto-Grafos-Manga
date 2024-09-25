# Projeto de Teoria dos grafos: Recomendação de mangás
# Link para o youtube: /placeholder/
# Título: Manga Oracle

O projeto visa modelar um sistema de recomendação de mangás em pequena escala, para testar a validade dos algoritmos para uma possível expansão. A modelagem do problema funciona da seguinte maneira:

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
