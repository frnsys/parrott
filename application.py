#!parrott-env/bin/python

from app import app, collector
from apscheduler.scheduler import Scheduler

import datetime

def foo():
    myFile = open ('/Users/ftseng/Desktop/foo.txt', 'w')
    myFile.write(str(datetime.datetime.now()))
    myFile.close()

if __name__ == '__main__':
    # Schedule the Collector
    scheduler = Scheduler()
    #scheduler.add_interval_job(collector.collect(), minutes=30)
    scheduler.add_interval_job(foo, seconds=5)
    scheduler.start()

    app.run(debug=True)
