'''
Memory
======================
By Francis Tseng (@frnsys)

Interface for Solr.
'''

import httplib2
import sunburnt

SOLR_URL = "http://localhost:8983/solr/master"

class Memory:
    def __init__(self):
        h = httplib2.Http(cache="/var/tmp/solr_cache")
        self.memory = sunburnt.SolrInterface(url=SOLR_URL, http_connection=h)

    def recall(self):
        self.memory.query

    def memorize(self, tweet):
        '''
        Adds a Tweet to Solr.

        Args:
            tweet (string): the Tweet content
        '''
        self.memory.add({tweet: tweet})

