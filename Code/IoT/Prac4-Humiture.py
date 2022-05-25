function getSensorData()
{
  return Math.floor(map(analogRead(A0), 0, 1023, 0, 100) + 0.5);
}
function setup() {
  attachInterrupt(A0, function() {
    processData(getSensorData());
  });
}
function processData(data) {
  if(data > 90) {
        customWrite(0, data + " going to rain");
  }else {
        customWrite(0, data + " no rain");
  }
}
