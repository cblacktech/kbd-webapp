from flask import Flask, render_template, url_for, request, redirect, abort
from time import sleep
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfbW%$EYGHw$%Hwe4r'
# app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))
# app.config['DEBUG'] = True
# logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def countdown():
    if request.method == 'POST':
        print('GOT A POST REQUEST')
        print(request.get_json())
        # return redirect(url_for('display'))
        return redirect('/display')
    else:
        return render_template('countdown.html', title="Countdown", style='countdown.css', custom_js='countdown.js')

@app.route('/display')
def display():
    return render_template('display.html', title="Display Page", style="display.css", name="display page")
    # return "<script>alert('Hello There');</script>"

# @app.route('/', methods=['GET', 'POST'])
# def custom():
#     time = request.form.get('time', 180)

if __name__ == "__main__":
    app.run()
