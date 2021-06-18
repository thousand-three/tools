'''
@application: 加速系统时间
@author: 三千
@create time: 2021-6-17
@edit time: 
@editor:

'''

import win32api
import ctypes
import sys

month : dict = {1:31,2:28,22:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
tm_year : int = 0
tm_mon : int = 0
tm_wday : int = 0
tm_mday : int = 0
tm_hour : int = 0
tm_min : int = 0
tm_sec : int = 0
tm_millisec : int = 0

def AccelerateSystemTime(multiple):
    if ctypes.windll.shell32.IsUserAnAdmin():
        global tm_year,tm_mon,tm_wday,tm_mday,tm_hour,tm_min,tm_sec,tm_millisec
        tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, tm_millisec = win32api.GetSystemTime()
        start_day = tm_mday
        while True:
            CorrectionTime(multiple)
            win32api.SetSystemTime(tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, tm_millisec)
            if (start_day - tm_mday >= 2) or (start_day - tm_mday < 0 and start_day == 1):
                break
        
def CorrectionTime(multiple):
    global tm_year,tm_mon,tm_wday,tm_mday,tm_hour,tm_min,tm_sec,tm_millisec
    current_month = tm_mon
    if tm_year%4 == 0 and tm_mon == 2:
        current_month = 22

    day = month[current_month]
    tm_millisec *= int(multiple)
    if tm_millisec >= 1000:
        tm_sec += int(tm_millisec/1000)
        tm_millisec = tm_millisec%1000
    if tm_sec >= 60:
        tm_min += int(tm_sec/60)
        tm_sec = tm_sec%60
    if tm_min >= 60:
        tm_hour += int(tm_min/60)
        tm_min = tm_min%60
    if tm_hour >= 24:
        tm_hour -= 24
        tm_mday += 1
    if tm_mday > day:
        tm_mday -= day
        current_month += 1
    if current_month > 12:
        tm_year += 1
        current_month = 1

if __name__ == "__main__":
    if len(sys.argv) == 2:
        multiple = sys.argv[1]
        AccelerateSystemTime(multiple)
    else:
        print("parameter is incorrect")