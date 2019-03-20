def uniao(A, B):
    C = []
    for a in A:
        C.append(a)
    for e in B:
        if e not in C:
        C.append(e)
    return print(C)
