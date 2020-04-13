def findSoundex(word):
    vov=['a','e','i','o','u','y','w','h','-',"'",'!']
    li1=['b','f','p','v']
    li2=['c','g','j','k','q','s','x','z']
    li3=['d','t']
    li4=['l']
    li5=['m','n']
    li6=['r']
    if(word=='a'):
        return "A000"
    lisSoundex=[]
    lisSoundex.append(word[0].upper())
    prevchar=word[0]
    for i in range(1,len(word)):
        if ((word[i] in vov)):
            pass
        if(prevchar==word[i]):
            pass
        elif word[i] in li2:
            lisSoundex.append('2')
        elif word[i] in li1:
            lisSoundex.append('1')
        elif word[i] in li3:
            lisSoundex.append('3')
        elif word[i] in li5:
            lisSoundex.append('5')
        elif word[i] in li4:
            lisSoundex.append('4')
        elif word[i] in li6:
            lisSoundex.append('6')
        prevchar=word[i]
        if(len(lisSoundex)==4):
            break
    if(len(lisSoundex)<4):
        for i in range(4-len(lisSoundex)):
            lisSoundex.append('0')
    soundex = ''.join(lisSoundex)
    return soundex

    

