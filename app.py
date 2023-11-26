import datetime
from flask import Flask, request, jsonify
import service

app = Flask(__name__)
# f1allseason = []
# f1season = {}
    


@app.route('/', methods=['GET'])
def index():
    return "Welcome to Formula 1 API, created by Fahrendra Khoirul Ihtada and Rizha Alfianita \n endpoint: \n /season/<year> \n /all-season \n /upcoming"

@app.route('/season/<int:year>', methods=['GET'])
def get_season(year):
    try:
        start = datetime.datetime.now()
        success, res = service.read_json(str(year))
        if success:
            end = datetime.datetime.now()
            print("Time taken: ", end - start)
            return jsonify(res)
        else:
            link_year = f"https://www.formula1.com/en/results.html/{year}/races.html"
            res = service.get_year(link_year)
            end = datetime.datetime.now()
            print("DONEEE")
            if res == []:
                return "Year not found : F1 only available from 1950 to current year"
            print("Time taken: ", end - start)
            return jsonify(res)
    except Exception as e:
        return jsonify(error=str(e)), 500  # Return the error message with a 500 status code


@app.route('/all-season', methods=['GET'])
def get_all_season():
    try:
        res = service.list_all_year("https://www.formula1.com/en/results.html/2023/races.html")  
        return jsonify(res)
    except Exception as e:
        return jsonify(error=str(e)), 500  # Return the error message with a 500 status code

@app.route('/upcoming', methods=['GET'])
def get_upcoming():
    return jsonify(service.get_upcoming())

@app.route('/circuit', methods=['GET'])
def get_circuit():
    return jsonify(service.get_circuit())



# @app.route('/start', methods=['GET'])
# def start():
#     f1allseason = service.list_all_year("https://www.formula1.com/en/results.html/2023/races.html")
#     print("List All Season DONE")
#     f1season = {}
#     for season in f1allseason:
#         if season['year'] not in f1season:
#             f1season[season['year']] = service.get_year(season['link'])
#             print(season['year'] + " DONE")
#     return jsonify(f1season)

if __name__ == '__main__':
    app.config['TIMEOUT'] = 20  # Set timeout to 10 seconds
    app.run(debug=False, host='0.0.0.0',port=10000)

