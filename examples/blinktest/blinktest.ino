#define BV(x)    (1 << (x))

void setup()
{
  DDRA |= BV(PA0);
}

void loop()
{
  PORTA |= BV(PA0);
  delay(2000);
  PORTA &= ~BV(PA0);
  delay(2000);
}

