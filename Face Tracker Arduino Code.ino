#include <Servo.h>
#include <string.h>

Servo servox; 
Servo servoy;
int Buffer = 30;
int angle_step = 0;
void setup() {
  Serial.begin(9600);
  servox.attach(9);
  servox.write(90);
  servoy.attach(10);
  servoy.write(90);

}

void loop() {

if (Serial.available()>=2)
{
  angle_step = 0;
  int screen_x = Serial.read();
  int screen_y = Serial.read();

  if(screen_x >100)
  {
    servox.write(servox.read() - 2);
  }
  else if (screen_x < 80)
  {
      servox.write(servox.read() + 2);
  }


  if(screen_y >100 )
  {
    servoy.write(servoy.read() + 1);
  }
  else if (screen_y < 80   )
  {
    servoy.write(servoy.read() - 1);
  }
    
}
}



