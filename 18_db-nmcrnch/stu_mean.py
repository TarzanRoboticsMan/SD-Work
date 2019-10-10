#Coby Sontag
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

#Create new table
c.execute("CREATE TABLE IF NOT EXISTS stu_avg(id text, mark real)")

#Find each student
print(c.execute("SELECT id FROM students"))
'''
with open('courses.csv') as csvfile:
     reader = csv.reader(csvfile, delimiter=',')
     for row in reader:
         #print(row)
         command = "INSERT INTO courses VALUES ('"+row[0]+"','"+row[1]+"','"+row[2]+"')"
         c.execute(command)

Compute each student’s average
Display each student’s name, id, and average
Create a table of IDs and associated averages, named "stu_avg"
Facilitate adding rows to the courses table
'''
#==========================================================

db.commit() #save changes
db.close()  #close database
