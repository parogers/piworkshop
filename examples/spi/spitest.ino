#define BV(x)    (1<<(x))

void SPI_Init (void)
{
    DDRB = 0b00110010;
    USICR = BV(USIWM0) | BV(USICS1);
}

char SPI_Exchange (char out)
{
    USIDR = out;
    USISR = (1<<USIOIF);
    while (!(USISR&(1<<USIOIF)));
    return USIDR;
}

void setup()
{
  SPI_Init();
}

static char out = 55;

void loop()
{
  /* Wait for the CS line to go high */
  if (PINB & BV(PB3)) {
    out = SPI_Exchange(out);
  }
}

