import socket

def initClientModule(self, module):
  IP = module['IP']
  PORT = module['PORT']
  NAME = module['NAME']
  
  setattr(self, NAME, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
  getattr(self, NAME).connect((IP, PORT))

  self.logger(f'ClientModule "{NAME}" INIT in https://{IP}:{PORT}!')