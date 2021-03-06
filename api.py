from flask import Flask
from flask_restful import Resource, Api
import requests, json
import random
import os
app = Flask(__name__)
api = Api(app)
url = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all"

class GetDogFact(Resource):
    def get(self):
        fact_list = requests.get(url).json()
        random_fact = random.choice(fact_list)['fact']
        return {'fact': str(random_fact)}

api.add_resource(GetDogFact, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)