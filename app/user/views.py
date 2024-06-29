import os

from flask import *
from werkzeug.utils import secure_filename



from flask_login import *
from app.extensions import db
from app.user.form import LoginForm, RegistrationForm
from app.user.models import User
from app.utils import TEMPLATE_FOLDER, STATIC_FOLDER

user_bp = Blueprint('user', __name__, static_folder=STATIC_FOLDER,
                    template_folder=TEMPLATE_FOLDER, url_prefix='/user')


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

@user_bp.route("user/")
@user_bp.route("user/home")
def home():
    return render_template("user/home.html")


@user_bp.route("user/porsche")
def porsche():
    return render_template("user/porch.html")


@user_bp.route("/bmw")
def bmw():
    return render_template("user/bmw.html")


@user_bp.route("/mercedes")
def mercedes():
    return render_template("user/mercedes.html")

@user_bp.route("user/bugatti")
def bugatti():
    return render_template("user/bugati.html")


@user_bp.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = User.check_credentials(email, password)
            if not user:
                flash('Invalid Credentials, Try Again!')
                return redirect(url_for('user.login'))
            session['user_id'] = user.id
            session['full_name'] = user.full_name
            return redirect(url_for('blog.home'))
        print(form.errors)
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@user_bp.route("/register", methods=["POST", "GET"])

def register():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data
            age = form.age.data
            address = form.address.data
            user = User.query.filter_by(first_name=first_name).all()
            if user:
                # flash('User With This Email Already Exists!')
                form.first_name.errors = ['User With This First Name Already Exists!']
                return render_template('register.html', form=form)

            user = User(first_name=first_name, last_name=last_name,
                        email=email, password=password,
                        age=age, address=address)
            db.session.add(user)
            db.session.commit()
            flash('User Successfully Created!!')
            return redirect(url_for('blog.home'))
        print(form.errors)
        return render_template('register.html', form=form)
    return render_template('register.html', form=form)




