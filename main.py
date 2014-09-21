# -*- coding: utf-8 -*-
from datetime import datetime
import time
from data_table import Data
from utilities.name_utils import get_game_name

__author__ = 'Modulus'

from utilities.number_extractor import extract
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

url_map = {
    "lotto": "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsLotto.htm",
    "viking_lotto": "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsVikingLotto.htm",
    "extra": "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsExtra.htm",
    "keno": "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsKeno.htm"
}


@app.route("/api/lotto", methods=["GET"])
def get_lotto_numbers():
    now = datetime.now()
    start_date_string = request.args.get("start_date", default="2004-06-20")
    end_date_string = request.args.get("end_date", default="2014-05-20")
    #start_date = request.args.get(datetime.date(datetime(start_date_string, "%Y-%m-%d")), default=datetime.date(datetime(1986, 01, 01)))
    #start_date = datetime.date(datetime(1986, 01, 01))
    #end_date = request.args.get(datetime.date(datetime(end_date_string, "%Y-%m-%d")), default=datetime.date(datetime(now.year, now.month, now.day)))
    #end_date = datetime.date(datetime(now.year, now.month, now.day))

    #start_date = datetime.date(datetime(start_date_string, "%Y-%m-%d"))
    #end_date = datetime.date(datetime(end_date_string, "%Y-%m-%d"))
    start_date = time.strptime(str(start_date_string), "%Y-%m-%d")
    end_date = time.strptime(str(end_date_string), "%Y-%m-%d")


    game = "lotto"
   # mport time#
#>>> time.strptime("30 Nov 00", "%d %b %y")
#time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
 #                tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)

    name = (" {0} nummer".format(get_game_name(url_map.get(game))))

    permutations = extract(7, 8, start_date, end_date, url_map.get(game))

    permutations.sort()

    data = Data(start_date, end_date, name, permutations)
    return jsonify(data.json())

@app.route("/api/lotto/least", methods=["GET"])
def get_least_picked_lotto():
    now = datetime.now()
    #start_date_string = request.args.get("start_date")
    #end_date_string = request.args.get("end_date")
    start_date = datetime.date(datetime(2004, 01, 01))
    end_date = datetime.date(datetime(2014, 01, 01))
    #game = request.args.get("game", default="lotto")

    name = (" {0} nummer".format(get_game_name(url_map.get("lotto"))))

    permutations = extract(7, 10,start_date, end_date, url_map.get("lotto"), most_common=False)

    permutations.sort()

    data = Data(start_date, end_date, name, permutations)
    return jsonify(data.json())

@app.route("/api/lotto/most", methods=["GET"])
def get_most_picked_lotto():
    now = datetime.now()
    #start_date_string = request.args.get("start_date")
    #end_date_string = request.args.get("end_date")
    start_date = datetime.date(datetime(2004, 01, 01))
    end_date = datetime.date(datetime(2014, 01, 01))
    #game = request.args.get("game", default="lotto")

    name = (" {0} nummer".format(get_game_name(url_map.get("lotto"))))

    permutations = extract(7, 10, start_date, end_date, url_map.get("lotto"), most_common=True)

    permutations.sort()

    data = Data(start_date, end_date, name, permutations)
    return jsonify(data.json())


@app.route("/", methods=["GET"])
def get_view():
    return render_template("index.html")


@app.route("/book", methods=["GET"])
def get_bookview():
    return render_template("book.html")


@app.route("/about", methods=["GET"])
def get_aboutview():
    return render_template("about.html")


def run():
    start_date = datetime.datetime(datetime(2010, 01, 01))

    current_date = datetime.now()

    urls = [
        "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsLotto.htm",
        "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsVikingLotto.htm",
        "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsExtra.htm",
        "https://www.norsk-tipping.no/miscellaneous/getNumberStatisticsKeno.htm"
    ]

    for index, url in enumerate(urls):

        print(" {0} numbers".format(get_game_name(url)))

        permutations = extract(7, 8, start_date, current_date, url)

        for value in permutations:
            print(value)

        print("\n")


if __name__ == "__main__":
    #Visible on the network
    app.run(debug=True, host="0.0.0.0", port=8080)

    #Local access only
    # app.run(debug=True)