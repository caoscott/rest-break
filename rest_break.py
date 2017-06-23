#!/usr/bin/env python
import sys
import time
import os
import logging
import datetime

# All times are in seconds

def trigger_break(break_type, break_duration, icon_path):
    while break_duration >= 30:
        os.system('notify-send -t %d -u normal -i %s \"%s break: %s left\"'
                %(30000, icon_path, break_type, 
                str(datetime.timedelta(seconds=break_duration))))
        time.sleep(30)
        break_duration -= 30
    if 0 < break_duration < 30:
        os.system('notify-send -t %d -u normal -i %s \"%s break: %s left\"'
                %(break_duration, icon_path, break_type, 
                str(datetime.timedelta(seconds=break_duration))))
        time.sleep(break_duration)
        # break_duration = 0
    os.system('notify-send -t %d -u normal \"%s break is over\"'
                %(2000, break_type))


if __name__ == '__main__':

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
   
    TIME_BETWEEN_QUICK_BREAKS = 300
    DURATION_OF_QUICK_BREAK = 30
    TIME_BETWEEN_REST_BREAKS = 1800
    DURATION_OF_REST_BREAK = 600
    PATH_TO_ICON = '~/rest-break/icon.png'

    # Keeps track of how many seconds have passed since the last rest break 
    # (or how long since the script started running if there was no rest break). 
    # Does not account for the time for breaks.
    if len(sys.argv) > 1:
        time_since_rest_break = int(sys.argv[1])
    else:
        time_since_rest_break = 0

    # Keeps track of how many seconds have passed since the script started running
    # Does not account for the time for breaks.
    if len(sys.argv) > 1:
        total_time = int(sys.argv[1])
    else:
        total_time = 0

    while True:
        time_til_rest_break = TIME_BETWEEN_REST_BREAKS - time_since_rest_break
        
        if time_til_rest_break <= TIME_BETWEEN_QUICK_BREAKS:
            # Sleep until rest break
            time.sleep(time_til_rest_break)
            total_time += time_til_rest_break
            time_since_rest_break = 0
            os.system('aplay /usr/share/sounds/speech-dispatcher/test.wav')
            trigger_break('Rest', DURATION_OF_REST_BREAK, PATH_TO_ICON)
            os.system('aplay /usr/share/sounds/purple/login.wav')
        else:
            # Sleep until quick break
            time.sleep(TIME_BETWEEN_QUICK_BREAKS)
            total_time += TIME_BETWEEN_QUICK_BREAKS
            time_since_rest_break += TIME_BETWEEN_QUICK_BREAKS
            os.system('aplay /usr/share/sounds/purple/send.wav')
            trigger_break('Quick', DURATION_OF_QUICK_BREAK, PATH_TO_ICON)
            os.system('aplay /usr/share/sounds/purple/login.wav')
