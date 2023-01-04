from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/route<int:route_num>')
def route_info(route_num):
    return render_template('route_info.html',route_num=route_num)