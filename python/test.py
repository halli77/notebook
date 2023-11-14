#!/usr/bin/env python3

import time
import datetime

d = datetime.date(2022, 11, 23)
# d = datetime.datetime.today()
# -> 2022-11-23

print(datetime.date.timetuple(d))
# -> time.struct_time(tm_year=2022, tm_mon=11, tm_mday=23, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=327, tm_isdst=-1)

t = datetime.time(2, 30, 59)
print(t)
# -> 02:30:59

dt = datetime.datetime(2022, 11, 23, 2, 30, 59)
# dt = datetime.datetime.now()
# dt = datetime.datetime.utcnow()
# -> 2022-11-23 02:30:59

unix_ts = time.time()
dt = datetime.datetime.fromtimestamp(unix_ts)
# -> 2023-11-14 08:27:54.433735

d1 = datetime.datetime(2023, 10, 23, 0, 0, 0)
d2 = datetime.datetime(2023, 10, 24, 1, 0, 0)
delta1 = d2-d1
print("difference:", delta1)
# -> difference: 1 day, 1:00:00
print ("difference in days:", delta1.days)
# -> difference in days: 1
print ("difference in seconds:", delta1.seconds)
# -> difference in seconds: 3600

