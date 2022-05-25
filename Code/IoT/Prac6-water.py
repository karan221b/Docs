from gpio import*
from time import*

while True:

  water_level = analogRead(A0)
  if water_level < 400:
    digitalWrite(A1, HIGH)
  else:
    digitalWrite(A1, LOW)
  sleep(0.3)
