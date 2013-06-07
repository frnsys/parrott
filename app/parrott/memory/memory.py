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
        return self.memory.query(audited=False).paginate(start=page,rows=10).execute()

    def recall_audited(self):
        '''
        Retrieves audited Tweets.
        Amount returned depends on Solr's configuration.
        '''
        return self.memory.query(audited=True).execute()

    def recall_positive(self):
        '''
        Retrieves positive (audited) Tweets.
        Amount returned depends on Solr's configuration.
        '''
        return self.memory.query(audited=True, positive=True).execute()

    def recall_negative(self):
        '''
        Retrieves negative (audited) Tweets.
        Amount returned depends on Solr's configuration.
        '''
        return self.memory.query(audited=True, positive=False).execute()


    def forget(self, tweet):
        '''
        Deletes a Tweet from Solr.
        '''
        self.memory.delete(tweet)

    def memorize(self, tweet):
        '''
        Adds a Tweet to Solr.

        Args:
            tweet (string): the Tweet content
        '''
        self.memory.add(tweet)
        self.memory.commit()

