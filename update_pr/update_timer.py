import os
from datetime import datetime, timedelta
from threading import Timer
from pr_eta_update import pr_eta_update

x=datetime.today()
y = x.replace(day=x.day, hour=8, minute=0, second=0, microsecond=0) + timedelta(days=1)
#y = x.replace(day=x.day, hour=x.hour, minute=x.minute, second=0, microsecond=0) + timedelta(seconds=180)
delta_t=y-x
secs = delta_t.days*24*60*60 + delta_t.seconds

def callback_in_timers():
    os.system('date')
    pr_eta_update()

    #trigger next time
    t = Timer(secs, callback_in_timers)
    t.start()

if __name__ == "__main__":
    os.system('date')
    pr_eta_update()

    t = Timer(secs, callback_in_timers)
    t.start()
