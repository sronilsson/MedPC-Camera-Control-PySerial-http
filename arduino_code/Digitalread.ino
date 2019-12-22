int Cam1_Pin = 2;
int Cam2_Pin = 3;
int Cam3_Pin = 4;
int Cam4_Pin = 5;
int Cam5_Pin = 6;
int Cam6_Pin = 7;
int Cam7_Pin = 8;
int Cam8_Pin = 9;
int Cam9_Pin = 10;
int Cam10_Pin = 11;
int Cam11_Pin = 12;
int Cam12_Pin = 13;


int Cam1_output = 0;
int Cam2_output = 0;
int Cam3_output = 0;
int Cam4_output = 0;
int Cam5_output = 0;
int Cam6_output = 0;
int Cam7_output = 0;
int Cam8_output = 0;
int Cam9_output = 0;
int Cam10_output = 0;
int Cam11_output = 0;
int Cam12_output = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Cam1_output = digitalRead(Cam1_Pin);
  Cam2_output = digitalRead(Cam2_Pin);
  Cam3_output = digitalRead(Cam3_Pin);
  Cam4_output = digitalRead(Cam4_Pin);
  Cam5_output = digitalRead(Cam5_Pin);
  Cam6_output = digitalRead(Cam6_Pin);
  Cam7_output = digitalRead(Cam7_Pin);
  Cam8_output = digitalRead(Cam8_Pin);
  Cam9_output = digitalRead(Cam9_Pin);
  Cam10_output = digitalRead(Cam10_Pin);
  Cam11_output = digitalRead(Cam11_Pin);
  Cam12_output = digitalRead(Cam12_Pin);
  
  String DataString = String(Cam1_output) + ',' + String(Cam2_output) + ',' + String(Cam3_output) + ',' + String(Cam4_output) + ',' + String(Cam5_output) + ',' + String(Cam6_output) + ',' + String(Cam7_output) + ',' + String(Cam8_output) + ',' + String(Cam9_output) + ',' + String(Cam10_output) + ',' + String(Cam11_output) + ',' + String(Cam12_output) + ',';
  Serial.println(DataString);
  delay(1); 
}
