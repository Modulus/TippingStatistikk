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

    start_date = time.strptime(str(start_date_string), "%Y-%m-%d")
    end_date = time.strptime(str(end_date_string), "%Y-%m-%d")
    most_common = request.args.get("most_common", default="true")
    most = True
    if most_common:
        if most_common == "true":
            most = True
        else:
            most = False

    game = request.args.get("game", default="lotto")

    name = (" {0} nummer".format(get_game_name(url_map.get(game))))

    resolution_text = request.args.get("resolution", default="low")

    resolution = 8

    if resolution_text == "medium":
        resolution = 9
    elif resolution_text == "high":
        resolution = 10
    permutations = []

    if game == "lotto":
        permutations = extract(7, resolution, start_date, end_date, url_map.get(game), most_common=most)
    elif game == "viking_lotto":
        permutations = extract(6, resolution-1, start_date, end_date, url_map.get(game), most_common=most)
    else:
        permutations = extract(7, resolution, start_date, end_date, url_map.get(game), most_common=most)

    permutations.sort()

    data = Data(start_date, end_date, name, permutations)
    return jsonify(data.json())


@app.route("/", methods=["GET"])
def get_view():
    return render_template("index.html")


@app.route("/extra", methods=["GET"])
def get_extra():
    return render_template("extra.html")


@app.route("/viking", methods=["GET"])
def get_viking():
    return render_template("viking.html")


@app.route("/keno", methods=["GET"])
def get_keno():
    return render_template("keno.html")


@app.route("/book", methods=["GET"])
def get_bookview():
    return render_template("book.html")


@app.route("/about", methods=["GET"])
def get_aboutview():
    return render_template("about.html")


if __name__ == "__main__":
    #Visible on the network
    app.run(debug=True, host="0.0.0.0", port=8080)

    #Local access only
    # app.run(debug=True)