#Coby Sontag, William Lin
#SoftDev1 pd 2
#K24 
#2019-11-13

#Key: qel64kzuxUAJzn4Jb40ZL8o5PRS9BGfhbPaYH2Np
#https://api.nasa.gov/planetary/apod?api_key=qel64kzuxUAJzn4Jb40ZL8o5PRS9BGfhbPaYH2Np

from flask import Flask render_template
import json, urllib2
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib2.urlopen("URL HERE")
    response = u.read
    data = json.loads(response)
    return render_template("file.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
