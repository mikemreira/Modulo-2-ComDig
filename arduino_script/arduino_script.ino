char input;
 
void setup() {
    Serial.begin(9600); 
    delay(2000);  
}
 
void loop() {
    if(Serial.available()){
        input = Serial.read();
        Serial.println(input);
    }
}
