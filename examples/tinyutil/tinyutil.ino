/* SPI with interrupts */

#include "AnalogBuffer.h"
#include "USI_SPI.h"

#define BUFFER_BYTES (2*ANALOG_PINS)
byte *byteBuffer;
int bufferPos;

ISR(PCINT0_vect)
{
  if (ENABLE_PIN & BV(ENABLE_BIT)) {
    /* The chip-select line went high - ready to send/receive data */
    bufferPos = 0;
    handle_spi_xfer();
  }
}

ISR(USI_OVF_vect)
{
  /* Save data from the host */
  //out = USIBR;
  /* Clear the overflow interrupt */
  USISR = BV(USIOIF);
  if (ENABLE_PIN & BV(ENABLE_BIT)) {
    /* The chip-select line is still high - send more bytes */
    handle_spi_xfer();
  }
}

void handle_spi_xfer()
{
  char out = 0;
  if (bufferPos < BUFFER_BYTES) out = byteBuffer[bufferPos];
  else out = 0;

  SPI_Exchange(out);
  bufferPos++;
}

void setup()
{
  AnalogBuffer.begin();
  byteBuffer = (byte*)AnalogBuffer.buffer;
  SPI_Init();
}

void loop()
{
  AnalogBuffer.update();
}

