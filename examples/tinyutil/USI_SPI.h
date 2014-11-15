#ifndef __SPI_H__
#define __SPI_H__

#include <Arduino.h>

#define BV(x)        (1<<(x))

/* The enable/chip-select pin will tell us when we're receiving data via SPI */
#define ENABLE_BIT   PA7
#define ENABLE_DDR   DDRA
#define ENABLE_PIN   PINA
#define ENABLE_PCINT PCINT7
#define ENABLE_MSK   PCMSK0

#define MOSI_BIT     PA6
#define MISO_BIT     PA5
#define SCL_BIT      PA4
#define SPI_DDR      DDRA

void SPI_Init (void);
char SPI_Exchange(char out);

#endif


