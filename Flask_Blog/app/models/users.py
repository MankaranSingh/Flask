from .. import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model, UserMixin ):

    __tablename__ = 'roles'

    role_name =  db.Column(db.String(50), unique = True)
    id = db.Column(db.Integer, primary_key = True)
    users = db.relationship('User' , backref = 'role', lazy = 'dynamic' )

    
        
                

class User(db.Model):

    __tablename__ = 'users'
    
    username = db.Column(db.String(50), unique = True, nullable = False)
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    role_id = db.Column(db.Integer , db.ForeignKey('roles.id'))
    email = db.Column(db.String(120), unique= True, nullable = False)
    password = db.Column(db.String(120), nullable = False)

    

        
    
