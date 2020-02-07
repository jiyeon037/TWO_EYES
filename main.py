from flask import Flask, render_template, Response, request
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
#import folium

#app = Flask(__name__)
app = Flask(__name__, template_folder="templates")
Bootstrap(app)

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = ""

# you can also pass key here
GoogleMaps(
    app,
)


@app.route('/')
def index():

    sndmap = Map(
        style="height:450px;width:1200px;",
        identifier="sndmap",
        varname="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419), (37.4500, -122.1350), (37.4300, -122.1400, "Hello World")]
    )
        
    return render_template('index.html', sndmap=sndmap, GOOGLEMAPS_KEY=request.args.get('apikey'))



'''
@app.route('/test', method=['GET', 'POST'])
def test():
    if request.method =='GET':
        return render_template('post.html')
    elif request.method =='POST':
        value = request.form['test']
        return render_template('default.html')
'''

if __name__ == '__main__':
    app.run(debug=True)