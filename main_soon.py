from flask import Flask, render_template, Response, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from flask import current_app as current_app
import dbModule, getParams, makeFunc
import re

app = Flask(__name__, template_folder="templates")

app.config['GOOGLEMAPS_KEY'] = "AIzaSyCYsvWvFTrZTWyS81JJiEeHMXXlFgTtxLY"
GoogleMaps(app)

db_class = dbModule.Database()
getparams = getParams.Data()
makefunc = makeFunc.Func()

@app.route('/data', methods=['GET'])
def data():
    return getparams.get_data()

# gps_list=[(), (), ()] 이렇게 받아와서 Map의 markers에 대입할 것

@app.route('/')
def index():
    return makefunc.using_func()


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000, debug=True)