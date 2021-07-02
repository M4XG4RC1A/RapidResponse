
int pinButton = 2;
int pinButton2 = 3;

bool b1State = false;
bool b2State = false;

void setup() {
  pinMode(pinButton,OUTPUT);
  pinMode(pinButton2,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(pinButton) && !b1State){
    Serial.println("B");
    b1State = true;
  }else if (!digitalRead(pinButton)){
    b1State = false;
  }
  if(digitalRead(pinButton2) && !b2State){
    Serial.println("R");
    b2State = true;
  }else if (!digitalRead(pinButton2)){
    b2State = false;
  }
  delay(20);
}
