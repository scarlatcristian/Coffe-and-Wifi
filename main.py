from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired, URL
import csv
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, 'cafe-data.csv')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe_name = StringField(label='Cafe name', validators=[InputRequired()])
    location = StringField(
        label='Cafe Location on Google Maps (URL)', validators=[InputRequired(), URL()])
    opening_time = StringField(
        label='Opening Time e.g. 8AM', validators=[InputRequired()])
    closing_time = StringField(
        label='Closing Time e.g. 5:30PM', validators=[InputRequired()])
    coffee_rating = SelectField(
        label='Coffee Rating', choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'], validators=[InputRequired()])
    wifi_rating = SelectField(
        label='Wifi Strength Rating', choices=['✘', '💪', '💪 💪', '💪 💪💪', '💪💪💪💪', '💪💪💪💪💪'], validators=[InputRequired()])
    power_outlets = SelectField(
        label='Number of Power Outlets', choices=['✘', '🔌', '🔌 🔌', '🔌 🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], validators=[InputRequired()])
    submit = SubmitField('Submit')

# all Flask routes below


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("Form Submitted")

        with open(file_path, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow([
                form.cafe_name.data,
                form.location.data,
                form.opening_time.data,
                form.closing_time.data,
                form.coffee_rating.data,
                form.wifi_rating.data,
                form.power_outlets.data
            ])
        form = CafeForm()
        return redirect(url_for('add_cafe'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(file_path, newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
