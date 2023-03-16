import json

__data = [ ]

def load_candidates_from_json(path):
    global __data
    with open(path, 'r', encoding='utf-8') as file:
        __data = json.load(file)
    return __data

def get_candidate(candidate_id):
    pass

def get_candidates_by_name(candidate_name):
    pass

def get_candidates_by_skill(skill_name):
    pass
