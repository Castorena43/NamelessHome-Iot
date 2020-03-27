#include <Servo.h>
#include <SPI.h>
#include <MFRC522.h>
Servo ser1;

byte myCards[] = {0x39,0xA6,0xCA,0x8E};

int successRead;      

byte dummy = 0x00;

byte readCard[4]; 

#define greenLed 2    
#define redLed   4      
#define yellowLed 3  

#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);


void setup() {
  ser1.attach(7);
  ser1.write(90);
  pinMode(greenLed,OUTPUT);  
  pinMode(redLed,OUTPUT);
  pinMode(yellowLed,OUTPUT);
  Serial.begin(9600);                            
  SPI.begin();                                  //Iniciamos protocolo SPI
  mfrc522.PCD_Init();                             
  mfrc522.PCD_SetAntennaGain(mfrc522.RxGain_max); 
   Serial.println("IDENTIFIQUESE...");
}

void loop() {
  
 Iniciar(); 
}
void Iniciar()
{
  do{
   
    digitalWrite(yellowLed,HIGH);
    delay(500);
    digitalWrite(yellowLed,LOW);
    delay(500);
    successRead = getID();
  } 
  while (!successRead);

  if (readCard[0] == myCards[0] && readCard[1] == myCards[1] 
  && readCard[2] == myCards[2] && readCard[3] == myCards[3])
  {   
   
    Serial.println("Bienvenido a casa");
    Success();
    ser1.write(180);
    delay(5000);
    ser1.write(90);
    
   
   
   for(int i = 0; i<4; i++) dummy = readCard[i];   // removing previous stored value from the readCard variable
   
   successRead = 0;
  }else {
  
    Error();      //calling the error function
  }
}

int getID() {
  // Getting ready for Reading PICCs
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return 0;
  }
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return 0;
  }

  Serial.println("");
  for (int i = 0; i < 4; i++) {  // 
    readCard[i] = mfrc522.uid.uidByte[i];
    Serial.print(readCard[i], HEX);
  }
  
  Serial.println("");
  mfrc522.PICC_HaltA(); 
  return 1;
}

void Success(){
  digitalWrite(greenLed,HIGH);
  delay(2000);
  digitalWrite(greenLed,LOW);
  delay(500);
}

void Error(){
  Serial.println("USUARIO NO IDENTIFICADO"); 
  
    digitalWrite(redLed,HIGH);
    delay(2000);
    digitalWrite(redLed,LOW);
    delay(500);
  
}
