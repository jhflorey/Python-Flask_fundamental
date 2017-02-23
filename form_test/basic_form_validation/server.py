from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def index():
  return render_template('index.html')





@app.route('/process', methods=['Post'])
def process():
	if len(request.form ['name']) < 1:
		#display validation errors
	else:
		#display success message
  
  return redirect('/')















app.run(debug=True)
