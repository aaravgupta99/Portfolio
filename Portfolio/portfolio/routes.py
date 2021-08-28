from portfolio import app
from flask import render_template, redirect, url_for
from portfolio.forms import ContactForm
import secrets

@app.route('/')
@app.route('/home')
def home():
    return render_template('HomeSection.html', section='Home Section', Name='Aarav Gupta', Description='Backend Developer')


skills = ['Python', 'Flask', 'Django', 'C', 'C++', 'JavaScript', 'NodeJs', 'MongoDB']
@app.route('/moreaboutme')
def moreaboutme():
    return render_template('MoreAboutMe.html', section='More About Me Section', skills=skills)

@app.route('/projects')
def projects():
    return render_template('Projects.html', section='Projects')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('ContactForm.html', section='Contact Me', form=form)
