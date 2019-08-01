# crontab 基本格式：
# ┌───────────── minute (0 - 59)
#  │ ┌───────────── hour (0 - 23)
#  │ │ ┌───────────── day of month (1 - 31)
#  │ │ │ ┌───────────── month (1 - 12)
#  │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
#  │ │ │ │ │                                       7 is also Sunday)
#  │ │ │ │ │
#  │ │ │ │ │
#  * * * * *  command to execute

# get_prev方法，獲取上一次執行時間

from croniter import croniter
from datetime import datetime
base = datetime(2010, 1, 25, 4, 46)

iter = croniter('*/5 * * * *', base)  # every 5 minutes
print(iter.get_next(datetime))   # 2010-01-25 04:50:00
print(iter.get_next(datetime))   # 2010-01-25 04:55:00
print(iter.get_next(datetime))   # 2010-01-25 05:00:00

iter = croniter('2 4 * * mon,fri', base)  # 04:02 on every Monday and Friday
print(iter.get_next(datetime))   # 2010-01-26 04:02:00
print(iter.get_next(datetime))   # 2010-01-30 04:02:00
print(iter.get_next(datetime))   # 2010-02-02 04:02:00

iter = croniter('2 4 1 * wed', base)  # 04:02 on every Wednesday OR on 1st day of month
print(iter.get_next(datetime))   # 2010-01-27 04:02:00
print(iter.get_next(datetime))   # 2010-02-01 04:02:00
print(iter.get_next(datetime))   # 2010-02-03 04:02:00

iter = croniter('2 4 1 * wed', base, day_or=False)  # 04:02 on every 1st day of the month if it is a Wednesday
print(iter.get_next(datetime))   # 2010-09-01 04:02:00
print(iter.get_next(datetime))   # 2010-12-01 04:02:00
print(iter.get_next(datetime))   # 2011-06-01 04:02:00