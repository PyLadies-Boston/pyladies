from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/library')
def library():
    return render_template('library.html')

if __name__ == '__main__':
    app.run()
