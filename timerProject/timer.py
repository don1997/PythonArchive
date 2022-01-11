#Helpful Urls:
#https://www.youtube.com/watch?v=CJeElAsOvzc
#https://stackoverflow.com/questions/7479777/difference-between-python-datetime-vs-time-modules
#https://www.theproblemsite.com/reference/science/technology/programming/seconds-minutes-and-hours

import time

def getDate(tyme):
    a = time.strftime('%Y-%m-%d',time.localtime(tyme))
    return a

def getTime(tyme):
    a = time.strftime('%H:%M %Z',time.localtime(tyme))
    return a


    

######MAIN######################

begin = time.time()

Date = getDate(begin)

#assings inital old time
startTime = getTime(begin)

print("Current Time: ", startTime)


endtimer = input("Press ENTER to stop\n")

end = time.time()

elapsed = round(end - begin)

####CALC FOR TIME CONVERSION
sec = round(elapsed % 60)
minute = (round(elapsed / 60) % 60)
hour = round((elapsed / 3600))
####CALC FOR TIME CONVERSION



endTime = getTime(end)


print("End Time: ", endTime)

print("The time elapsed is ", round(hour), " hours ", round(minute) , " minutes and ", round(sec), "seconds")



######FILE I/O#########################
file = open("times.txt", 'a')
#file = open("times.txt", "w")



file.write(str(Date) + "\t")
file.write(str(startTime) + "\t")
file.write(str(endTime) + "\t")

file.write(str(hour) + "\t")
file.write(str(minute)  + "\t")
file.write(str(sec) + "\n")

file.close()

#####FILE I/O##########################

