#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

c.execute("CREATE TABLE IF NOT EXISTS courses(code text, mark integer, id integer)")
# test SQL stmt in sqlite3 shell, save as string

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
with open('courses.csv') as csvfile:
     reader = csv.reader(csvfile, delimiter=',')
     for row in reader:
         #print(row)
         command = "INSERT INTO courses VALUES ('"+row[0]+"','"+row[1]+"','"+row[2]+"')"
         c.execute(command)

#==========================================================

c.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER, id INTEGER)")

with open('students.csv') as csvfile:
     reader = csv.reader(csvfile)
     for row in reader:
         command = "INSERT INTO courses VALUES ('"+row[0]+"','"+row[1]+"','"+row[2]+"')"
         c.execute(command)

#==========================================================

db.commit() #save changes
db.close()  #close database
