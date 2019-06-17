def URLify(string):
    newstring = ""
    k = len(string)
    while (string[k-1] == " "):
        k = k-1
    for i in range(k):
        if string[i] == ' ':
            newstring = newstring + '%20'
        else:
            newstring = newstring + string[i]
    print(newstring)

print(URLify('What   the fuck       '))
string = 'what the fuck'
print(' '.join(string.split()))



A = [1,2,3]
print(tuple(A))