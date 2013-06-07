from flask import render_template, flash, redirect, request
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
    app.parrott.memory.recall_audited()

@app.route('/audit')
def audit():
    '''
    Get latest unaudited Tweets
    for auditing.
    '''
    page = int(request.args.get('page', '0'))
    tweets = app.parrott.memory.recall_unaudited(page)
    return render_template('audit.html',
            tweets=tweets)

@app.route('/classify', methods=['GET','POST'])
def classify():
    form = ClassifyForm()

    # Redirect on (valid) submit
    if form.validate_on_submit():
        flash('The text you submitted was %s' % (form.tweet.data))
        return redirect('/')
    return render_template('classify.html', form=form)

