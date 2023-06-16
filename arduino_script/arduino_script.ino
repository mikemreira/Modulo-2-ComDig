#include "Fletcher.h"

void setup() {
    Serial.begin(9600);   
}

void loop() {
  uint16_t text[] = {1, 3, 9, 27, 81, 243, 729};
  uint32_t fl = fletcher32(text, 7, 0, 0);
  Serial.println(fl);
  delay(10000);
}
