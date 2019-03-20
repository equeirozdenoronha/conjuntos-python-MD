def complemento(A, B):
    C = []
    for x in A:
        if x not in B:
            C.append(x)
    return C
