"""
file = open("myfile.txt","w")
file.write("myTekst")
file.close()
"""

import bookCreator as bookCreator
import LogCreator as Log
import fileReader as reader

def main():
    print("1 - kulalisteraamat")
    print("2 - Luua loogid")
    print("2 - Lugeda faili")
    userInput = input("Sinu valik: ")
    if userInput == "1":
       bookCreator.guestBook()
    elif userInput =="2":
        Log.createLog()
     elif userInput =="3":
        userfile = input("milline file sa tahad lugeda?")
        filereader.readfile(userfile)
    else:
        print("vale valik")
main()
