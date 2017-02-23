from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	print session.get('times')

	if session.get('times') == None:
		session['times'] = 1
	else:
		session['times'] += 1


	return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info" # we'll talk about the following two lines after we learn a little more about forms
    session['times'] = request.form['times']
    
    return redirect('/show')
	

@app.route('/show')
def show_user():
	return render_template('user.html', times=session['times'])




 


app.run(debug=True) 