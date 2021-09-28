import socket
import time

from .logger import Logger
from .config import Config

class App:
  def __init__(self):
    self.config = Config(self).get()
    self.logger = Logger(self).logger

  def initClient(self):
    IP = self.config.get('IP')
    PORT = self.config.get('PORT')

    self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    self.connection.bind((IP, PORT))
    self.connection.listen(1)


  def runClient(self):
    IP = self.config.get('IP')
    PORT = self.config.get('PORT')

    self.logger('VASK RUN in https://{}:{}!'.format(IP, PORT))

    while True:
      conn, addr = self.connection.accept()
      self.logger(f'Connected {addr}!')

      while True:
        csv = open("VASK_test.csv", "rb").read(13000)
        # .decode("Windows-1251").encode('utf-8')        
        self.logger(f'[{addr}]:\n"{csv.decode("utf-8")}"\n')

        try:
          conn.send(csv)
          time.sleep(1)
        except:
          conn.close()
          break
