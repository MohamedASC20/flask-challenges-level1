from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Mohameds Raibow Project'

@app.route('/red')
def red():
    return render_template('red.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')