from flask import Flask, redirect, url_for, render_template, Blueprint
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField,TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from flask_pymongo import PyMongo 
from datetime import datetime



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
    email = StringField('Email', validators=[DataRequired()])
    message = TextAreaField('Message')
    department = SelectField('Department', choices=[("department","Department"),("sales","Sales"),("tech support","Tech Support"),("/dev/null","/Dev/Null")], validators=[DataRequired()])
    submit = SubmitField('Submit')
    checkbox = BooleanField('I Am a Human')

def log_information(name, email, message, department, subtime):
    return {"name":name, "email":email, "message":message, "submit_time":subtime}


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def index():
    form = ContactForm()
    user_collection = mongo.db.users
    if request.method == 'POST':
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        user_collection.insert(log_information(form.name.data, form.email.data, form.message.data, form.department.data, current_time))

    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
