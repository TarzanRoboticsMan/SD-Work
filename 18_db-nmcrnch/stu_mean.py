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
c.execute("CREATE TABLE IF NOT EXISTS stu_avg(id text, avg real)")

#Find each student
kidList = c.execute("SELECT name, id FROM students")
courseList = c.execute("SELECT mark, id FROM courses")

gradeTot = 0
numClasses = 0

for kid in kidList: #For each student
         for class in courseList: #Check each course
                  if class[id] == kid[id]: #To see if it's their grade
                           numClasses++ 
                           gradeTot+=class[mark] #Add to average
         c.execute("INSERT INTO stu_avg VALUES("+kid+","+gradeTot/numClasses)
         print(kid[name]+", id "+kid[id]+": average "+gradeTot/numClasses)
         gradeTot = 0
         numClasses = 0 #reset counters
         
def addCourse(code, mark, id):
         c.execute("INSERT INTO courses VALUES("+code+","+mark+","+id+")")


#==========================================================

db.commit() #save changes
db.close()  #close database
