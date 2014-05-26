int in;

void setup()
{
  pinMode(13,OUTPUT);
  Serial.begin(9600);
  
}

void loop()
{
  if(Serial.available())
  {
    in = Serial.read();
    if(in == '1')
    digitalWrite(13,HIGH);
    else if(in == '0')
    digitalWrite(13,LOW);
  }
}
