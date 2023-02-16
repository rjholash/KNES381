import time
from time import sleep

def printRocket():
    print(
            """
            
            
                    -
                  /   \\
                  | - |
                  |   |
                 /     \\
                /       \\
                    
            """ )
printRocket()
time.sleep(.8)
delay = 800
print('                 %%%%%%%%')
time.sleep(.1)
print('               %%%%%%%%%%%%')
time.sleep(.1)
print('            %%%%%%%%%%%%%%%%%%')
time.sleep(.5)
for i in range(10):
    print('                    \\')
    print('                     /')
    sleep(delay/1000)
    delay = delay *0.9