from flask import render_template
from app import app

@app.route('/')
@app.route("/index")
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
