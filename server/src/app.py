import socket
import time
import threading
import json

from PySide2 import QtCore, QtGui, QtWidgets
from .ui import Ui_MainWindow

from .logger import Logger
from .config import Config
from .parser import Parser
from .interface import Interface
from .module_utils.initClientModule import initClientModule
from .module_utils.initServerModule import initServerModule
from .module_utils.runClientModule import runClientModule
from .module_utils.runServerModule import runServerModule

class App(QtWidgets.QMainWindow):
  def __init__(self):
    super(App, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.config = Config(self).get()
    self.logger = Logger(self).logger
    self.updateInterface = Interface(self).update
    self.parser = Parser(self).CSV_to_JSON

    self.initServer()
    self.runServer()
    self.show()

  def __initClientModule(self, module):
    initClientModule(self, module)

  def __initServerModule(self, module):
    initServerModule(self, module)

  def __runClientModule(self, module):
    runClientModule(self, module)
  
  def __runServerModule(self, module):
    runServerModule(self, module)

  def __initModule(self, moduleName):
    module = self.config.get(moduleName)
    TYPE = module['TYPE']

    if TYPE == 'SERVER':
      self.__initServerModule(module)
    elif TYPE == 'CLIENT':
      self.__initClientModule(module)

  def __runModule(self, moduleName):
    module = self.config.get(moduleName)
    TYPE = module['TYPE']

    if TYPE == 'SERVER':
      self.__runServerModule(module)
    elif TYPE == 'CLIENT':
      self.__runClientModule(module)
  
  def initServer(self):
    self.__initModule('VASK')
    self.__initModule('CLIENT')

  def runServer(self):
    t1 = threading.Thread(target=self.__runModule, args=('VASK',))
    t2 = threading.Thread(target=self.__runModule, args=('CLIENT',))

    t1.start()
    t2.start()
