import sys
import asyncio
from PySide2.QtWidgets import QApplication

from src.app import App

async def start():
  app = QApplication(sys.argv)
  application = App()
  sys.exit(app.exec_())

asyncio.run(start())