#!usr/bin/python3


from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

def add_user(username, email):
    try:
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to add user: {str(e)}"}), 500

def list_users():
    users = User.query.all()
    user_info = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
    return jsonify(user_info), 200
