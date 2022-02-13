def dupl(x):
    repeated = []
    for i in range(len(x)):
        k=i+1
        for j in range(k, len(x)):
            if x[i]==x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
