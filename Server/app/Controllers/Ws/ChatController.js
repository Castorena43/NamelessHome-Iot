"use strict";

class ChatController {
  constructor({ socket, request }) {
    this.socket = socket;
    this.request = request;
  }

  onLeds(data) {
    this.socket.broadcast("leds", data);
    console.log('leds ' + data);
  }
  onPuertas(data) {
    this.socket.broadcast("puertas", data);
    console.log('puertas ' + data);
  }
  onTemperatura(data) {
    this.socket.broadcast("temperatura", data);
    console.log('temperatura ' + data);
  }
  onAlarma(data) {
    this.socket.broadcast("alarma", data);
    console.log('alarma ' + data);
  }
}

module.exports = ChatController;
