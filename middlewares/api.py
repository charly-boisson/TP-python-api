from flask import jsonify, abort, make_response, request, url_for
from service.CandidateService import CandidateService

db_engine = 'sqlite:////Users/charlyboisson/Documents/MYDIGITALSCHOOL/COURS/PYTHON/tp-python-api/db/bdd_python.db'
DATA_PROVIDER = CandidateService(db_engine)

# Candidat
def get_candidates(serialize=True):
    # Récupère les candidats
    candidates = DATA_PROVIDER.get_candidate(serialize=True)
    if candidates:
        # Si c'est pour l'api on serialise
        if serialize:
            return jsonify(candidates)
        # Sinon on retourne le tableu des candidats pour l'affichage
        else:
            return candidates
    else:
        return abort(404)

def get_candidat(id):
    if type(id) == int:
        candidate = DATA_PROVIDER.get_candidate(id,serialize=True)
        if candidate:
            return jsonify(candidate)
        else:
            return abort(404)
    else:
        return abort(400)

def add_candidat():

    first_name = request.form['first_name']
    last_name = request.form['first_name']
    email = request.form['first_name']

    if  first_name is not None and last_name is not None and email is not None:
        candidate_id = DATA_PROVIDER.add_candidate(first_name,last_name,email)
        if candidate_id:
            resp = {
                "id": candidate_id,
                "url": url_for('get_candidate',id=candidate_id),
             }
            return make_response(jsonify(resp), 201)
        else:
            return abort(500)
    else:
        return abort(400)

def delete_candidat(id):
    deletecandidat = DATA_PROVIDER.delete_candidate(id)
    print(deletecandidat)
    if deletecandidat:
        resp = { "message": "Candidat supprimé !" }
        return make_response(jsonify(resp), 200)
    else:
        return abort(404)

def update_candidat(id):
    if type(id) == int:
        new_candidate = {
            'first_name': request.form['first_name'],
            'last_name': request.form['first_name'],
            'email': request.form['first_name'],
        }
        candidate = DATA_PROVIDER.update_candidate(id,new_candidate)
        if candidate:
            # return jsonify(candidate)
            resp = { "message": "Candidat mis à jour !" }
            return jsonify(resp)
        else:
            return abort(404)
    else:
        return abort(400)

# Interview
def get_interviews(serialize=True):
    interviews = DATA_PROVIDER.get_interview(serialize=True)
    if interviews:
        if serialize:
            return jsonify(interviews)
        else:
            return interviews
    else:
        return abort(404)

def get_interview(id):
    if type(id) == int:
        interview = DATA_PROVIDER.get_interview(id,serialize=True)
        if interview:
            return jsonify(interview)
        else:
            return abort(404)
    else:
        return abort(400)

# Position
def get_positions(serialize=True):
    positions = DATA_PROVIDER.get_position(serialize=True)
    if positions:
        if serialize:
            return jsonify(positions)
        else:
            return positions
    else:
        return abort(404)

def get_position(id):
    if type(id) == int:
        position = DATA_PROVIDER.get_position(id,serialize=True)
        if position:
            return jsonify(position)
        else:
            return abort(404)
    else:
        return abort(400)

# DB
def init_database():
    DATA_PROVIDER.init_database()
    resp = { "message": "Instanciation BDD reussis !" }
    return jsonify(resp)

def fill_database():
    DATA_PROVIDER.fill_database()
    resp = { "message": "Creation des jeux de donnees de la BDD reussis !" }
    return jsonify(resp)
