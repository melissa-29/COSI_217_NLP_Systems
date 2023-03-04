from flask import Flask, request
from flask_restful import Resource, Api
from ner import get_entities, get_entities_with_markup

app = Flask(__name__)
api = Api(app)

class access_spacy_NER(Resource):

    def get(self):
        return {'NER task': 'Takes a .txt file with as input and returns the corresponding NER information.'}

    def post(self):
        text = request.get_data(as_text=True)
        entities = get_entities(text)
        return {'entities': entities}, 201

api.add_resource(access_spacy_NER, '/api')

if __name__ == '__main__':
    app.run()

