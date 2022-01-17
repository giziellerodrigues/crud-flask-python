# compose_flask/app.py
import os
from flask import Flask
from redis import Redis
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import scoped_session,sessionmaker

from repository import userrepository
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_CONFIG_URI')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

engine = createengine(DB_PATH) 
Session = sessionmaker(bind=engine) 
session = Session()

    
@app.teardown_appcontext
def shutdown_session(exception=None):
    ''' Enable Flask to automatically remove database sessions at the
    end of the request or when the application shuts down.
    Ref: http://flask.pocoo.org/docs/patterns/sqlalchemy/
    '''
    Session.remove()

@app.route('/users', methods=['GET'])
def get_all():
    users = userrepository.list_all()
    names = [ user.name for users in user]
    return ','.join(names)


@app.route('/users', methods=['POST'])
def save():
    user = User()
    user.username = 'teste'
    user.email = 'teste@email.com'
    
    user = userrepository.save(user)
    names = [ user.name for users in user]
    return f'{user.id}, {user.username}, {user.email}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)