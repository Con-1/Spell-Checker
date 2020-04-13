import pandas as pd
import toSoundex as sd
import numpy as np
import json
from os import path            
def fileCheck():
    Fin_Dict=json.load(open("dumpFIN.txt"))
    dic=json.load(open("dumpTEMP.txt"))
    temp_Dic={}
    corr=0
    wrong=0
    with open("Copy.txt",'r') as outfile:
        for line in outfile:
            for word in line.split():
                if(word in dic):
                    corr+=1                    
                else:
                    temp_Dic[word]=sd.findSoundex(word)
                    wrong+=1 
    print("Total Words = ",corr+wrong)
    print("Total Correct Words = ",corr)
    print("Total Wrong Words = ",wrong)
    print()
    print("-------Wrong Words Suggestions------")
    for i in temp_Dic:
        print("Word = ",i)
        if(temp_Dic[i] not in Fin_Dict):
            print("NO SUGGESTIONS")
        else:
            print("Suggestions = ",Fin_Dict[temp_Dic[i]])
        print()
def spellCheck():
    if (not(path.exists('Words_With_Soundex.csv'))):
        wordList=pd.read_csv('Wordlist.csv',encoding="ISO-8859-1")
        arr=wordList.values
        for i in arr:
            i[1]=sd.findSoundex(i[0])
        dic=dict(arr)
        np.savetxt("Words_With_Soundex.csv",arr,'%s',',')   
        finDic={}
        for i in arr:
            if(i[1] in finDic):
                finDic[i[1]].append(i[0])
            else:
                finDic[i[1]]=[i[0]]
        json.dump(dic,open("dumpTEMP.txt",'w'))
        json.dump(finDic,open("dumpFIN.txt",'w'))
    fileCheck()
 
            
            
    
        

