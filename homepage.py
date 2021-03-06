from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html'), 200


@app.route('/loginin', methods=['GET', 'POST'])
def loginin():
    if request.method == 'POST':
        username = request.form.get('username')
        return redirect(url_for('index', usename=request.form['username']))
    else:
        return render_template('loginin.html')



@app.route('/loginin/<name>', methods=['GET', 'POST'])
def welcome(name):
	user = {'name':name}
	if name == 'none':
		return redirect(url_for('loginin'))
	else:
		return render_template('welcome.html', user=user)

@app.route('/billboard/')
def inherits_two():
    return render_template('billboard.html')

@app.route('/singer/')
def inherits_three():
    return render_template('singer.html')

@app.route('/singer/Taylor Swift')
def inherits_three0():
    return render_template('Taylor Swift.html')

@app.route('/classification/')
def inherits_four():
    return render_template('classification.html')

@app.route('/HOT !')
def display():
    return '<img src="'+url_for('static', filename='images/HOT!.png')+'"/>'

@app.route('/time')
def time():
    return render_template('time.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

