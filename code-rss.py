from flask import Flask, redirect, url_for, render_template, Blueprint,request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField, TextAreaField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email
from flask_pymongo import PyMongo 
from datetime import datetime
import email_validator



app = Flask(__name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files)
)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'randomkey'

#the database name is ContactUsFormTest and the user is user1 with the password also being user1
mongo = PyMongo(app, uri = "mongodb+srv://user1:user1@hopefullyaclusterthatwo.m2buw.mongodb.net/ContactFormTest?retryWrites=true&w=majority")

class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message')
    department = SelectField('Department', choices=[("department","Department"),("sales","Sales"),("tech support","Tech Support"),("/dev/null","/Dev/Null")], validators=[DataRequired()])
    submit = SubmitField('Submit')
    checkbox = BooleanField('I Am a Human')

def log_information(name, email, message, department, subtime):
    return {"name":name, "email":email, "message":message, "submit_time":subtime}


@app.route("/", methods=['GET', 'POST'])
def index():
    form = ContactForm()
    return render_template("index.html", form=form)

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    user_collection = mongo.db.users
    form = ContactForm()
    if request.method == 'POST':
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        user_collection.insert_one(log_information(form.name.data, form.email.data, form.message.data, form.department.data, current_time))
        form.name.data = None
        form.email.data = None
        form.message.data = None
        form.department.data = None

        return "<h1>response submitted</h1>"

if __name__ == "__main__":
    app.run(debug=True)
