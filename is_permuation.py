s1 = 'fairy tales'

s2 =  'rail safety'

def is_permutation(s1,s2):
    dicty = {}

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in dicty:
            dicty[i] += 1
        else:
            dicty[i] = 1
    for i in s2:
        if i in dicty:
            dicty[i] -= 1
        else:
            dicty[i] = 1

    for i in dicty:
        if dicty[i] != 0:
            return False

    return True

if __name__ == "__main__":
    print(is_permutation(s1,s2))
    

