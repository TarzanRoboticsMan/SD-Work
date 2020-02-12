from flask import Flask

app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when run route requested
def hello_word():
    print(__name__) #where will this go?
    return "No hablo queso!" 
if __name__ == "__main__":
    app.debug = True
    app.run()
