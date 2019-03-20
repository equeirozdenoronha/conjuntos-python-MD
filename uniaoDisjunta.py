A = [1, 3, 4]
B = [3, 5, 6]

def inserePar(a, Anome):
    C = []
    C.append((a, Anome))
    return C

def uniaoDisjunta(A, B):
    C = []
    
    for a in A:
        C.append(inserePar(a, 'A'))
    for b in B:
        C.append(inserePar(b, 'B'))
    return C

print("Conjunto União Disjunta: ", uniaoDisjunta(A, B))
