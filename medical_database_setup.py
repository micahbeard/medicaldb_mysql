print("Starting...")
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="medicaldb"
    )

mycursor = db.cursor()
# mycursor.execute("CREATE DATABASE medicaldb")
mycursor.execute("CREATE TABLE patient (ID INT AUTO_INCREMENT NOT NULL, FirstName VARCHAR(255) NOT NULL CHECK(FirstName NOT LIKE '%[^A-Z]%'), LastName VARCHAR(255) NOT NULL CHECK(LastName NOT LIKE '%[^A-Z]%'), Sex CHAR(1), Height FLOAT(2) NOT NULL CHECK(Height>=0 AND Height<=1000), Weight FLOAT(2) NOT NULL, Result VARCHAR(255) CHECK(Result='Positive' OR Result='Negative' OR Result=''), PRIMARY KEY (ID))")
mycursor.execute("INSERT INTO patient (FirstName, LastName, Sex, Height, Weight, Result) VALUES ('Bob', 'Smith', 'M', 135.90, 190.98, 'Positive')")
mycursor.execute("INSERT INTO patient (FirstName, LastName, Sex, Height, Weight, Result) VALUES ('Sara', 'Smith', 'F', 130.90, 205.64, 'Negative')")


db.commit()

mycursor.execute("SELECT * FROM patient")

for x in mycursor:
    print(x)

# mycursor.execute("DROP TABLE patient") # Delete Table