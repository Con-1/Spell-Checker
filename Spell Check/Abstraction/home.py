import Makesoundex as msd
print()
o='1'
while(o!='X'):
    print("Press 1: If want to write Word/Sentance/Paragraph now.")
    print("Press 2: If Already written in file \"0Write_File.txt\".")
    x=(input("Option = "))
    infile=open("Copy.txt",'w')
    if x=='2':
        with open("0Write_File.txt",'r') as outfile: 
            for line in outfile:
                for word in line.split():
                    infile.write(word.lower())
                    infile.write(" ")
        infile.close()
    elif x=='1':
        stri=input("String = ")
        infile.write(stri.lower())
        infile.close()
    else:
        print("Sorry!!! Not valid Option")
        continue
    print()
    msd.spellCheck()
    print()
    print("To Exit Press 'X', Or Press any key to Continue")
    o=input("Option = ")
    
   