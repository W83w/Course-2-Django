from flask import Flask, render_template
from  utils import  load_candidates_from_json

app = Flask(__name__)

data = load_candidates_from_json('candidates.json')

@app.route("/")
def index():
    return render_template('index.html', candidates=data)

app.run(debug=True)