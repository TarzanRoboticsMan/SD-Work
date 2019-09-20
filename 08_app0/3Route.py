
from flask import Flask

app = Flask(__name__) #create instance of class Flask

@app.route('/') #assign following fxn to run when run route requested
def hello_word():
    print(__name__) #where will this go?
        return "BASIC... Use routes!"

@app.route("/fine")
def route1():
    print(__name__)
        return "lame... try more!"

@app.route("/howboutthise")
def route1():
        print(__name__)
        return "now we're getting there"

@app.route("/Igetitnowe")
def route1():
        print(__name__)
        return "Alright dude!"

if __name__ == "__main__":
    app.debug = True
    app.run()

