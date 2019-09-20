from flask import Flask

app = Flask(__name__) #create instance of class Flask

@app.route('/') #assign following fxn to run when run route requested
def hello_word():
    print(__name__) #where will this go?
    return "Love 19th"

coll = [0,1,1,2,3,5,8]
@app.route("/my_foist_template")
def test_templ():
    print(__name__)
    return render

if __name__ == "__main__":
    app.debug = True
    app.run()
