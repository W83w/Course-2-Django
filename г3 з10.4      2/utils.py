import json
from pprint import pprint


def load_candidates():
    with open("candidates.json", 'r', encoding="utf-8") as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i["id"]] = i

        #pprint(candidates)
        return candidates

load_candidates()