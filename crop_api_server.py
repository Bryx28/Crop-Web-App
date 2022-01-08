from flask import Flask, jsonify, request
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import desc

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CropDatabase.sqlite'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(server)
ma = Marshmallow(server)

class User(db.Model, UserMixin):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    user_image = db.Column(db.String(20), nullable=False, default='default.jpg')
    user_fname = db.Column(db.String(50), nullable=False)
    user_mname = db.Column(db.String(50), nullable=False)
    user_lname = db.Column(db.String(50))
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def  __repr__(self):
        return f"User({self.username} - {self.user_fname} {self.user_lname})"

db.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "user_image", "user_fname", "user_mname", 
                "user_lname", "username", "email", "password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@server.route('/create', methods=['POST'])
def create():
    user_fname = request.json.get('user_fname')
    user_mname = request.json.get('user_mname')
    user_lname = request.json.get('user_lname')
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')

    new_user = User(user_fname = user_fname, 
                    user_mname = user_mname, 
                    user_lname = user_lname,
                    username = username,
                    email = email,
                    password = password)
    
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@server.route('/existing_username/<username>', methods=['GET'])
def existing_username(username):
    exist = User.query.filter_by(username=username).first()
    user = user_schema.dump(exist)
    return user_schema.jsonify(user)

@server.route('/existing_email/<email>', methods=['GET'])
def existing_email(email):
    exist = User.query.filter_by(email=email).first()
    user = user_schema.dump(exist)
    return user_schema.jsonify(user)

@server.route('/load_user/<user_id>', methods=['GET'])
def load_user(user_id):
    exist = User.query.get(int(user_id))
    user  = user_schema.dump(exist)
    return user_schema.jsonify(user)

@server.route('/update_account/<user_id>', methods=['PUT'])
def update_account(user_id):
    account_record = User.query.get(int(user_id))

    user_image = request.json.get('user_image')
    user_fname = request.json.get('user_fname')
    user_mname = request.json.get('user_mname')
    user_lname = request.json.get('user_lname')
    username = request.json.get('username')
    email = request.json.get('email')
    
    account_record.user_image = user_image
    account_record.user_fname = user_fname
    account_record.user_mname = user_mname
    account_record.user_lname = user_lname
    account_record.username = username
    account_record.email = email

    db.session.commit()

    return user_schema.jsonify(account_record)

if __name__ == "__main__":
    server.run(debug=True)