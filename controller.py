from Babysitter import Babysitter
from Family import Family

from flask import jsonify, request
from app import db

# Get all mothers
def get_mothers():
    mothers = Family.query.all()
    return jsonify([{'id': mother.id, 'name': mother.name} for mother in mothers])

# Create a new mother
def create_mother():
    data = request.get_json()
    name = data.get('name')

    mother = Family(name=name)
    db.session.add(mother)
    db.session.commit()

    return jsonify({'message': 'Mother created successfully!', 'id': mother.id}), 201

# Get all babysitters
def get_babysitters():
    babysitters = Babysitter.query.all()
    return jsonify([{'id': babysitter.id, 'name': babysitter.name} for babysitter in babysitters])


