#include "Fletcher.h"
#include "Fletcher16.h"

void setup_for_B() {
    Serial.begin(9600);   
}

void loop_for_B() {
  char text [] = {'1', '3', '9', '2', '7', '8', '1', '2', '4', '3', '7', '2', '9'};
  uint16_t fl = fletcher16(text, 13,0,0);
  for(int i = 0; i < 13; i++) {
    Serial.print(text[i]);
  }
  Serial.print(",");
  Serial.println(fl);
  delay(10000);
}
