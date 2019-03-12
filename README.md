# Algoritmos de operação de conjuntos utilizando python

#### Alunos: Ezequiel, Kennedy, Taylor e Alexandre Moraes

**Intersecção**

```python
def intersecao(lista1, lista2):  
	lista3 = {}  
	for n in lista1:  
		if n in lista2:  
			lista3.append(n)  
	return lista3
```

Algoritmo:
```
// Programa que verifica a intersecção entre dois conjuntos
algoritmo
	sub-rotina interseccao (c1,c2 numerico)
		c3 <- {}
	    	para a em c1 faca:
	    		se a esta em c2 faca:
	   			c3 <- a
	    	retorne c3
	fim_sub_rotina
fim_algoritmo
```
Explicação:

O algoritmo interseccao demonstra como funcionaria um programa que faz a intersecção entre dois conjuntos. Como argumentos para o método têm-se duas variáveis ambas conjuntos numéricos. Na linha 4 é atribuído um conjunto vazio a c3. Depois o primeiro conjunto passado como parâmetro (c1) é percorrido e a cada elemento deste, faz-se uma comparação onde o objetivo é verificar se o elemento atual em análise, também é um elemento do segundo conjunto, também passado como parâmetro (c2). Caso essa comparação retorne verdade, o elemento é atribuído ao conjunto - antes vazio - c3. Por fim, o algoritmo retorna todo o conjunto c3, onde os elementos contidos nele são os elementos que fazem intersecção entre os dois conjuntos analisados.

**União**
```python
def uniao(l1, l2):  
	l3 = {}  
	for a in l1:  
		l3.append(a)  
	for e in l2:  
		if e not in l3:  
			l3.append(e)  
	return l3
```
Algoritmo:
```
// Programa que faz a união entre dois conjuntos
algoritmo
	sub-rotina uniao (c1,c2 numerico)
		c3 <- {}
	    	para a em c1 faca:
	     	   c3.append(a)
	    	para e em c2 faca:
	     	   se e nao esta em c3 faca:
	          	  c3 <- e
	    	retorne c3
	fim_sub_rotina
fim_algoritmo
```
Explicação:

----
##### append(): acrescenta um elemento ao conjunto
---
O algoritmo de união realiza a união entre dois conjuntos numericos. Ele recebe como parâmetros dois conjuntos sob os quais a operação de união será realizada. Utilizando um loop controlado o primeiro conjunto é percorrido, e cada um dos seus elementos elementos são adicionados em um conjunto resultante da união. O segundo conjunto recebido como parâmetro também é percorrido com um loop controlado, e para cada elemento do conjunto, é verificado se o elemento já existe no conjunto resultante. Caso o elemento não exista, ele é adicionado. Para finalizar a rotina, é retornando o conjunto resultante da união entre os dois conjuntos recebidos como parâmetros na função.


**Diferença**

```python
def diferenca(lista1, lista2):
	lista3 = []
	for n in lista1:
		if n not in lista2:
			lista3.append(n)
	return lista3
```
Algoritmo:
```
algoritmo
	sub-rotina diferenca (c1, c2 numerico):
		inicio
		declare c3 numerico
		c3 <- {}
		para e em c1 faca:
			se e nao esta em c2:
				c3 <- c3 + e
		retorne c3
		fim
	fim_sub_rotina
fim_algoritmo
```
falta explicação

**Plano cartesiano**

Algoritmo:
```
algoritmo
	sub-rotina planoCartesiano (a, b numerico):
		inicio
		para x em a faca:
			para y em b faca:
				escreva a:{x} b:{y}
		fim
	fim_sub_rotina
fim_algoritmo
```
Explicação:

O algoritmo pCartesiano realiza o produto cartesiano entre dois conjuntos. A função pCarteiano recebe como parâmetro dois conjuntos (a, b) sob os quais o produto cartesiano será realizado. É inicializado o conjunto c3, que conterá o resultado do produto cartesiano. Utilizando um loop controlado o primeiro conjunto (a) recebido como parâmetro na função é percorrido, dentro do loop controlado do primeiro conjunto (a), o segundo conjunto (b) recebido como parâmetro na função também é percorrido, e para cada um dos seus elementos, a função escreva é responsável por criar o par com o elemento da iteração do primeiro (a) com o segundo (b) conjunto e adiciona-lo no conjunto c3. Ao final da rotina, o conjunto c3 contendo o produto cartesiano do conjunto a sob o conjunto b é retornado.

**Complemento**

Algoritmo:

```
algoritmo
	sub-rotina complementar (c1, c2 numerico):
		inicio
		declare c3 numerico
		c3 <- {}
		para a em c1 faca:
			se a nao esta em c2:
				c3 <- c3 + a
		retorne c3
		fim
	fim_sub_rotina
fim_algoritmo
```
