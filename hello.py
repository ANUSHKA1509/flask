from flask import Flask, render_template

# Create Flask instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

def index():
	return render_template("index.html") 

# localhost:5000/user/John 
@app.route('/user/<name>')
def user(name):
	return render_template("user.html", user_name=name) 
	#return "<h1>Hello {}</h1>".format(name)