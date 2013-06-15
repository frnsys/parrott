from flask import render_template, flash, redirect, request, jsonify, url_for
from forms import ClassifyForm
from flask.views import MethodView
from app import app

# Create RESTful routing for Tweet
# using Flask's MethodView.
class TweetAPI(MethodView):
    # Viewing a tweet.
    def get(self, tweet_id):
        print request.__dict__
        # If no id is specified...
        if tweet_id is None:
            tweets = app.parrott.memory.recall_unaudited(0)
            return jsonify(data=tweets)
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

# Build the actual REST routes.
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



# Serve the index.html page,
# which will start require.js.
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# Rendering the index for
# Backbone to take over.
# This is probably not the best way to do this.
@app.route('/audited')
@app.route('/audited/<int:page>')
@app.route('/audit')
@app.route('/audit/<int:page>')
def backbone(page=0):
    return render_template('index.html')

@app.route('/api/audited/')
@app.route('/api/audited/<int:page>')
def audited(page=0):
    '''
    View latest audited Tweets.
    '''
    tweets = app.parrott.memory.recall_audited(page)
    return jsonify(data=tweets, page=page)

@app.route('/api/audit/')
@app.route('/api/audit/<int:page>')
def audit(page=0):
    '''
    Get latest unaudited Tweets
    for auditing.
    '''
    tweets = app.parrott.memory.recall_unaudited(page)
    return jsonify(data=tweets, page=page)

@app.route('/classify', methods=['GET','POST'])
def classify():
    form = ClassifyForm()

    # Redirect on (valid) submit
    if form.validate_on_submit():
        app.parrott.train()
        result = app.parrott.classify(form.tweet.data)
        flash('The text you submitted was %s' % (form.tweet.data))
        flash('Your result was %f' % (result))
        return redirect(url_for('classify'))
    return render_template('classify.html', form=form)

