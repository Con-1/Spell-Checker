import pandas as pd
import numpy as np
# Importing Pandas and Numpy to deal with the CSV file, Data frames and Numpy arrays
import toSoundex as sd
# Importing toSoundex library.
# This is a user-defined library which has findSoundex function
# This function takes a word as a input and return a soundex as a string of that word.
import json
# With help of this library Dumping a data structure to a file and extract it as it is
from os import path            
# This library deals with the file system of the windows.
def spellCheck():
    if (not(path.exists('Words_With_Soundex.csv'))):
        # Checks the file If the file with soundex data exists, Countinue but if it doesn't calculate it and create it.
        wordList=pd.read_csv('Wordlist.csv',encoding="ISO-8859-1")
        # Import all the words from "WorList.csv" as panda dataframe.
        arr=wordList.values
        # arr is numpy array of the wordList dataframe.
        for i in arr:
            i[1]=sd.findSoundex(i[0])
            # Find all the soundex values of the words in array and store them against it.
        dic=dict(arr)
        # dic is a dictonary of the numpy array arr.
        np.savetxt("Words_With_Soundex.csv",arr,'%s',',')   
        # Save the data of Words and soundex values in a file "Words_With_Soundex.csv"
        finDic={}
        for i in arr:
            if(i[1] in finDic):
                finDic[i[1]].append(i[0])
            else:
                finDic[i[1]]=[i[0]]
        # For loop of making dictonary that stores a soundex value as a key and list of words corresponding to that Soundex value as a Element.
        json.dump(dic,open("dumpTEMP.txt",'w'))
        json.dump(finDic,open("dumpFIN.txt",'w'))
        # Dump dic and Fin_Dict with help of the json to be extracted the data in from of dictonaries from the text file.
    fileCheck()

def fileCheck():
    Fin_Dict=json.load(open("dumpFIN.txt"))
    dic=json.load(open("dumpTEMP.txt"))
    # Extracting the data in from of dictonaries from the text file.
    # Fin_Dict is a dictonary that stores a soundex value as a key and list of words corresponding to that Soundex value as a Element.
    # dic is a dictonary that stores a all the words in the vocab as a key and its Soundex value as a Element.
    temp_Dic={} # Stores all the all the wrong words with their Soundex.
    corr=0      # Stores all the sum of the correct words.
    wrong=0     # Stores all the sum of the wrong words.
    with open("Copy.txt",'r') as outfile:
        # Reading the file "Copy.txt" which contains  all the words given by the user.
        for line in outfile:
            for word in line.split():
                # Reading File "Copy.txt" word by word.
                if(word in dic):
                    corr+=1                    
                    # If that word lies in the dic that means the word lies in the vocab and is correct and increase the counter corr.
                else:
                    # That means that the word does not exists in the vocab and is wrong.
                    temp_Dic[word]=sd.findSoundex(word)
                    wrong+=1 
                    # Find the soundex of that word, and sotre it in the temp_Dict dictonary and increase the wrong counter.
    print("Total Words = ",corr+wrong)
    print("Total Correct Words = ",corr)
    print("Total Wrong Words = ",wrong)
    print()
    # Display all the info. like total words, correct words, wrong words.
    print("-------Wrong Words Suggestions------")
    # Loop that iterate in temp_Dict take words and soundex and display all the suggestions for that word sharing the same soundex from Fin_Dict.
    for i in temp_Dic:
        print("Word = ",i)
        if(temp_Dic[i] not in Fin_Dict):
            # If the soundex does not lie in the Fin_Dict print No Suggestions.
            print("NO SUGGESTIONS")
        else:
            # Print all the suggestions for that given soundex.
            print("Suggestions = ",Fin_Dict[temp_Dic[i]])
        print()
 
            
            
    
        

