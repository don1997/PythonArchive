import time

def getDate(tyme):
    a = time.strftime('%Y-%m-%d',time.localtime(tyme))
    print("Current date: " + a)
    return a

def getTime(tyme):
    a = time.strftime('%H:%M %Z',time.localtime(tyme))
    return a
    
t = time.time()

alpha  = getTime(t)

while True:
    print(alpha)
   