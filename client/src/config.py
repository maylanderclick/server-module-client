import json

class Config:
  def __init__(self, parent):
    self.parent = parent

  def get(self):
    f = open('config.json')
    return json.load(f)