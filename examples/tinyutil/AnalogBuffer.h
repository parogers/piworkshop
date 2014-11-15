#ifndef __ANALOG_BUFFER_H__
#define __ANALOG_BUFFER_H__

#include <Arduino.h>

#define ANALOG_PINS 4

class AnalogBufferClass
{
  public:
    uint16_t buffer[ANALOG_PINS];
  
    void begin();
    void update();
    
};

extern AnalogBufferClass AnalogBuffer;

#endif

