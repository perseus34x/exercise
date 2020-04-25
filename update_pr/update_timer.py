import os
import time
from datetime import datetime, timedelta
from threading import Timer
from pr_eta_update import pr_eta_update

x=datetime.today()
y = x.replace(day=x.day, hour=8, minute=0, second=0, microsecond=0) + timedelta(days=1)
#y = x.replace(day=x.day, hour=x.hour, minute=x.minute, second=0, microsecond=0) + timedelta(seconds=180)
delta_t=y-x
secs = delta_t.days*24*60*60 + delta_t.seconds

def callback_in_timers():
    os.system('python pr_eta_update.py &>output.log')
    time.sleep(5)
    os.system('/usr/bin/mail -t benliu@juniper.net < output.log')

    #trigger next time
    t = Timer(secs, callback_in_timers)
    t.start()

if __name__ == "__main__":
    os.system('python pr_eta_update.py &>output.log')
    time.sleep(5)
    os.system('/usr/bin/mail -t benliu@juniper.net -s pr_eta_update < output.log')

    t = Timer(secs, callback_in_timers)
    t.start()
