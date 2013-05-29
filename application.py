#!parrott-env/bin/python

from app import app, collector
from apscheduler.scheduler import Scheduler

if __name__ == '__main__':
    app.run(debug=True)

# Schedule the Collector
scheduler = Scheduler()
scheduler.add_interval_job(collect(), minutes=30)
scheduler.start()
