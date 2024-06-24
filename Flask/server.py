from flask import Flask, request, render_template,redirect

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Polynomial Regression</h1><p>This is a simple polynomial regression model API!</p>"

@app.route('/flask', methods=['GET'])
def flask():
    return render_template('index.html')

#params
@app.route('/params/<score>', methods=['GET'])
def params(score):
    return f"Score is: {str(score)}"

#Query
@app.route('/query', methods=['GET'])
def query():
    name = request.args.get('name')
    return f"Name is: {name}"

# Middleware
@app.before_request
def before_request():
    # Implement middleware functionality here
    print('Before Request')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username != 'admin' and password != 'admin':
            return render_template('/home.html', name=username)
        else:
            return redirect('/login')
    
    return render_template('login.html')

app.run(port=5000,debug=True)