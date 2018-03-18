from flask import Flask, jsonify, request
from pages_jaunes_france import PJ

app = Flask(__name__)

# incomes = [
#   { 'description': 'salary', 'amount': 5000 }
# ]


@app.route('/phones/')
def get_phones():
    query = 'pulido'
    location = 'bayonne'
    proximite = 0
    pj = PJ()
    pj.set_query(query)
    pj.set_location(location)
    pj.set_proximite(proximite)
    result = pj.search()

    return jsonify(result)