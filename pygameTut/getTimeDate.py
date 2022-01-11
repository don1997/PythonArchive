#for getting date
from datetime import date
#for getting time
import time


#gets date
today = date.today()
print("Today's date: ", today)
#gets time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)