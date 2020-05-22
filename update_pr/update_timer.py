import os
import sys
import time
from datetime import datetime, timedelta
from threading import Timer
from pr_eta_update import pr_eta_update


def pr_eta_update_timer():
    output_file = os.path.join(sys.path[0], 'output.log')
    os.system('/volume/buildtools/bin/python ' + os.path.join(sys.path[0],'pr_eta_update.py') + \
            ' &>' + output_file)
    time.sleep(5)
    os.system('/usr/bin/mail -t benliu@juniper.net -s pr_eta_update < ' + output_file)

    #trigger next time
    x=datetime.today()
    y = x.replace(day=x.day, hour=17, minute=0, second=0, microsecond=0) + timedelta(days=1)
    delta_t=y-x
    secs = delta_t.days*24*60*60 + delta_t.seconds
    t = Timer(secs, pr_eta_update_timer)
    t.start()

if __name__ == "__main__":

    # PR ETA update process
    pr_eta_update_timer()
