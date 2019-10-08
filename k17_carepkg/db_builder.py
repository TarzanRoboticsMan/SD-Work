#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

#db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
#c = db.cursor()               #facilitate db ops

#==========================================================

#command = "CREATE TABLE courses("code" text, "mark" integer, "id" integer);"          # test SQL stmt in sqlite3 shell, save as string

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
with open('courses.csv') as csvfile:
     reader = csv.reader(csvfile)
     for row in reader:
         print row;

#c.execute(command)    # run SQL statement

#==========================================================

#db.commit() #save changes
#db.close()  #close database
