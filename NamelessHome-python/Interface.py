#from Adafruit_IO import Client
from Gpio import Gpio
import sys
from Adafruit import Adafruit


class Interface:
    def __init__(self):
        self._adafruit = Adafruit()
        self._gpio = Gpio()

    def run(self):
        try:
            while True:
                self._adafruit.cuarto(self._gpio.getCuarto1(),'cuarto1')
                self._adafruit.cuarto(self._gpio.getCuarto2(),'cuarto2')
                self._adafruit.cuarto(self._gpio.getCuarto3(),'cuarto3')
                self._adafruit.cuarto(self._gpio.getCuarto4(),'cuarto4')
                self._adafruit.cuarto(self._gpio.getCuarto5(),'cuarto5')
                self._adafruit.puertas(self._gpio.getPuerta1(),'puertas.puerta1')
                self._adafruit.puertas(self._gpio.getPuerta2(),'puertas.puerta2')
                # self._adafruit.puertas(self._gpio.getPuerta3(),'puertas.puerta3')
                # estado = self._adafruit.alarma(self._gpio.getRele(),'alarma',self._gpio.getDetectar())
                # if estado == 'ACTIVE':
                #     self._gpio.setPir()
                # data = self._gpio.setTemperatura()
                # if data == True:
                #     self._adafruit.temperatura(self._gpio.getTemperatura(),'sensor-ht')
        except KeyboardInterrupt:
            sys.exit(1)