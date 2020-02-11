from flask import Flask, render_template, Response, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from flask import current_app as current_app
import dbModule
import re

app = Flask(__name__, template_folder="templates")

app.config['GOOGLEMAPS_KEY'] = "AIzaSyCYsvWvFTrZTWyS81JJiEeHMXXlFgTtxLY"
GoogleMaps(app)

db_class = dbModule.Database()

@app.route('/data', methods=['GET'])
def data():
    lat = request.args.get('req_lat')
    lng = request.args.get('req_lng')
    t1 = request.args.get('req_t1')
    t2 = request.args.get('req_t2')
    h = request.args.get('req_h')
    
    #print(lat,",",lng)

    sql = """insert into data(lat, lng, t1, t2, h) values (%s, %s, %s, %s, %s)"""
    db_class.execute(sql, (lat, lng, t1, t2, h))
    db_class.commit()

    return render_template('insert.html')


center_lat=37.557402
center_lng=127.045322

# gps_list=[(), (), ()] 이렇게 받아와서 Map의 markers에 대입할 것


@app.route('/')
def index():

    ##### map #####
    sql = """select lat, lng from data"""
    row = db_class.executeAll(sql)

    #### table ####
    sql2 = "select * from data"
    row2 = db_class.executeAll(sql2)

    print("@@@@ ", row2)

    ##### cnt #####
    db_class.execute("select count(*) from data")
    #cnt = (list(db_class.cursor))
    cnt = db_class.cursor.fetchone()
    cnt = re.findall('\d', str(cnt)).__getitem__(0)
    cnt = int(cnt)

    gps_list=[]

    # cnt 포함 X
    for i in range(0, cnt):
        row_lat = re.findall('\d+.\d+', str(row).split(",")[i*2]).__getitem__(0)
        row_lng = re.findall('\d+.\d+', str(row).split(",")[i*2+1]).__getitem__(0)
        row_lat = float(row_lat)
        row_lng = float(row_lng)

        gps_list.append((row_lat, row_lng))
        print(gps_list)

    sndmap = Map(
        style="height: 450px; width: 1150px;",
        identifier="sndmap",
        varname="sndmap",
        zoom=15, #13
        # 추후 idx 0값을 center lat lng으로 설정할 것
        lat=center_lat,
        lng=center_lng,
        markers=gps_list
    )

    return render_template('index.html', sndmap=sndmap, GOOGLEMAPS_KEY=request.args.get('apikey'), row2=row2, len=len(row2))


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0,0,0,0', port=5000, debug=True)