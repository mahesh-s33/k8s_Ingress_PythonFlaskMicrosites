from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from Database.database import Database
from Model.user import User

app = Flask(__name__)

class Users():
    @app.route("/", methods=['GET'])
    def hello():
        Database.initialise(database="testdb", user="mahesh", password="password@123", host="postgres")
        users = User.get_all_users()
        return render_template('hello.html', data=users)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5003, debug = True)
