import Makesoundex as msd
# Importing user-defined library
print()
o='1'
while(o!='X'):
    print("Press 1: If want to write Word/Sentance/Paragraph now.")
    print("Press 2: If Already written in file \"0Write_File.txt\".")
    x=(input("Option = "))
    infile=open("Copy.txt",'w')
    if x=='2':
        # If option selected is 2 read from file "0Write_File.txt" and copy it to the file "Copy.txt" 
        with open("0Write_File.txt",'r') as outfile: 
            for line in outfile:
                for word in line.split():
                    infile.write(word.lower())
                    infile.write(" ")
        infile.close()
        # Reading word by word form "0Write_File.txt" and writing it to "Copy.txt".
    elif x=='1':
        # If option = 1 read from the console and write it to "Copy.txt" word by word.
        stri=input("String = ")
        infile.write(stri.lower())
        infile.close()
    else:
        print("Sorry!!! Not valid Option")
        continue
    print()
    msd.spellCheck()
    #call spellcheck function from Makesoundex.py file.
    print()
    print("To Exit Press 'X', Or Press any key to Continue")
    o=input("Option = ")
    
   