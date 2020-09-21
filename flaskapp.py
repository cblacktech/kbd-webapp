from flask import Flask, render_template, url_for, request, redirect, abort
from flask_talisman import Talisman
from time import sleep
import logging
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
app.config['SECRET_KEY'] = 'sdfbW%$EYGHw$%Hwe4r'

csp = {
    'default-src': [
        '\'self\'',
    ]
}
talisman = Talisman(app, force_https=True, content_security_policy=csp)


# app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))
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
@talisman(
    frame_options='ALLOW_FROM',
    fram_options_allow_from='https://kbd-app.herokuapp.com/',
)
def display():
    text = ""
    cnt = 3

    text += ('-' * 25 * cnt) + '\n'
    text += ('|' + '  ****            ****  ') * cnt + '|\n'
    text += ('|' + ' *    **        **    * ') * cnt + '|\n'
    text += ('|' + '  *      **  **      *  ') * cnt + '|\n'
    text += ('|' + '   *       **       *   ') * cnt + '|\n'
    text += ('|' + '    *              *    ') * cnt + '|\n'
    text += ('|' + '     *            *     ') * cnt + '|\n'
    text += ('|' + '      *          *      ') * cnt + '|\n'
    text += ('|' + '       *        *       ') * cnt + '|\n'
    text += ('|' + '        *      *        ') * cnt + '|\n'
    text += ('|' + '         *    *         ') * cnt + '|\n'
    text += ('|' + '          *  *          ') * cnt + '|\n'
    text += ('|' + '           **           ') * cnt + '|\n'
    text += ('-' * 25 * cnt) + '\n'
    # print(text_list)
    return render_template('display.html', title="Display Page", style="display.css",
                           top_text="HAPPY BIRTHDAY !!!!", text=text)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=port)
