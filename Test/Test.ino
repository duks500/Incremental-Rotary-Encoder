
#define A 2
#define B 3
#define Key  12//key
#define hysteresis 5
#define D 19 //Diameter 19mm

float C = 0; //perimeter
unsigned int Distance;
int VA = 0;
int VB = 0;
bool firstRun = true;
unsigned long Count = 0;//count
unsigned int Count_1 = 0; //Negative count
unsigned char flag = 1;
unsigned long lasttime = 0, Modetime = 0;
long  flag_A = 0;
//Length measurement range is ± 6 M
void setup()
{
  Serial.begin(9600);
  pinMode(A, INPUT_PULLUP); //Pull-up input
  pinMode(B, INPUT_PULLUP);
  pinMode(Key, INPUT);
  attachInterrupt(digitalPinToInterrupt(A), interrupt, RISING);
  C = D * PI;
}

void loop()
{
//      Serial.print("Detection ");//
      if (Count > 0 && Count < 0xffff)//Determine whether the length is positive
      {
//        Serial.print('-');//The length is negative
        Distance = C * Count / 400;
      }

      else if (Count == 0 && Count_1 == 0 )//Determine whether the length is zero
      {
//        Serial.print(' ');
        Distance = C * Count / 400;
      }

      else//Length is positive
      {
//        Serial.print('+');
        Distance = Count_1 * C  / 400;
      }
      
      Modetime = millis();
  
      if(firstRun == false)
      {
        Serial.print(Distance / 10000);
        Serial.print((Distance / 1000) % 10);
        Serial.print((Distance / 100) % 10);
        Serial.print('.');
        Serial.print((Distance / 10) % 10);
        Serial.print(Distance % 10);
      }
      else
      {
        firstRun = false;
      }
  delay(100);
  Serial.print('\n');
}

void interrupt()
{
  VB = digitalRead(B);
   if (VB == 1)//To determine whether the positive measurement
    {
      flag = 1;
      
      if (Count > 0xffff)
      {
        Count_1 -= 1;
      }

      Count += 1;
    }
    
    else//Reverse measurement
    {
      flag = 0;
      Count -= 1;
      
      if (Count > 0xFFFF)
      {
        Count_1 += 1;
      }
    }
    
    //Count is cleared over the range
    if (Count < 0xFFFF && Count > 0x294A)
      Count = 0;

    else if (Count < 0xFFFFD6B5 && Count > 0xFFFF)
      Count = 0;

}  
