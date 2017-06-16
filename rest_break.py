#!/usr/bin/env python
import time
import os
import logging

# All times are in seconds

def log_total_time():
    print(total_time)


def trigger_break(break_type, break_duration):
    while break_duration >= 10:
        os.system('notify-send -t %d -u normal \"%s break: %d left\"'
                %(10000, break_type, break_duration))
        time.sleep(10)
        break_duration -= 10
    if 0 < break_duration < 10:
        os.system('notify-send -t %d -u normal \"%s break: %d left\"'
                %(break_duration, break_type, break_duration))
        time.sleep(break_duration)
        # break_duration = 0
    os.system('notify-send -t %d -u normal \"%s break is over\"'
                %(2000, break_type))


if __name__ == '__main__':
    
    TIME_BETWEEN_QUICK_BREAKS = 300
    DURATION_OF_QUICK_BREAK = 30
    TIME_BETWEEN_REST_BREAKS = 1800
    DURATION_OF_REST_BREAK = 600

    # Keeps track of how many seconds have passed since the last rest break 
    # (or how long since the script started running if there was no rest break). 
    # Does not account for the time for breaks.
    time_since_rest_break = 0

    # Keeps track of how many seconds have passed since the script started running
    # Does not account for the time for breaks. 
    total_time = 0

    while True:
        time_til_rest_break = TIME_BETWEEN_REST_BREAKS - time_since_rest_break
        
        if time_til_rest_break <= TIME_BETWEEN_QUICK_BREAKS:
            # Sleep until rest break
            time.sleep(time_til_rest_break)
            total_time += time_til_rest_break
            time_since_rest_break = 0
            print("REST BREAK")
            log_total_time()
            trigger_break('Rest', DURATION_OF_REST_BREAK)
            print("REST BREAK IS OVER")
            log_total_time()
        else:
            # Sleep until quick break
            time.sleep(TIME_BETWEEN_QUICK_BREAKS)
            total_time += TIME_BETWEEN_QUICK_BREAKS
            time_since_rest_break += TIME_BETWEEN_QUICK_BREAKS
            print("QUICK BREAK")
            log_total_time()
            trigger_break('Quick', DURATION_OF_QUICK_BREAK)
            print("QUICK BREAK IS OVER")
            log_total_time()
