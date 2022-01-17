from flask_sqlalchemy_session import current_session
from models import User


def list_all():
    print('session', id(current_session))
    return current_session.query(User).all()

def save(user: User):
    print('session', id(current_session))
    current_session.add(user)
    current_session.flush()
    session.refresh(user)
    
    return user