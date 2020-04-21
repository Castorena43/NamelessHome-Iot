import websocket
from threading import Thread
import time
import sys
import json


def on_message(ws, message):
    try:
        r = json.loads(message)
        print( r['d']['event'] + ' ' + r['d']['data'])
    except:
        print('Error')


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        ws.send('{"t":1,"d":{"topic":"chat"}}')
        # for i in range(3):
        #     ws.send('{"t":7,"d":{"topic":"chat","event":"message","data":"Hola python"}}')
        #     time.sleep(1)

        # time.sleep(1)
        # ws.close()
        print("Thread terminating...")

    Thread(target=run).start()


if __name__ == "__main__":
    websocket.enableTrace(True)
    host = "ws://192.168.137.1:3333/ws"
    
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                keep_running=True)
    
    while True:
        ws.on_open = on_open
        ws.run_forever()
    