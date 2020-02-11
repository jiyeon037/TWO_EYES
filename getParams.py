import dbModule

db_class = dbModule.Database()

class Data():
    def get_data(self):
        self.lat = request.args.get('req_lat')
        self.lng = request.args.get('req_lng')
        self.t1 = request.args.get('req_t1')
        self.t2 = request.args.get('req_t2')
        self.h = request.args.get('req_h')

        #print(lat,",",lng)

        sql = """insert into data(lat, lng, t1, t2, h) values (%s, %s, %s, %s, %s)"""
        db_class.execute(sql, (lat, lng, t1, t2, h))
        db_class.commit()

        return render_template('insert.html')