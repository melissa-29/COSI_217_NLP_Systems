from collections import Counter
import db

from flask import Flask, render_template, request
from ner import SpacyDocument

app = Flask(__name__)
connection = db.DatabaseConnection('entity_counts.sqlite')
connection.create_schema()

@app.route('/')
def home():
    default_text = "When Sebastian Thrun started working on self-driving " \
                   "cars at Google in 2007, few people outside of the " \
                   "company took him seriously. \"I can tell you " \
                   "very senior CEOs of major American car companies " \
                   "would shake my hand and turn away because I wasn't " \
                   "worth talking to,\" said Thrun, in an interview " \
                   "with Recode earlier this week."
    all_ents = connection.get()
    return render_template('home.html', default_text=default_text, all_ents=all_ents)


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        text = request.form['text']
        spacy_doc = SpacyDocument(text)
        ents = [tup[2] for tup in spacy_doc.get_entities()]
        print(ents)
        for ent, count in Counter(ents).items():
            connection.add(ent, count)
        marked_ents = spacy_doc.get_entities_with_markup()
        return render_template('results.html', ents=ents, marked_ents=marked_ents)
    else:
        ents = request.args.get('ents', type=list)
        marked_ents = request.args.get('marked_ents')
        print("marked_ents:", marked_ents)
        return render_template('results.html', ents=ents, marked_ents=marked_ents)


@app.route('/entities_count', methods=['GET', 'POST'])
def all_results():
    if request.method == 'POST':
        marked_ents = request.args.get('marked_ents')
        all_ents = connection.get()
        return render_template('entities_count.html', all_ents=all_ents, marked_ents=marked_ents)
    else:
        marked_ents = request.args.get('marked_ents')
        all_ents = connection.get()
        return render_template('entities_count.html', all_ents=all_ents, marked_ents=marked_ents)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
