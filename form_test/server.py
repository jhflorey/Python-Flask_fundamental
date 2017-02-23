from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info" # we'll talk about the following two lines after we learn a little more about forms
    your_name = request.form['name']
    dojo_location = request.form['location'] # redirects back to the '/' route
    favorite_language = request.form['language']
    comment = request.form['comment']
    return render_template('result.html', name= request.form['name'], location= request.form['location'], language= request.form['language'], comment= request.form['comment'])

# @app.route('/result')
# def result():
#  return render_template('result.html') 	

@app.route('/show')
def show_user():
  return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')









app.run(debug=True) # run our server