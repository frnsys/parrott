#!./parrott-env/bin/python

from app import app, collector
from apscheduler.scheduler import Scheduler

if __name__ == '__main__':
    # Run the collector on start
    collector.collect()

    # Schedule the Collector
    scheduler = Scheduler()
    scheduler.add_interval_job(collector.collect, minutes=30)
    scheduler.start()

    # Awaken the Parrott
    app.run(debug=True)
