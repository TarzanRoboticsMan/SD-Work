from flask import Flask, render_template, random

fn = 'occupations.csv'
fileR = open(fn, 'r')

jobs = fileR.readlines()
occupations = dict()

for job in jobs:
    words = job.split(',')
    percentage = words.pop(len(words) - 1)
    #delimiter = ','
    occupations[','.join(words)] = float(percentage)

def randomJob(dictOfJobs):
    perct = dictOfJobs['Total'] * 100
    randomperct = random.random() * perct
    keys = dictOfJobs.keys()
    x = 0;
    while ((dictOfJobs[keys[x]] * 100) < randomperct):
        randomperct = randomperct - (dictOfJobs[keys[x]] * 100)
        x = x + 1
    return keys[x]

print(randomJob(occupations))


app = Flask(__name__) #create instance of class Flask

@app.route('/') #assign following fxn to run when run route requested
def hello_word():
    print(__name__) #where will this go?
    return "Default"

@app.route("/occupyflaskst")
def protest():

    return render_template('model_templt.html',
                            titl="Occupation List",
                            head="Returns random occupation from the table below\nMr. Mylky\nCoby Sontag,Ethan Chen")
if __name__ == "__main__":
    app.debug = True
    app.run()
