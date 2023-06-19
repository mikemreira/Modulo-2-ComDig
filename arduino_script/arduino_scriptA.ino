void setup_for_A() {
    Serial.begin(9600);
}

void loop_for_A() {
  uint16_t text[] = {1, 3, 9, 27, 81, 243, 729};
  for(int i = 0; i < 8; i++) {
    Serial.println(text[i]);
  }
  delay(10000);
}