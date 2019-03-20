A=[5, 8, 9,6]
B=[5, 10 ,11 , 7]

def diferenca(A, B):
    C = []
    for a in A:
        if a not in B:
            C.append(a)
    return C

print("Conjunto da diferença: ", diferenca(A, B))
