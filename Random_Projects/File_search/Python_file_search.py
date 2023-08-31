
import os

def getFiles():
    docList = os.listdir("C:\\Users\\Josh\\Documents\\GitHub\\Python_Projects\\File_search")
    for i in docList:
        if i.endswith(".txt") == True:
            print(i)















if __name__ == "__main__":
    getFiles()
