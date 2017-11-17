from tkinter import *

QUICK_BREAK = 30
REST_BREAK = 30
TIME_UNTIL_QUICK = 300
TIME_UNTIL_REST = 1800

time_until = 0

root = Tk()
top = Toplevel()
root.withdraw()
top.withdraw()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
top.geometry("{}x{}+0+0".format(w, h))

top.grab_set()

def set_event(t, x):
    top.after(t * 1000, x)

def quick_break():
    global time_until
    time_until += TIME_UNTIL_QUICK
    top.title('Quick Break')
    top.deiconify()
    set_event(QUICK_BREAK, top.withdraw)
    if TIME_UNTIL_REST - time_until <= TIME_UNTIL_QUICK:
        set_event(TIME_UNTIL_QUICK + QUICK_BREAK, rest_break)
    else:
        set_event(TIME_UNTIL_REST + QUICK_BREAK, quick_break)

def rest_break():
    global time_until
    time_until = 0
    top.title('Rest Break')
    top.deiconify()
    set_event(REST_BREAK, top.withdraw)
    set_event(TIME_UNTIL_QUICK + REST_BREAK, quick_break)

set_event(TIME_UNTIL_QUICK, quick_break)
root.mainloop()
