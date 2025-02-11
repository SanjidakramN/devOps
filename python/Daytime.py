# import datetime 
# print(dir(datetime))

from datetime import datetime
import pytz
now = datetime.now(pytz.timezone('Asia/Kolkata'))
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
#print("Current date and time: ", now, "\nCurrent day: ", day, "\nCurrent month: ", month, "\nCurrent year: ", year, "\nCurrent hour: ", hour, "\nCurrent minute: ", minute, "\nCurrent second: ", second)

print("Current date and time: ", now)

