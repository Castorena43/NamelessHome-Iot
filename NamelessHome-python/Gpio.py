from gpiozero import MotionSensor, LED, Servo, AngularServo
import gpiozero
import Adafruit_DHT
class Gpio:
    def __init__(self):
        self.cuarto1 = LED(5)
        self.cuarto2 = LED(6)
        self.cuarto3 = LED(13)
        self.cuarto4 = LED(19)
        self.cuarto5 = LED(26)
        self.detectar = LED(21)
        self.RELAY_PIN = 12
        self.RELAY_PIN1 = 18
        self.relay = gpiozero.OutputDevice(self.RELAY_PIN, active_high=False, initial_value=False)
        self.relayV = gpiozero.OutputDevice(self.RELAY_PIN1, active_high=False, initial_value=False)
        self.pir = MotionSensor(17)
        self.puerta1 = AngularServo(20, min_angle=0, max_angle=90)
        self.puerta2 = AngularServo(16, min_angle=0, max_angle=90)
        self.puerta3 = AngularServo(7, min_angle=0, max_angle=90)
        self.DHT_READ_TIMEOUT = 10
        self.DHT_DATA_PIN = 4
        self.dht22_sensor = Adafruit_DHT.DHT11
        self.temperature = 0
    
    def getCuarto1(self):
        return self.cuarto1
    
    def getCuarto2(self):
        return self.cuarto2
    
    def getCuarto3(self):
        return self.cuarto3

    def getCuarto4(self):
        return self.cuarto4
    
    def getCuarto5(self):
        return self.cuarto5
    
    def getRele(self):
        return self.relay
    
    def getPir(self):
        return self.pir
    
    def setPir(self):
        if self.pir.motion_detected:
            self.detectar.on()
            time.sleep(5)
            self.detectar.off()
            print('Movimiento')
        else:
            self.detectar.off()
            print('NO Movimiento')
    
    def getPuerta1(self):
        return self.puerta1
    
    def getPuerta2(self):
        return self.puerta2
    
    def getPuerta3(self):
        return self.puerta3

    def getDetectar(self):
        return self.detectar
    
    def getTemperatura(self):
        return self.temperature

    def setTemperatura(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.dht22_sensor, self.DHT_DATA_PIN)
        if humidity is not None and temperature is not None:
            self.temperature = '%.0f'%(temperature)
            print(self.temperature)
            if int(self.temperature) > 30:
                self.relayV.on()
            else:
                self.relayV.off()            
            return True

    #def setServo(self):
