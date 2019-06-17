

A = [1,2,2]

def subset(A):
    result = [[]]
    for i in A:
        newsubset = [subset +[i] for subset in result if subset + [i] not in result]
        result.extend(newsubset)
    return result

print(subset(A))