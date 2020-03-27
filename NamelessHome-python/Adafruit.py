from Adafruit_IO import Client
import sys

class Adafruit:
    def __init__(self):
        self.aio = Client('Castorena', '35d5cc8177b24e198574c9db7aaa5ba2')
    
    def cuarto(self,led,feed):
        try:
            data = self.aio.receive(feed)
            if data.value == 'ON':
                led.on()
            elif data.value == 'OFF':
                led.off()
        except KeyboardInterrupt:
            sys.exit(1)
        except:
            print('Fallo al obtener datos')
        
    def puertas(self,led,feed):
        try:
            data = self.aio.receive(feed)
            if data.value == 'OPEN':
                led.max()
            elif data.value == 'CLOSE':
                led.min()
        except KeyboardInterrupt:
            sys.exit(1)
        except:
            print('Fallo al obtener datos')
    
    def alarma(self,relay,feed,led):
        try:
            data = self.aio.receive(feed)
            if data.value == 'ACTIVE':
                relay.on()
                return 'ACTIVE'
            elif data.value == 'INACTIVE':
                led.off()
                relay.off()
                return 'INACTIVE'
        except KeyboardInterrupt:
            sys.exit(1)
        except:
            print('Fallo al obtener datos')
    
    def temperatura(self,t,feed):
        try:
            data = self.aio.send(feed,str(t))
        except KeyboardInterrupt:
            sys.exit(1)
        except:
            print('Fallo al obtener datos')
