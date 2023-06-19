#include "Fletcher.h"
#include "Fletcher16.h"

void setup_for_C() {
    Serial.begin(9600);
}

void loop_for_C() {
  char text [] = {'7', '3', '9'};
  uint16_t fl = fletcher16(text, 3,0,0);
  for(int i = 0; i < 3; i++) {
    Serial.print(text[i]);
  }
  Serial.print(",");
  Serial.println(fl);
  delay(10000);
}