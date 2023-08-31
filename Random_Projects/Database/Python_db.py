import sqlite3

db = sqlite3.connect("python.db")

with db:
    cur = db.cursor()
    cur.execute("Create Table If Not Exists tbl_files ( \
        ID Integer Primary Key AutoIncrement, \
        col_fname Text \
        )")
    db.commit()
db.close()

def getFiles():
    docList = ('information.docx', 'Hello.txt', 'myImage.png', \
               'myMovie.mpg', 'World.txt', 'data.pdf', 'myphoto.jpg')
    for i in docList:
        if i.endswith(".txt") == True:
            db = sqlite3.connect("python.db")
            with db:
                cur = db.cursor()
                cur.execute("Insert Into tbl_files (col_fname) Values (?)", \
                            ([i]))
                db.commit()
            db.close()
            print(i)

if __name__ == "__main__":
    getFiles()
