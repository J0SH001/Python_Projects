import sqlite3
with sqlite3.connect("C:\\Users\\Josh\\Documents\\GitHub\\Python_Projects\\Random_Projects\\SQLite\\sqlite.db") as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE Table People (FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES ('Ron', 'Obvious', '42');
                    """)
    connection.commit()
    peopleValues = (('Luigi', 'Vercotti', 43), ('Jean-Baptiste Zorg', 'Human', 122))
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
    connection.commit()

# select all first and last names from people over age 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    while True:
            row = c.fetchone()
            if row is None:
                break
            print(row)
connection.close()
