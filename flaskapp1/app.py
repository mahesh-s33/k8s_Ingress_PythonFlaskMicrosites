from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from Database.database import Database
from Model.user import User

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.DataRequired()])
    email = TextField('Email:', validators=[validators.DataRequired(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.DataRequired(), validators.Length(min=3, max=35)])

    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
        Database.initialise(database="testdb", user="mahesh", password="password@123", host="postgres")
        if request.method == 'POST':
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            print("{} Registered".format(first_name))
            user = User(None, first_name, last_name, email)
            user.save_to_db()

        if form.validate():
            flash('Thanks for registration ' + first_name)
        else:
            flash('Error: All the form fields are required. ')

        return render_template('hello.html', form=form)


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5003, debug = True)
