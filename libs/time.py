import json
import machine
import utime
import time
from ntptime import settime

def calibrate_time():
    print(time.localtime()) #  year month day hour minute second weekday dayinyear
    settime()
    rtc = machine.RTC()
    #   for time convert to second
    time_in_second_gmt = utime.time()
    # Calgary is gmt-6. 
    # 6 hours = 21600 seconds
    time_in_second_calgary = time_in_second_gmt-21600
    #   (year, month, day, weekday, hours, minutes, seconds, subseconds)
    #   Convert back to datetime format
    local_datetime_format = utime.localtime(time_in_second_calgary)
      
    return local_datetime_format


