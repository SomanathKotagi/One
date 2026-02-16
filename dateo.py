from datetime import datetime,timedelta

now=datetime.now()

print("Now the time is ",now)

yesterday=now-timedelta(days=1)
print(yesterday)


import time
print(time.time())
print(time.sleep(5))
print("Somanath")
