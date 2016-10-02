#include <Servo.h>
Servo lServo;
Servo mServo;
Servo nServo;
Servo oServo;
Servo pServo;
boolean recording = false;

int recordingVar;


void setup()
{
  recordingVar = 0;
  recording =false;
  Serial.begin(9600);

  
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  lServo.attach(6);
  mServo.attach(7);
  nServo.attach(8);
  oServo.attach(9);
  pServo.attach(10);
  
  lServo.write(90);
  mServo.write(90);
  nServo.write(90);
  oServo.write(90);
  pServo.write(90);

  
  
}
void loop()
{
  
  static int lvar=90;
  static int mvar=90;
  static int ovar=90;
  static int pvar=90;
  
  int dir;
  char c;
  if(Serial.available() > 0)
  {
    c=Serial.read();
    
  if(c=='w')
  {
    if(recording)
    Serial.println("w");
    forward();
  }

  else if(c=='s')

  {
    if(recording)
    Serial.println("s");
    backward();
  }

  else if(c=='a')

  {
    if(recording)
   Serial.println("a");
   leftward();
  }

  else if(c=='d')
  {
    if(recording)
    Serial.println("d");
    rightward();
  }

  else if(c=='l')
  {
    int x = Serial.parseInt();
    if(recording)
    {
    Serial.print("l ");
    Serial.println(x);
    }
    if(lvar>x) dir = -1;
    else dir = 1;
    while(lvar!=x)
    {
      lvar = lvar+dir;
      lServo.write(lvar);
      delay(15);
    }
    
  }
  else if(c=='m')
  {
    int x = Serial.parseInt();
    if(recording)
    {
    Serial.print("m ");
    Serial.println(x);
    }
    if(mvar>x) dir = -1;
    else dir = 1;
    while(mvar!=x)
    {
      mvar = mvar+dir;
      mServo.write(mvar);
      nServo.write(180-mvar);
      delay(15);
    }
  }
  
  else if(c=='o')
  {
    int x = Serial.parseInt();
    if(recording)
    {
    Serial.print("o ");
    Serial.println(x);
    }
    if(ovar>x) dir = -1;
    else dir = 1;
    while(ovar!=x)
    {
        ovar +=dir;
        oServo.write(ovar);
        delay(15);
    }
  }
  else if(c=='p')
  {
   int x = Serial.parseInt();
   if(recording)
   {
    Serial.print("p ");
    Serial.println(x);
   }
    if(pvar>x) dir=-1;
    else dir =1;
    while(pvar!=x)
    {
      pvar+=dir;
      pServo.write(pvar);
      delay(15);
    }

  }
 

  }
}
void forward()
{
  digitalWrite(2,HIGH);
  digitalWrite(5,HIGH);
  delay(300);
  digitalWrite(2,LOW);
  digitalWrite(5,LOW);
}

void backward()
{
  digitalWrite(3,HIGH);
  digitalWrite(4,HIGH);
  delay(300);
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  
}
void rightward()
{
  digitalWrite(2,HIGH);
  delay(300);
  digitalWrite(2,LOW);
}
void leftward()
{
  digitalWrite(5,HIGH);
  delay(300);
  digitalWrite(5,LOW);
}







