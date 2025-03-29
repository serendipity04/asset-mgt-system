from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app
from sqlalchemy import event
from flask_login import UserMixin
from . import db, loginManager


@loginManager.user_loader
def load_user(id):
    return Employee.query.get(int(id))

class Employee(UserMixin, db.Model):
    __tablename__ = 'Employee'
    id = db.Column(db.Integer, primary_key=True)
    employee_number = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    role_id = db.Column(db.Integer, db.ForeignKey('Role.id'))
    dept_id = db.Column(db.Integer, db.ForeignKey('Department.id'))
    date_joined = db.Column(db.DateTime, default=datetime.now)

    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'confirm': self.id})

    def confirm(self, token, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token, max_age=expiration)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'reset': self.id})

    @staticmethod
    def reset_password(token, new_password, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token, max_age=expiration)
        except:
            return False
        user = Employee.query.get(data.get('reset'))
        if user is None:
            return False
        user.password = new_password
        db.session.add(user)
        return True
    
    def generate_email_change_token(self, new_email):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps(
            {'change_email': self.id, 'new_email': new_email})
    
    def change_email(self, token, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token, max_age=expiration)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        db.session.add(self)
        return True
    
    @staticmethod
    def generate_employee_number(mapper, connection, target):
        if not target.employee_number:
            date_str = datetime.now().strftime("%Y")
            last_employee_id = 0 if len(db.session.query(Employee).filter_by(dept=target.dept).all())==0 else db.session.query(Employee).filter_by(dept=target.dept).all()[-1].id
            last_employee_count = last_employee_id + 1
            target.employee_number = f"{target.dept.name}-{date_str}-{last_employee_count:03d}"

    def __repr__(self):
        return '<Employee %r>' % self.username

event.listen(Employee, "before_insert", Employee.generate_employee_number)


class Role(db.Model):
    __tablename__ = 'Role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('Employee', foreign_keys=[Employee.role_id], backref='role', lazy='dynamic')


    

    def __repr__(self):
        return '<Role %r>' % self.name


class Department(db.Model):
    __tablename__ = 'Department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    location = db.Column(db.String(64), nullable=False)
    users = db.relationship('Employee', foreign_keys=[Employee.dept_id], backref='dept', lazy='dynamic')

    def __repr__(self):
        return '<Dept %r>' % self.name

