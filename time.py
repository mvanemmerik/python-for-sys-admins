# https://docs.python.org/3/library/time.html

from time import localtime, mktime, strftime

now = localtime()
print(now)
print(f'The hour is: {now.tm_hour}')
print('---')

start_time = localtime()
print(f"Timer started: {strftime('%X', start_time)}")

input("Press 'Enter' to stop timer ")

stop_time   = localtime()
difference = mktime(stop_time) - mktime(start_time)
print(f"Timer ended: {strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")



