from flask import Flask, request, jsonify, render_template
from rrr import *

flask_app = Flask(__name__)

@flask_app.route("/")
def Home():
    return render_template("index.html")



@flask_app.route("/predicts", methods = ["POST"])
def predicts():
    data=[str(x) for x in request.form.values()]
    return render_template("index.html",text=s)
                           

if __name__ == "__main__":
    flask_app.run(debug=True)

