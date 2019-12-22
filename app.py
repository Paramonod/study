from flask import Flask, render_template, request
import constants
import db
from db import build_tables
from objects import WeatherStat

app = Flask(__name__)
build_tables()


@app.route('/')
def hello_world():
    return 'test'


@app.route('/weather', methods=['GET'])
def weather_get():
    return render_template('dashboard.html', city_num=db.get_weather_num(), chart_num=2, charts=db.get_weather_chart(),
                           rows=db.get_weather_cards())


@app.route('/weather', methods=['POST'])
def weather_post():
    days = request.form['days']
    city = request.form['city']
    return str(db.add_weather_city(city, days))


@app.route('/weatherstat', methods=['GET'])
def weatherstat_get():
    return render_template('dashboard.html', city_num=db.get_stat_num(), chart_num=2, charts=db.get_stat_chart(),
                           rows=db.get_stat_cards())


@app.route('/weatherstat', methods=['POST'])
def weatherstat_post():
    mean = request.form['mean']
    median = request.form['median']
    days = request.form['days']
    city = request.form['city']
    return str(db.add_stat_city(city, mean, median, days))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
