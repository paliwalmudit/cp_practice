def merge_the_tools(s, k):
    ln=len(s)
    for i in range(0,ln,k):
        ss=s[i:i+k]
        sss=[]
        for x in ss:
            if x not in sss:
                sss.append(x)
        print (''.join(sss))  

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)