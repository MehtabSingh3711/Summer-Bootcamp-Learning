import mysql.connector
# # Connection To Server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Garry@123",
  database = "testpy"
)


# ## Creating Database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE testpy;")


# ## Viewing Database
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES;")
for db in mycursor:
    print(db)


## AFTER USING DATABASE WE CAN DIRECTLY TYPE NAME OF DATABASE IN mydb
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE students ( RegID int(10), Name varchar(255), RollNo varchar(30), Degree varchar(255), Age int(10), Address varchar(255), Contact int(20));") 


## Viewing tables
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES;")
for tb in mycursor:
    print(tb)

## Inserting Data
mycursor = mydb.cursor()
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
students = [("Mehtab", 19),
            ("Rohit", 21),
            ("Sadhna", 19),
            ("Sakshi", 19)]
mycursor.execute(sqlFormula, students)
sqlFormula = "INSERT INTO students (RegID, RollNo) VALUES (%s, %s)"
students = [(120, "63"),
            (121, "58"),
            (122, "23"),
            (123, "15")]
mycursor.executemany(sqlFormula, students)


mydb.commit()

## Selecting and Getting Data
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM STUDENTS")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

 ### SELECTING SPECIFIC
mycursor = mydb.cursor()
mycursor.execute("SELECT age FROM STUDENTS")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

 ### IF U WANT ONLY ONE TO VERIFY IF WORKING
mycursor = mydb.cursor() 
mycursor.execute("SELECT age FROM STUDENTS")
myresult = mycursor.fetchone()
for row in myresult:
    print(row)


## WHERE QUERIES
mycursor = mydb.cursor()
sql = "SELECT * FROM students WHERE age = '19'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for result in myresult:
    print(result)

## UPDATE Query
mycursor = mydb.cursor()
sql = "UPDATE students SET RegID = 120 WHERE name ='Mehtab'"
mycursor.execute(sql)
mydb.commit()

## DELETING Entries
mycursor = mydb.cursor()
sql = "DELETE FROM students WHERE name is null"
mycursor.execute(sql)
mydb.commit()   

## DROPPING Table
mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS students"
mycursor.execute(sql)
mydb.commit()
