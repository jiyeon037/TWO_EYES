#-*- coding: utf-8 -*-

from flask import Flask, render_template, Response, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from flask import current_app as current_app
from flask_mail import Mail, Message
import dbModule
import re, os, datetime
import base64

app = Flask(__name__, template_folder="templates")

app.config['GOOGLEMAPS_KEY'] = "AIzaSyCYsvWvFTrZTWyS81JJiEeHMXXlFgTtxLY"
GoogleMaps(app)


UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', '587'))
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'twiceteam1@gmail.com') #이 계정 보안 풀어야했음
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'magiceco')
app.config['MAIL_USE_TLS'] = int(os.environ.get('MAIL_USE_TLS', True))
app.config['MAIL_USE_SSL'] = int(os.environ.get('MAIL_USE_SSL', False))

mail = Mail(app)

db_class = dbModule.Database()


@app.route('/email', methods=['POST'])
def email():
    name = request.form['name']
    email_address = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    msg = Message('A new message from TWICE', sender=email_address, recipients=['twiceteam3@gmail.com'])
    msg.body = "You have received a new message from your website contact form.\nHere are the details:\n\nName: %s\n\nEmail: %s\n\nPhone: %s\n\nMessage: %s" % (name, email_address, phone, message)
    mail.send(msg)
    return 'Sent'


@app.route('/data', methods=['GET'])
def getData():
    lat = request.args.get('req_lat')
    lng = request.args.get('req_lng')
    t1 = request.args.get('req_t1')
    t2 = request.args.get('req_t2')
    h = request.args.get('req_h')
    date = request.args.get('req_date')
    time = request.args.get('req_time')

    sql = """insert into data(lat, lng, t1, t2, h, date, time) values (%s, %s, %s, %s, %s, %s, %s)"""
    db_class.execute(sql, (lat, lng, t1, t2, h, date, time))
    db_class.commit()

    return 'Data'


@app.route('/image', methods=['POST'])
def postImage():
    file = request.files['file']
    if file:
        #filename = secure_filename(file.filename)
        filename = datetime.datetime.now().strftime('%y%m%d_%H%M%S')+'.jpg'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return 'Image'


@app.route('/')
def index():

    #### map, table ####
    sql = "select * from data order by date"
    row = db_class.executeAll(sql)

    ##### cnt #####
    db_class.execute("select count(*) from data")
    cnt = db_class.cursor.fetchone()

    #cnt = int(re.findall('\d', str(cnt)).__getitem__(0))
    cnt = cnt.get('count(*)')

    gps_list=[]

    # cnt 포함 X
    for i in range(0, cnt): 
       row_lat = float(row[i].get('lat'))
       row_lng = float(row[i].get('lng'))
       
       gps_list.append((row_lat, row_lng))
       #print(gps_list)

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)