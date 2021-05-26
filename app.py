from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__,template_folder='templates')
bootstrap = Bootstrap(app)



@app.route("/")
def home():
    return render_template('index.html')


@app.route("/music")
def music():
    return render_template('music.html')

@app.route("/arranger")
def arranger():
    return render_template('arranger.html')

@app.route("/voiceover")
def voiceover():
    return render_template('voiceover.html')


@app.route("/bandleader")
def bandleader():
    return render_template('bandleader.html')