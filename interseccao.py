lista1=[1, 5, 6, 8]
lista2=[1, 10,8, 40]

def intersecao(lista1, lista2):
    lista3 = []
    for n in lista1:
        if n in lista2:
            lista3.append(n)
    return lista3

print("Conjunto intersecção: ", intersecao(lista1, lista2))
