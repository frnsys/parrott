from flask import render_template, flash, redirect
from forms import ClassifyForm
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/audited')
def audited():
    '''
    View latest audited Tweets.
    '''
    parrott.memory.recall_audited()

@app.route('/audit')
def audit():
    '''
    Get latest unaudited Tweets
    for auditing.
    '''
    tweets = parrott.memory.recall_unaudited()
    return render_template('audit.html',
            tweets=tweets)

@app.route('/classify', methods=['GET','POST'])
def classify():
    form = ClassifyForm()

    # Redirect on (valid) submit
    if form.validate_on_submit():
        flash('Classify foo')
        return redirect('/')
    return render_template('classify.html', form=form)

