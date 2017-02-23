from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	# print session.get('times')
	import random
	session['random'] = random.randrange(0, 101)
	 


	return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
	print "Got Post Info" # we'll talk about the following two lines after we learn a little more about forms
	session['user_number'] = int(request.form['someKey'])
	# print session['user_number']
	if session['random'] > session['user_number']:
		session['result'] = 'low'
		session['text'] = 'too low'
	elif session['random'] < session['user_number']:
		session['result'] = 'high'
		session['text'] = 'too high'
	else:
		session['result'] = 'equal'
		session['text'] = 'was the number!'
	return redirect('/show')
	 

@app.route('/show')
def show_user():
	return render_template('user.html')







app.run(debug=True) 