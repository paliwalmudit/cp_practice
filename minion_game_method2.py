#for each character(i) there will be a substring with every character in order in that lenth(n) so number of substrings will be length-i 
#(-i to remove character before the dezired character) number of occurence of substring = length - i
def minion_game(string):
    vowel = "AEIOU"
    sc = 0
    kc = 0
    x = len(string)
    for i in range(x):
        if string[i] in vowel:
            kc += x - i
        else:
            sc += x - i
    if sc > kc:
        print("Stuart", str(sc))
    elif kc > sc:
        print("Kevin", str(kc))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)