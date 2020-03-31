from flask import Flask, render_template

app = Flask(__name__) #create instance of class Flask

@app.route('/')
def hello_word():
    print(__name__)
    
if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0')
