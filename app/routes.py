from flask import render_template, flash, redirect, request, jsonify
from forms import ClassifyForm
from flask.views import MethodView
from app import app

class TweetAPI(MethodView):
    # Viewing a tweet.
    def get(self, tweet_id):
        if tweet_id is None:
            tweets = app.parrott.memory.recall_audited(0)
            return jsonify(data=tweets.result.docs)
        else:
            tweet = app.parrott.memory.recall(tweet_id)
            return jsonify(tweet=tweet)

    # We're not creating tweets so pass on this.
    def post(self):
        return ""

    # Deleting a tweet.
    def delete(self, tweet_id):
        tweet = app.parrott.memory.recall(tweet_id)
        app.parrott.memory.forget(tweet)
        return ""

    # Auditing a tweet.
    def put(self, tweet_id):
        tweet = app.parrott.memory.recall(tweet_id)
        positive = request.json['positive'] # bool
        app.parrott.audit(tweet, positive)
        return jsonify(data=request.json)

tweet_view = TweetAPI.as_view('tweet')
app.add_url_rule('/api/tweet/',
                defaults={'tweet_id': None},
                view_func=tweet_view,
                methods=['GET'])
app.add_url_rule('/api/tweet/',
                view_func=tweet_view,
                methods=['POST'])
app.add_url_rule('/api/tweet/<tweet_id>',
                view_func=tweet_view,
                methods=['GET', 'PUT', 'DELETE'])



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

@app.route('/audit/')
@app.route('/audit/<int:page>')
def audit(page=0):
    '''
    Get latest unaudited Tweets
    for auditing.
    '''
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

