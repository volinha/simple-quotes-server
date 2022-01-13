import random
from flask import jsonify,request,Flask
from flask_cors import CORS, cross_origin
import pandas as pd

BuftoApi = Flask(__name__)
cors = CORS(BuftoApi)
BuftoApi.config['CORS_HEADERS'] = 'Content-Type'

df = pd.read_csv('finalQuotes.csv', names=['Speakers', 'Quotes'])

def get_random_quote():
    rq = random.randint(0, len(df))
    speaking = df.values[rq][0]
    quote = df.values[rq][1]
    quote_obj = {"speaker": speaking, "quote": quote}
    return quote_obj

@cross_origin()
@BuftoApi.route('/', methods=['GET'])
def dashboard():
    return jsonify(get_random_quote())

if __name__ == '__main__':
    BuftoApi.run(host= '127.0.0.1',port=5000)
