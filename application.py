#!parrott-env/bin/python

from app import app
from apscheduler.scheduler import Scheduler

if __name__ == '__main__':
    app.run(debug=True)

# Schedule the Collector
scheduler = Scheduler()
scheduler.add_interval_job(parrott.collect, minutes=30)
scheduler.start()
