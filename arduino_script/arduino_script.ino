#include "Fletcher.h"
#include "Fletcher16.h"

// Fletcher16 fl = Fletcher16();

void setup() {
    // fl.begin();
    Serial.begin(9600);   
}

void loop() {
  //uint16_t text[] = {1, 3, 9, 27, 81, 243, 729};
  char text[] = {'1', '2', '3'};
  uint16_t fl = fletcher16(text, 3,0,0);
  for(int i = 0; i < sizeof text; i++) {
    Serial.print(text[i]);
  }
  //Serial.print(text);
  Serial.print(",");
  Serial.println(fl);
  delay(10000);
}
