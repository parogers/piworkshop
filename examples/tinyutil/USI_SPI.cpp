/* SPI.cpp */
#include <Arduino.h>
#include "USI_SPI.h"

void SPI_Init (void)
{
  /* Set the enable/chip-select pin to input */
  ENABLE_DDR &= ~BV(ENABLE_BIT);
  //DDRA = 0b00110010;
  /* Set output pins for SPI */
  SPI_DDR |= BV(MISO_BIT);
  /* Set input pins for SPI */
  SPI_DDR &= ~(BV(MOSI_BIT) | BV(SCL_BIT));
  /* Enable USI in three-wire mode (we'll use it to fake SPI), using an external
   * clock source triggered on a positive edge. */
  USICR = BV(USIWM0) | BV(USICS1) | BV(USICS0);
  /* Have the enable line trigger an interrupt call */
  ENABLE_MSK |= BV(ENABLE_PCINT);
  /* Enable interrupt on USI overflow flag (eg host sent a complete byte of data) */
  USISR |= BV(USIOIF);
  USICR |= BV(USIOIE);
  /* Enable global interrupts and pin change interrupts */
  GIMSK |= BV(PCIE0);
  sei();
}

char SPI_Exchange(char out)
{
  /* The data we put into the USI data register will be sent to the master */
  USIDR = out;
  /* Clear the overflow condition interrupt flag */
  USISR = BV(USIOIF);
  /* Wait for the overflow flag to flip, which indicates we have received an entire
   * byte of data. (8 bits, or 16 increments of the 4-bit counter, which is incremented
   * on the rising and falling edge of the external clock source)  */
//  while (!(USISR & BV(USIOIF))) ;
  /* Once the counter overflows the contents of USIBR (the temp buffer, it's contents are 
  * received from master node) is dumped into USIDR */
//  return USIBR;
}

