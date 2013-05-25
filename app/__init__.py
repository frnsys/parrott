from flask import Flask
app = Flask(__name__)
from app import routes, models
from apscheduler.scheduler import Scheduler
import parrott

neg = [example.strip() for example in open("data/neg.txt").readlines()]
pos = [example.strip() for example in open("data/pos.txt").readlines()]

print "Training on %i positive examples" % len(pos)
print "Training on %i negative examples" % len(neg)

#parrott = parrott.Parrott( neg, pos )

# Schedule the Collector
scheduler = Scheduler()
scheduler.add_interval_job(parrott.collect, minutes=30)
scheduler.start()

