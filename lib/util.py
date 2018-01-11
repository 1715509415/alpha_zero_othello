import sys
from time import time
import psutil
import os

def print_progress_bar(count, total, start=0):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    
    if percents == 100:
        if start == 0:
            msg = '[%s] %d%%\n' % (bar, percents)
        else:
            elapsed = time() - start
            if elapsed > 3600:
                elapsed /= 3600
                msg = '[%s] %d%% total: %0.2f hours\n' % (bar, percents, elapsed)
            elif elapsed > 60:
                elapsed /= 60
                msg = '[%s] %d%% total: %0.2f minutes\n' % (bar, percents, elapsed)
            else:
                msg = '[%s] %d%% total: %0.2f seconds\n' % (bar, percents, elapsed)
    elif start == 0 or percents == 0:
        msg = '[%s] %d%%\r' % (bar, percents)
    else:
        elapsed = time() - start
        eta = elapsed / (percents/100) - elapsed
        if eta > 3600:
            eta /= 3600
            msg = '[%s] %d%% eta: %0.2f hours   \r' % (bar, percents, eta)
        elif eta > 60:
            eta /= 60
            msg = '[%s] %d%% eta: %0.2f minutes \r' % (bar, percents, eta)
        else:
            msg = '[%s] %d%% eta: %0.2f seconds \r' % (bar, percents, eta)
    sys.stdout.write(msg[:-1].ljust(89)+msg[-1])
    sys.stdout.flush()
    
def set_low_process_priority():
    p = psutil.Process(os.getpid())
    if sys.platform == "win32":
        p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    else:
        p.nice(5)

def set_high_process_priority():
    p = psutil.Process(os.getpid())
    if sys.platform == "win32":
        p.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)
    else:
        p.nice(-5)
        
def getPlayerName(player):
    return os.path.basename(player).split(".")[0]