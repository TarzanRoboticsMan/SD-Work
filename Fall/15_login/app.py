#Saad Bhuiyan and Coby Sontag
#SoftDev1 pd2
#K15 -- Using Python, Flask, Jinja2, and HTML to create a form and custom response.
#2019-10-02

from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)

teamName = "Team Cod"
teamMembers = "Saad Bhuiyan and Coby Sontag"

@app.route("/")
def root():
    if ('t' in session):
        print("Redirected to /welcome from /")
        return redirect(url_for("welcome"))
    else:
        return redirect(url_for("login"))

@app.route("/login")
def login():
    error = ""
    print(request.form)
    if len(request.form) > 0:
        if request.form["username"] == myUsername and request.form["password"] == myPassword:
            session['logged?'] = 't'
            print("Redirected to /welcome from /login")
            return redirect(url_for("welcome"))
        else:
            error = "Wrong username or password"

    return render_template("login.html",
                            teamName = teamName,
                            teamMembers = teamMembers,
                            error = error
    )

myUsername = "teamCod"
myPassword = "fishy"

@app.route("/welcome")
def welcome():
    return render_template("welcome.html",
                    username = myUsername)


@app.route("/login")
def authenticate():
    if request.form["username"] == myUsername and request.form["password"] == myPassword:
        session['logged?'] = 't'
        return render_template("welcome.html",
                        username = myUsername)
    else:
        return render_template("response.html",
                            teamName = teamName,
                            teamMembers = teamMembers,
                            name = request.args['name'],
                            donation = request.args['donation'],
                            method = request.method
    )

@app.route("/logout")
def logout():
    return render_template("logout.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
