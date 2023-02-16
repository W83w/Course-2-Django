from flask import Flask
import json
import utils

app = Flask(__name__)

candidates = utils.load_candidates()

#############


@app.route("/")
def page_index():
    str_candidates = '<pre>'
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
    str_candidates += "</pre>"
    return str_candidates


@app.route("/candidates/<int:id>")
def profile(id):
    candidate = candidates[id]
    str_candidates = f"<img src={candidate['picture']}></img><br>{candidate['name']}<br>{candidate['position']}" \
                      f"<br>{candidate['skills']}<br>\n\n"

    return str_candidates


@app.route("/skills/<skill>")
def skills(skill):
    str_candidates = '<pre>'
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        print(candidate_skills)
        if skill in candidate_skills:
            str_candidates += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']}\n\n"
    str_candidates += '</pre>'

    return str_candidates

app.run(debug=True)
