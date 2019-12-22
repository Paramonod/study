import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import constants
import json
from objects import WeatherStat, Weather
from constants import db_password, db_user, db_host, db_name


def build_tables():
    con_str = 'postgresql://{user}:{password}@{host}/{name}'.format(user=db_user, password=db_password, host=db_host,
                                                                    name=db_name)
    engine = create_engine(con_str, echo=True, connect_args={'options': '-csearch_path={}'.format('data')})
    constants.Session.configure(bind=engine)
    constants.session = constants.Session()


def get_stat_chart():
    res = []
    for days in constants.session.query(WeatherStat.days):
        res += [[['day 1', 'day 2', 'day 3', 'day 4', 'day 5'], json.loads(days[0])]]
        print(json.dumps(res))
    return res


def get_stat_cards():
    res = []
    i = 1
    row = []
    for city, mean, median in constants.session.query(WeatherStat.city, WeatherStat.mean, WeatherStat.median):
        if i - 1 % 3 == 0:
            res += [row]
            row = []
        row += [{'name': 'websiteViewsChart' + str(i), 'mean': mean, 'median': median, 'city': city}]
        i += 1
    if row:
        res += [row]
    print(res)
    return res


def get_stat_num():
    return constants.session.query(func.count(WeatherStat.id)).scalar()


def add_stat_city(name, mean, median, days):
    name = str(name).capitalize()
    newd = []
    try:
        mean = float(mean)
        median = float(median)
        newd = json.loads(days)
    except Exception:
        return False
    if len(newd) != 5:
        return False
    if constants.session.query(WeatherStat).filter(WeatherStat.city == name).count() == 0:
        city = WeatherStat(city=name, mean=mean, median=median, days=days)
        constants.session.add(city)
    else:
        city = constants.session.query(WeatherStat).filter(WeatherStat.city == name)[0]
        city.mean = mean
        city.median = median
        city.days = days
    constants.session.commit()
    return True


def get_weather_chart():
    res = []
    for days in constants.session.query(Weather.days):
        res += [[['day 1', 'day 2', 'day 3', 'day 4', 'day 5'], json.loads(days[0])]]
        print(json.dumps(res))
    return res


def get_weather_cards():
    res = []
    i = 1
    row = []
    for city in constants.session.query(Weather.city):
        city = city[0]
        if i - 1 % 3 == 0:
            res += [row]
            row = []
        row += [{'name': 'websiteViewsChart' + str(i), 'city': city}]
        i += 1
    if row:
        res += [row]
    print(res)
    return res


def get_weather_num():
    return constants.session.query(func.count(Weather.id)).scalar()


def add_weather_city(name, days):
    newd = []
    try:
        newd = json.loads(days)
    except Exception:
        return False
    if len(newd) != 5:
        return False
    if constants.session.query(Weather).filter(Weather.city == name).count() == 0:
        city = Weather(city=name, days=days)
        constants.session.add(city)
    else:
        city = constants.session.query(Weather).filter(Weather.city == name)[0]
        city.days = days
    constants.session.commit()
    return True
