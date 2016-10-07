from flask import Flask, session, render_template, redirect
app = Flask(__name__)

app.secret_key = 'TurtlesInAHalfShellTurtlePower'

@app.route('/')
def index():
	if not 'hide' in session:
		session['hide'] = "show"
	return render_template("index.html")

@app.route('/ninja')
def catchGroup():
	#This didDraw boolean keeps track of whether or not the user is coming from another page
	if not 'didDraw' in session:
		session['didDraw'] = True	
	if not 'color' in session or session['didDraw'] == True:
		session['color'] = "all"
	session['didDraw'] = True
	return render_template('ninja.html')


@app.route('/ninja/<ninja_color>')
def display_ninja(ninja_color):
	colors = ["blue", "orange", "red", "purple"]
	if  ninja_color in colors:
		session['color'] = ninja_color
	else:
		session['color'] = "april"
	session['didDraw'] = False
	return redirect('/ninja')


app.run(debug=True)