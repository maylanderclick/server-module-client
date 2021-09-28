import json

class Logger:
  def __init__(self, parent):
    self.parent = parent

  def logger(self, message):
      print('>> {}'.format(message))