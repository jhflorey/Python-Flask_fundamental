from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)


from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html", name="Ninja")
@app.route('/ninja')
def ninja():
    return render_template('ninja.html')


app.run(debug=True)
