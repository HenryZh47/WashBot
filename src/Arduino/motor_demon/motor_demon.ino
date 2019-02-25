//Motor 1
int PUL = 5;  // pulse 
int DIR = 4;  // direction

//Motor 2
int PUL2 = 7;
int DIR2 = 6;


void setup() {
  // Setup code runs once
  // Sets pinouts to outputs
  pinMode(PUL, OUTPUT);
  pinMode(DIR, OUTPUT);

  pinMode(PUL2, OUTPUT);
  pinMode(DIR2, OUTPUT);
}

void loop() {
  // This demonstrates moving one motor foward 6400 ticks then backwards 6400 ticks
  // Each Pulse corresponds to one tick foward or backwatd
  
  for(int i=0; i<6400;i++)  //Forward 5000 steps
  {
    digitalWrite(DIR, LOW);   //Set direction of motor
    digitalWrite(PUL, HIGH);  //Pulse once
    delayMicroseconds(50);    //Pause so motor doesnt oscillate wildly
    digitalWrite(PUL,LOW);
    delayMicroseconds(50);
  }
  
  for (int i=0; i<6400; i++)   //Backward 5000 steps
  {
    digitalWrite(DIR,HIGH);
    digitalWrite(PUL,HIGH);
    delayMicroseconds(50);
    digitalWrite(PUL,LOW);
    delayMicroseconds(50);
  }
}
