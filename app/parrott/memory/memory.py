'''
Memory
======================
By Francis Tseng (@frnsys)

Interface for Solr.
'''

import httplib2
import sunburnt

SOLR_URL = "http://localhost:8983/solr/"

class Memory:
    def __init__(self):
        h = httplib2.Http(cache="/var/tmp/solr_cache")
        self.memory = sunburnt.SolrInterface(url=SOLR_URL, http_connection=h)

    def recall_unaudited(self, page):
        '''
        Retrieves unaudited Tweets.
        Amount returned depends on Solr's configuration.
        '''
        per_page = 10
        return self.memory.query(audited=False).paginate(start=page*per_page, rows=per_page).execute()

    def recall_audited(self, page):
        '''
        Retrieves audited Tweets.
        Amount returned depends on Solr's configuration.
        '''
        per_page = 10
        return self.memory.query(audited=True).paginate(start=page*per_page, rows=per_page).execute()

    def recall_positive(self, page):
        '''
        Retrieves positive (audited) Tweets.
        Amount returned depends on Solr's configuration.
        '''
        per_page = 10
        return self.memory.query(audited=True, positive=True).paginate(start=page*per_page, rows=per_page).execute()

    def recall_negative(self, page):
        '''
        Retrieves negative (audited) Tweets.
        Amount returned depends on Solr's configuration.
        '''
        per_page = 10
        return self.memory.query(audited=True, positive=False).paginate(start=page*per_page, rows=per_page).execute()


    def forget(self, tweet):
        '''
        Deletes a Tweet from Solr.
        '''
        self.memory.delete(tweet)

    def recall(self, tweet_id):
        '''
        Retrieves a Tweet by id from Solr.
        '''
        response = self.memory.query(id=tweet_id).execute()
        return response.result.docs[0]

    def memorize(self, tweet):
        '''
        Adds a Tweet to Solr.

        Args:
            tweet (string): the Tweet content
        '''
        self.memory.add(tweet)
        self.memory.commit()

