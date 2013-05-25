from flask import Flask
app = Flask(__name__)
from app import routes, models
from apscheduler.scheduler import Scheduler
import parrott

#parrott = parrott.Parrott( neg, pos )

# Schedule the Collector
scheduler = Scheduler()
scheduler.add_interval_job(parrott.collect, minutes=30)
scheduler.start()

