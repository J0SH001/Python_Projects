
import sqlite3

dataVal = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Puppet', 100), ('Ak\'not', 'Mangalore', -5))

with sqlite3.connect("C:\\Users\\Josh\\Documents\\GitHub\\Python_Projects\\Random_Projects\\data.db") as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS Roster;
                    CREATE Table Roster (Name TEXT, Species TEXT, IQ INT);
                    """)
    c.commit()
    c.execute("INSERT INTO Roster VALUES(?, ?, ?)", dataVal)

