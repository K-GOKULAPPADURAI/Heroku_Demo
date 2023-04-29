from flask import Flask, request, jsonify, render_template
from rrr import *
s=str(predictor('archive/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/104_1b1_Pr_sc_Litt3200.wav'))
  
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

