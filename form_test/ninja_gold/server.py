from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if 'total' not in session:
		session['total'] = 0

	return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def create_user():
	print "Got Post Info" 

	if request.form['building'] == 'farm':
		points = random.randrange(10,20)
		session['total'] = session['total'] + points
		return redirect('/')

	elif request.form['building'] == 'cave':
		points = random.randrange(5,10)
		session['total'] = session['total'] + points
		return redirect('/')
	
	elif request.form['building'] == 'house':
		points = random.randrange(2,5)
		session['total'] = session['total'] + points
		return redirect('/')

	elif request.form['building'] == 'casino':
		points = random.randrange(-50,50)
		session['total'] = session['total'] + points
		return redirect('/')

	return redirect('/')
	 
	 

# @app.route('/show')
# def show_user():
# 	return render_template('user.html')







app.run(debug=True) 