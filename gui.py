from flask import Flask, render_template, url_for,flash,redirect, request,session
import flask
import html_extractor
import os
from random import shuffle



app = Flask(__name__)
app.config["SECRET_KEY"] = "4ea43728bd6a06abbe62206c1c2213dc"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True



@app.route("/", methods=['GET', 'POST'])
def index():
    _files = [["select chapters",""]]
    cap = []
    flask.session['order'] = []
    flask.session['count'] = 0
    FILES = html_extractor.get_files()
    if request.method == "POST":
        cap = []
        cap.append(request.form.getlist('re'))
        cap.append(request.form.getlist('fu'))
        if not (cap == []):
            flask.session['caps'] = cap
            _files,k = html_extractor.get_html(cap)
            shuffle(k)
            flask.session['count'] = 0
            flask.session['order'] = k
        else:
            _files = [["select chapters",""]]
    return render_template("index.html",FILES = FILES,question=_files[0][0],ans=_files[0][0])


@app.route('/get_question', methods=['GET'])
def get_question(): 
   _direction = flask.request.args.get('direction')
   flask.session['count'] = flask.session['count'] + (1 if _direction == 'f' else - 1)
   pos = flask.session['order'][flask.session['count']]
   _files,a =html_extractor.get_html(flask.session['caps'])
   return flask.jsonify({'question':_files[pos][0],'ans':_files[pos][1], 'forward':str(flask.session['count']+1 < len(_files)), 'back':str(bool(flask.session['count']))})




if __name__ == "__main__":

    app.run(debug=True)