import dbModule
from flask import render_template, request

db_class = dbModule.Database()

class Data():
    def get_data(self):
        self.lat = request.args.get('req_lat')
        self.lng = request.args.get('req_lng')
        self.t1 = request.args.get('req_t1')
        self.t2 = request.args.get('req_t2')
        self.h = request.args.get('req_h')
        self.date = request.args.get('req_date')
        self.time = request.args.get('req_time')

        print(self.lat,", ",self.lng)

        sql = """insert into data(lat, lng, t1, t2, h, date, time) values (%s, %s, %s, %s, %s, %s, %s)"""
        db_class.execute(sql, (self.lat, self.lng, self.t1, self.t2, self.h, self.date, self.time))
        db_class.commit()

        return render_template('insert.html')