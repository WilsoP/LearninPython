from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def root():
	return "The default, 'root' route"

@app.route("/hello/")
def hello():
	return "Hello there"

@app.route("/goodbye/")
def goodbye():
	return "Goodbye cruel world"

@app.route("/general/")
def general():
	return "Genersl Kenobi"

@app.route("/private")
def private():
	#assume a test for user log in failed
	#so rdirect to log in user
	return redirect(url_for('login'))

@app.route("/login")
def login():
	return "Now we would get the username and password"

@app.errorhandler(404)
def page_not_found(error):
	return "You lost? We cant find this page",404


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

