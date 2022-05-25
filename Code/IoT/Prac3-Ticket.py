## MCU Board

from gpio import*
from time import*
from ioeclient import IoEClient

def main():
  pinMode(0, OUT)
  pinMode(1, IN)
  
  while True:
    customWrite(0, "Waiting")
    rfid = analogRead(A1)
    
    if(rfid == 0):
      customWrite(0, "Success")
    delay(3000)
if __name__ == "__main__":
  main()
  
  
## RFID Reader

if cardID == '1001':
  setState(0)
else:
  setState(1)
