# Flask is used for microservices
from flask import Flask
from flask import render_template # needed when using html templates
import json

import retriever

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
    <a href='http://127.0.0.1:5000/weather'>Weather</a> |
    <a href='http://127.0.0.1:5000/location'>Location</a>
    '''
    return content_html

# declare some routes (part of uS webserver)
@app.route('/home') # this is the homepage
def home():
    content_html = '''
    <h2>Welcome to Tushar's We-Lo (Weather and Location) App</h2>
    <a href='http://127.0.0.1:5000/weather'>Weather</a> |
    <a href='http://127.0.0.1:5000/location'>Location</a>
    '''
    return content_html

@app.route('/weather') # calls the weathergetter
@app.route('/weather/<city>') # calls the weathergetter
def weather(city='athlone'):
    #return render_template('weather.html', city=city)
    wg = retriever.WeatherGetter(city)
    wg.getData()

# a route which returns json
@app.route('/location') # an API REST end-point
@app.route('/location/<city>') # another API REST end-point
def location(city='athlone'): #  provide default param values
    struct = {'city':city, 'age':39, 'member':True}
    strcut_j = json.dumps(struct) # json typify the data
    s = json.loads(strcut_j) # convert json back to struct
    return struct # Flask will auto-convert to json

    return render_template('location.html', city=city)

@profile
def main():
    cities = ['athlone','belfast','cork','dublin','edenderry','frankfurt','galway','houston','istanbul','jakarta','kolkata','london','mumbai','nairobi','ottawa','paris','quebec']
    for c in cities:
        wg = retriever.WeatherGetter(c)
        wg.getData()
    app.run()
    #app.run(host='192.168.0.1')

if __name__ == '__main__':
    main()

