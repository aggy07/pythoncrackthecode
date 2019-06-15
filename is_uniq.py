def noDupe(s):
    a = {}
    for char in s:
        if char in a:
            return False
        else:
            a[char] = 1
    return True


print(noDupe('sdsdsdsddsdsd'))
print(noDupe('dsa'))