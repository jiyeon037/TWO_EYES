import dbModule
import re
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from flask import render_template, request

db_class = dbModule.Database()

class Func():

    def using_func(self):
        #### map, table ####
        sql = "select * from data"
        row = db_class.executeAll(sql)

        ##### cnt #####
        db_class.execute("select count(*) from data")
        cnt = db_class.cursor.fetchone()
        cnt = int(re.findall('\d', str(cnt)).__getitem__(0))

        gps_list=[]

        # cnt 포함 X
        for i in range(0, cnt): 
            row_lat = float(row[i].get('lat'))
            row_lng = float(row[i].get('lng'))
            gps_list.append((row_lat, row_lng))
        
        print("@@@@@@@, ", row)
        print(gps_list)

        sndmap = Map(
            style="height: 450px; width: 1150px;",
            identifier="sndmap",
            varname="sndmap",
            zoom=15, #13
            # 추후 idx 0값을 center lat lng으로 설정할 것
            lat=row[0].get('lat'),
            lng=row[0].get('lng'),
            markers=gps_list
        )

        return render_template('index.html', sndmap=sndmap, GOOGLEMAPS_KEY=request.args.get('apikey'), row=row, len=len(row))