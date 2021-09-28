import socket
import json

from .logger import Logger
from .config import Config

class App:
  def __init__(self):
    self.config = Config(self).get()
    self.logger = Logger(self).logger

  def initClient(self):
    IP = self.config.get('IP')
    PORT = self.config.get('PORT')

    self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.connection.connect((IP, PORT))

  def runClient(self):
    IP = self.config.get('IP')
    PORT = self.config.get('PORT')
    self.logger('Client RUN in https://{}:{}!'.format(IP, PORT))
    self.connection.sendall(b'Connect!')
    while True: 
      data = self.connection.recv(13000).decode('utf-8')
      self.logger(data)
      self.connection.sendall(b'202')

    self.connection.close()