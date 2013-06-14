from flask import render_template, flash, redirect, request
from forms import ClassifyForm
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/audited/')
@app.route('/audited/<int:page>')
def audited(page=0):
    '''
    View latest audited Tweets.
    '''
    tweets = app.parrott.memory.recall_audited(page)
    return render_template('audited.html',
        tweets=tweets, page=page)

@app.route('/audit/', methods=['GET', 'POST'])
@app.route('/audit/<int:page>', methods=['GET', 'POST'])
def audit(page=0):
    '''
    GET latest unaudited Tweets
    for auditing.

    POST a tweet as positive or
    negative.
    '''

    # POST: audits a tweet as positive or negative.
    if request.method == 'POST':
        tweet_id = request.form['id']
        positive = request.form['positive'] # bool
        tweet = app.parrott.memory.recall(tweet_id)
        if tweet:
            app.parrott.audit(tweet, positive)
            return jsonify(success=True)
        else:
            return jsonify(success=False,message='No matching tweet was found.')

    # GET: lists unaudited tweets.
    else:
        tweets = app.parrott.memory.recall_unaudited(page)
        return render_template('audit.html',
            tweets=tweets, page=page)

@app.route('/classify', methods=['GET','POST'])
def classify():
    form = ClassifyForm()

    # Redirect on (valid) submit
    if form.validate_on_submit():
        flash('The text you submitted was %s' % (form.tweet.data))
        return redirect('/')
    return render_template('classify.html', form=form)

