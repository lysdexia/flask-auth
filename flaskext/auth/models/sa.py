"""
Module to provide plug-and-play authentication support for SQLAlchemy.
"""

import datetime
from sqlalchemy import Column, Integer, String, DateTime
from flaskext.auth import AuthUser, get_current_user_data

def get_user_class(declarative_base):
    """
    Factory function to create an SQLAlchemy User model with a declarative 
    base (for example db.Model from the Flask-SQLAlchemy extension).
    """
    class User(declarative_base, AuthUser):
        """
        Implementation of User for SQLAlchemy.
        """
        id = Column(Integer, primary_key=True)
        email = Column(String(254), unique=True, nullable=False)
        password = Column(String(120), nullable=False)
        salt = Column(String(80))
        role = Column(String(80))
        created = Column(DateTime(), default=datetime.datetime.utcnow)
        modified = Column(DateTime())

        def __init__(self, *args, **kwargs):
            super(User, self).__init__(*args, **kwargs)
            password = kwargs.get('password')
            if password is not None and not self.id:
                self.created = datetime.datetime.utcnow()
                # Initialize and encrypt password before first save.
                self.set_and_encrypt_password(password)

        def __getstate__(self):
            return {
                'id': self.id,
                'email': self.email,
                'role': self.role,
                'created': self.created,
                'modified': self.modified,
            }

        @classmethod
        def load_current_user(cls, apply_timeout=True):
            data = get_current_user_data(apply_timeout)
            if not data:
                return None
            return cls.query.filter(cls.email==data['email']).one()

    return User
