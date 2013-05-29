#!parrott-env/bin/python

from app import app, collector
from apscheduler.scheduler import Scheduler

# Schedule the Collector
#scheduler = Scheduler()
#scheduler.add_interval_job(collect(), minutes=30)
#scheduler.start()

collector.collect()
