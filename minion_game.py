def minion_game(string):
    res=[]
    n=len(string)
    for i in range(n):
        if(string[i] not in res):
            res.append(string[i])
        for j in range(0,n+1,1):
            if(string[i:j] not in res and string[i:j]!=""):
                res.append(string[i:j])
    sr=0
    kr=0
    vowel="AEIOU"
    for i in res:
        if(i[0] in vowel):
            kr+=string.count(i)
        else:
            sr+=string.count(i) 
    if sr>kr:
        print("Stuart",sr)
    elif sr==kr:
        print("Draw")
    else:
        print("Kevin",kr)
    
    
    

if __name__ == '__main__':
    s = input()
    minion_game(s)