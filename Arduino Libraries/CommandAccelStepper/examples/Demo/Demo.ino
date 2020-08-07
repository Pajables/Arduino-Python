#include <CommandHandler.h>
#include <CommandManager.h>
CommandManager cmdMng;

#include <AccelStepper.h>
#include <CommandAccelStepper.h>
AccelStepper stp(AccelStepper::DRIVER, 54, 55);
CommandAccelStepper cmdStp(stp);

void setup()
{
  Serial.begin(115200);

  cmdStp.registerToCommandManager(cmdMng, "CSTP1");

  cmdMng.init();
  pinMode(38, OUTPUT);
  digitalWrite(38, LOW);
  
}

void loop()
{
  cmdMng.update();
}
