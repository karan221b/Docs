## 2. Timer based buzzer
from gpio import *
from time import *
pinMode(0, INPUT)
pinMode(0, OUTPUT)
while True:
    if digitalRead(0)== HIGH:
        sleep(5)
        digitalWrite (1, 1023)
    else:
        digitalWrite (1, 0)
        
       
      
## 3. Sensor based counting device

from gpio import*
from time import*

count = 0

pinMode(0, INPUT)
pinMode(0, OUTPUT)

while True:
  if digitalRead(0) == HIGH:
    count = count + 1
    print("Counting " + str(count))
    sleep(0.3)
