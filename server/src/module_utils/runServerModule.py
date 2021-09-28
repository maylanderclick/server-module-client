import socket
import json

def runServerModule(self, module):
  IP = module['IP']
  PORT = module['PORT']
  NAME = module['NAME']

  self.logger(f'ServerModule "{NAME}" RUN in https://{IP}:{PORT}!')
  connection = getattr(self, NAME)

  while True: 
    conn, addr = connection.accept()
    self.logger(f'Connected {addr}!')

    while True:
      try:
        if self.MESSAGE != '':
          data = json.dumps(self.MESSAGE, skipkeys=False, ensure_ascii=False)
          conn.sendall(bytes(data, 'utf-8'))

          self.MESSAGE = ''
      except:
        conn.close()
        break