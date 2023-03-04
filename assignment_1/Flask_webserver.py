from flask import Flask, render_template, request
from ner import get_entities_with_markup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    text = request.form['text']
    entities = get_entities_with_markup(text)
    return render_template('results.html', text=text, entities=entities)

if __name__ == '__main__':
    app.run(debug=True)
