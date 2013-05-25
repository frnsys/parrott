#!/usr/bin/env python

from apscheduler.scheduler import Scheduler
from datetime import datetime

sched = Scheduler()

#@sched.interval_schedule(minutes=1)

def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    #scheduler = Scheduler(standalone=True)
    scheduler = Scheduler()
    scheduler.add_interval_job(tick, seconds=3)
    print('Press Ctrl+C to exit')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass