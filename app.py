from flask import Flask, render_template

app = Flask(__name__) #create instance of class Flask

@app.route('/') #assign following fxn to run when run route requested
def hello_word():
    print(__name__) #where will this go?
    return "We love the 19th"

@app.route("occupyflaskst")
def 

if __name__ == "__main__":
    app.debug = True
    app.run()
