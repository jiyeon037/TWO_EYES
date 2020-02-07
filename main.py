from flask import Flask, render_template, Response, request
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from flask import current_app as current_app
from module import dbModule

app = Flask(__name__, template_folder="templates")
Bootstrap(app)

app.config['GOOGLEMAPS_KEY'] = "AIzaSyCYsvWvFTrZTWyS81JJiEeHMXXlFgTtxLY"
GoogleMaps(app)

center_lat=37.557402
center_lng=127.045322

# gps_list=[(), (), ()] 이렇게 받아와서 Map의 markers에 대입할 것


@app.route('/gps', methods=['GET'])
def gps():
    lat = request.args.get('req_lat')
    lng = request.args.get('req_lng')

    print(lat)
    print(lng)

    db_class = dbModule.Database()
    sql = """insert into gps(lat, lng) values (%s, %s)"""
    db_class.execute(sql, (lat, lng))
    db_class.commit()

    return render_template('insert.html', req_lat=lat, req_lng=lng)


@app.route('/')
def index():
    sndmap = Map(
        style="height: 450px; width: 1200px;",
        identifier="sndmap",
        varname="sndmap",
        zoom=16, #13
        lat=center_lat,
        lng=center_lng,
        markers=[(center_lat, center_lng), (37.556402, 127.046022)]
    )

    return render_template('index.html', sndmap=sndmap, GOOGLEMAPS_KEY=request.args.get('apikey'))


if __name__ == '__main__':
    app.run(debug=True)