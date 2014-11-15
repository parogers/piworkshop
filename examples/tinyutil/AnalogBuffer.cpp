#include "AnalogBuffer.h"

AnalogBufferClass AnalogBuffer;

void AnalogBufferClass::begin()
{
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
}

void AnalogBufferClass::update()
{
  buffer[0] = analogRead(A0);
  buffer[1] = analogRead(A1);
  buffer[2] = analogRead(A2);
  buffer[3] = analogRead(A3);
}


