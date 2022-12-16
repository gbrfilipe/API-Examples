from flask import Flask, make_response, jsonify, request
from countryinfo import CountryInfo

app = Flask(__name__)

@app.route('/', methods = ["GET"])

def get_country():
    country = request.args.get('country')
    co = CountryInfo(country).info()
    return make_response(
        jsonify(co
        )
    )

app.run() 
