from time import sleep
from sms import send_message
from config import NUMBER, CARRIER


loop = input("Enter loop number\n> ")
loop = int(loop)
# gets loop count

if loop != 0:
    loop += 1

wait = input("Enter wait time (s)\n> ")
wait = float(wait)
# gets wait time between sends

f = open("msg.txt", "r")
txt = f.readlines()
f.close()
# gets message
    
while (loop != 1):  # send loop
    for line in txt:
        send_message(NUMBER, CARRIER, line.strip())
        print(f"SENT: {line.strip()}")
        
        sleep(wait)
            
    loop -= 1