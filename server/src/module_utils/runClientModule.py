import socket

def runClientModule(self, module):
  IP = module['IP']
  PORT = module['PORT']
  NAME = module['NAME']

  self.logger(f'ClientModule "{NAME}" RUN in https://{IP}:{PORT}!')
  connection = getattr(self, NAME)
  connection.sendall(b'Connect!')

  while True: 
    csv = connection.recv(13000).decode("utf-8")
    connection.sendall(b'202')
    self.updateInterface(csv)
    self.MESSAGE = self.parser(csv)

  self.connection.close()