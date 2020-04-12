#from Adafruit_IO import Client
from Gpio import Gpio
import sys
from Adafruit import Adafruit
import websocket
from threading import Thread
import time
import json

class Interface:
    def __init__(self):
        # self._adafruit = Adafruit()
        # self._gpio = Gpio()
        websocket.enableTrace(True)
        self.host = "ws://192.168.137.1:3333/ws"    
        self.ws = websocket.WebSocketApp(self.host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                keep_running=True)

    def run(self):
        try:
            while True:
                # self._adafruit.cuarto(self._gpio.getCuarto1(),'cuarto1')
                # self._adafruit.cuarto(self._gpio.getCuarto2(),'cuarto2')
                # self._adafruit.cuarto(self._gpio.getCuarto3(),'cuarto3')
                # self._adafruit.cuarto(self._gpio.getCuarto4(),'cuarto4')
                # self._adafruit.cuarto(self._gpio.getCuarto5(),'cuarto5')
                # self._adafruit.puertas(self._gpio.getPuerta1(),'puertas.puerta1')
                # self._adafruit.puertas(self._gpio.getPuerta2(),'puertas.puerta2')
                # self._adafruit.puertas(self._gpio.getPuerta3(),'puertas.puerta3')
                # estado = self._adafruit.alarma(self._gpio.getRele(),'alarma',self._gpio.getDetectar())
                # if estado == 'ACTIVE':
                #     self._gpio.setPir()
                # data = self._gpio.setTemperatura()
                # if data == True:
                #     self._adafruit.temperatura(self._gpio.getTemperatura(),'sensor-ht')
                self.ws.on_open = on_open
                self.ws.run_forever()
        except KeyboardInterrupt:
            sys.exit(1)
i = Gpio()
def on_message(ws, message):
    try:
        r = json.loads(message)
        print( r['d']['event'] + ' ' + r['d']['data'])
        if r['d']['event'] == "leds":
            if r['d']['data'] == "Cuarto1 ON":
                i.getCuarto1().on()
            elif r['d']['data'] == "Cuarto1 OFF":
                i.getCuarto1().off()
            if r['d']['data'] == "Cuarto2 ON":
                i.getCuarto2().on()
            elif r['d']['data'] == "Cuarto2 OFF":
                i.getCuarto2().off()
            if r['d']['data'] == "Cuarto3 ON":
                i.getCuarto3().on()
            elif r['d']['data'] == "Cuarto3 OFF":
                i.getCuarto3().off()
            if r['d']['data'] == "Cuarto4 ON":
                i.getCuarto4().on()
            elif r['d']['data'] == "Cuarto4 OFF":
                i.getCuarto4().off()
            if r['d']['data'] == "Cuarto5 ON":
                i.getCuarto5().on()
            elif r['d']['data'] == "Cuarto5 OFF":
                i.getCuarto5().off()
        if r['d']['event'] == "puertas":
            if r['d']['data'] == "Puerta1 ON":
                i.getPuerta1().max()
            elif r['d']['data'] == "Puerta1 OFF":
                i.getPuerta1().min()
            if r['d']['data'] == "Puerta2 ON":
                i.getPuerta3().max()
            elif r['d']['data'] == "Puerta2 OFF":
                i.getPuerta3().min()
        if r['d']['event'] == "alarma":
            if r['d']['data'] == "ON":
                i.getRele().on()
                i.setPir()
            elif r['d']['data'] == "OFF":
                i.getRele().off()
    except:
        print('Error')


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        ws.send('{"t":1,"d":{"topic":"chat"}}')
        i.setPir()
        data = i.setTemperatura()
        if data == True:
            ws.send('{"t":7,"d":{"topic":"chat","event":"temperatura","data":"'+ i.getTemperatura() +'"}}')
        #     self._adafruit.temperatura(self._gpio.getTemperatura(),'sensor-ht')
        # for i in range(3):
        #     ws.send('{"t":7,"d":{"topic":"chat","event":"message","data":"Hola python"}}')
        #     time.sleep(1)

        # time.sleep(1)
        # ws.close()
        print("Thread terminating...")

    Thread(target=run).start()