s = "Was it a cat I saw"

def is_pal(s):
    i = 0
    j = len(s) - 1
    while i < j:
        while not s[i].isalnum() and i <j:
            i += 1
        while not s[j].isalnum() and i <j:
            j -= 1
        
        if s[i].lower() == s[j].lower():
            return True
            i +=1
            j -=1
        else:
            return False

def is_pal_new(s):
    s = s.lower()
    s.replace(" ","")

    i = 0 
    j = len(s) -1 
    while i < j:
        if s[i].lower() == s[j].lower():
            return True
            i += 1
            j -= 1
        else:
            return False
    
        

print(is_pal(s))
print(is_pal("malayalam"))
print(is_pal("bam"))
print(is_pal_new("Was it a cat I saw"))