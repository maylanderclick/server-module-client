import socket

def initServerModule(self, module):
  IP = module['IP']
  PORT = module['PORT']
  NAME = module['NAME']
  
  setattr(self, NAME, socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0))
  getattr(self, NAME).bind((IP, PORT))
  getattr(self, NAME).listen(10)

  self.logger(f'ServerModule "{NAME}" INIT in https://{IP}:{PORT}!')