from flask import Flask, render_template, Response
from flask_bootstrap import Bootstrap
#import folium

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
   # start_coords = (46.9540700, 142.7360300)
   # folium_map = folium.Map(location=start_coords, zoom_start=14)
    return render_template('index.html')

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