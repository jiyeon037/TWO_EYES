from flask import Flask, render_template, Response, request
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from flask import current_app as current_app
from module import dbModule

app = Flask(__name__, template_folder="templates")
Bootstrap(app)

app.config['GOOGLEMAPS_KEY'] = ""
GoogleMaps(app)

sch_lat=37.557402
sch_lng=127.045322

@app.route('/')
def index():
    sndmap = Map(
        style="height: 450px; width: 1200px;",
        identifier="sndmap",
        varname="sndmap",
        zoom=16, #13
        lat=37.557402,
        lng=127.045322,
        markers=[(37.557402, 127.045322), (37.556402, 127.046022, "Hello World")]
    )

    db_class = dbModule.Database()
    sql = """insert into gps(lat, lng) values (%s, %s)"""
    db_class.execute(sql, (sch_lat, sch_lng))
    db_class.commit()

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