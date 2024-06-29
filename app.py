from flask import *

from app import create_app
from flask_login import *
from app.extensions import db


app = create_app()

login_manager = LoginManager()
login_manager.init_app(app)



with app.app_context():
    print('Creating Database And Tables')
    db.create_all()
    print('Created Database and tablesss')


@app.before_request
def make_session_permanent():
    session.permanent = True


if __name__ == '__main__':
    app.run(debug=True, port=5100)
