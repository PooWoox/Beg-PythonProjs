from flask import Flask, render_template, flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = '551bba735a400f2e015f23f7948c53d0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Tasks(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task = db.Column(db.String(200), nullable=False)
	completed = db.Column(db.Boolean, nullable=False, default=False)
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f"Tasks('{self.task}', '{self.created_at}')"

class TaskForm(FlaskForm):
	task = StringField('Task', validators=[DataRequired()])
	submit = SubmitField('Create task')

@app.route('/', methods=('GET', 'POST'))
@app.route('/home', methods=('GET', 'POST'))
def home():
	form = TaskForm()
	if form.validate_on_submit():
		task = Tasks(task=form.task.data)
		db.session.add(task)
		db.session.commit()
		flash('Task created successfully!')
	else:
		flash('Task was not created with success.', 'danger')
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)