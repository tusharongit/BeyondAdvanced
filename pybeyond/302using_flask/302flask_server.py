# Flask is used for microservices
from flask import Flask
from flask import render_template # needed when using html templates
import json

from memory_profiler import profile

# declare an instance of flask called app
app = Flask(__name__)

# declare root (start of uS webserver)
@app.route('/') # this is the root of our app
def root():
    # we can write an html response
    content_html = '''
    <h1>We are at the root of this service</h1>
    <a href='http://127.0.0.1:5000/home'>Home</a> |
    <a href='http://127.0.0.1:5000/about'>About</a> |
    <a href='http://127.0.0.1:5000/data'>Data</a> |
    <a href='http://127.0.0.1:5000/hello'>Hello</a>
    '''
    return content_html

# declare some routes (part of uS webserver)
@app.route('/home') # this is the homepage
def home():
    content_html = '''
    <h2>Homepage content</h2>
    <a href='http://127.0.0.1:5000/about'>About</a> |
    <a href='http://127.0.0.1:5000/data'>Data</a> |
    <a href='http://127.0.0.1:5000/hello'>Hello</a>
    '''
    return content_html

@app.route('/about') # this is another page
def about():
    content_html = '''
    <h2>About page content</h2>
    <a href='http://127.0.0.1:5000/home'>Home</a> |
    <a href='http://127.0.0.1:5000/data'>Data</a> |
    <a href='http://127.0.0.1:5000/hello'>Hello</a>
    '''
    return content_html

# a route which returns json
@app.route('/data') # an API REST end-point
@app.route('/data/<age>') # another API REST end-point
@app.route('/data/<age>/<name>') # another API REST end-point
def data(age=39, name='Tushar'): #  provide default param values
    struct = {'name':name, 'age':age, 'member':True}
    strcut_j = json.dumps(struct) # json typify the data
    s = json.loads(strcut_j) # convert json back to struct
    return struct # Flask will auto-convert to json

# a route that accepts params
@app.route('/hello') # calls hello w/o param
@app.route('/hello/<name>') # calls hello expecting a param
def hello(name=None): #  provide default name
    return render_template('username.html', name=name)

@profile
def main():
    app.run()

if __name__ == '__main__':
    main()

