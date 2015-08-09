import os, time

hostname = input("host: ")

starting = True
while True:
    response = os.system("ping -c 1 -w15 " + hostname + " > /dev/null 2>&1")
    if response == 0:
        print(hostname + " is up :)")
        if starting == True:
            starting = False
            os.system("echo started monitoring " + hostname + ": >> " + hostname + ".uptime")
            os.system("date >> " + hostname + ".uptime")
    else:
        print(hostname + " is down :(")		
        os.system("echo " + hostname + " failed on: >> " + hostname + ".uptime")
        os.system("date >> " + hostname + ".uptime")
        exit(0)
    time.sleep(20)
