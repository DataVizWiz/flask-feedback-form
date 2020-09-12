from flask import render_template
from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import FeedbackForm

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', title='Home')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
      return redirect(url_for('home'))
    return render_template('feedback.html', title='Feedback', form=form)