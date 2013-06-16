Parrott
=======
By [Francis Tseng](http://supermedes.com)

[Parrott](http://supermedes.com/labs/parrott/) is intended to be a pseudo-intelligent retweeter. It will learn
from your retweeting habits, and optionally the retweeting habits of
others, and try to retweet things on your behalf.

If I can get it to work well enough, and if the Twitter API allows it
(so far it looks like it doesn't), you could in theory collect
tweets/retweets from several tastemaking accounts, and train Parrott to
be a tastemaker.

Parrott runs off a simple bag-of-words Naive Bayes classifier, which is
a slightly modified, [python-ported
version](https://github.com/ftzeng/naivebayes) of [Edwin Chen's Naive Bayes
classifier](http://goo.gl/uLmBf). Though Parrott uses unigrams, the
classifier supports any ngram, so you could modify the program to use
bigrams and so on.

Parrott is built with [Flask](http://flask.pocoo.org/), [Solr](https://lucene.apache.org/solr/), and [Backbone](http://backbonejs.org/).

Parrott is licensed under the [MIT
license](https://github.com/ftzeng/parrott/blob/master/LICENSE.txt).

## Setup
First, you will need to setup a Python
[virtualenv](http://www.virtualenv.org/en/latest/):
``` bash
    $ virtualenv parrott-env --no-site-packages
    $ source parrott-env/bin/activate
    $ pip install -r requirements.txt
```

Then you need to start the Jetty/Solr server:
``` bash
    $ cd solr
    $ java -jar start.jar -Dsolr.solr.home=memory
```
Then access at `http://localhost:8983/solr/#/`.

Note that you can move this `solr` directory to another machine and run
it there. But you will have to update the `SOLR_URL` constant in
`app/parrott/memory/memory.py` to point to the new Solr URL.

You may want to empty out the Solr instance so you can start fresh:
``` bash
    $ curl http://localhost:8983/solr/update --data '<delete><query>*:*</query></delete>' -H 'Content-type:text/xml; charset=utf-8'; curl http://localhost:8983/solr/update --data '<commit/>' -H 'Content-type:text/xml; charset=utf-8'"
```

Finally, you can start the actual application:
``` bash
    $ cd ..
    $ ./application.py
```

You should be prompted, in the command line, to authenticate your
Twitter account. Follow those instructions.

Then see Parrott at `http://localhost:5000/`.

Note that new Tweets will be collected from the authenciated user's
timeline every 30 minutes. You can edit this in `application.py`.


## Development Setup
If you want to build off of Parrott, there's a bit of extra setup required to
work on the frontend. The frontend is built off
[Bane](https://github.com/ftzeng/bane), look there for a bit more info.

You will need [Node](http://nodejs.org/), 
[NPM](https://npmjs.org/), and
[grunt-cli](https://github.com/gruntjs/grunt-cli). You will also need [Jam](http://jamjs.org/).

Once you have that, all you have to do is:
``` bash
    $ cd app/static/
    $ npm install -d
    $ jam install
    $ grunt
```
The final command, `grunt`, will setup the [Grunt](http://gruntjs.com/) task runner to monitor for file changes and automate compiling, etc.

Note that this is all in addition to the other setup instructions above.

## Why Parrott?
I'm lazy and want a computer to do my social media for me.


## To Do
* Make the damn thing more accurate

## Nice-To-Haves (Advanced Features)
* Follow links, pass through
	[Readability](https://github.com/buriy/python-readability), consider
	that content as part of the document (i.e. tweet)?