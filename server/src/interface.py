from PySide2.QtWidgets import QTableWidget, QTableWidgetItem
from PySide2 import QtCore, QtGui

class Interface:
  def __init__(self, parent):
    self.parent = parent

  def update(self, CSV):
    blocks = CSV.replace('\r', '').split('\n\n')

    for blockIndex in range(len(blocks)):
      if blockIndex == 0: 
        tableWidget = self.parent.ui.tableWidget
      elif blockIndex == 1: 
        tableWidget = self.parent.ui.tableWidget_2
      elif blockIndex == 2: 
        tableWidget = self.parent.ui.tableWidget_3

      lines = blocks[blockIndex].split('\n')

      table = list(map(lambda x: x.split(';'), lines))
      rowCount = len(table) - 1
      columnCount = len(table[0]) - 1

      for i in range(2, columnCount):
        tableWidget.setColumnWidth(i, 200)

      tableWidget.setRowCount(rowCount)
      tableWidget.setColumnCount(columnCount)

      for i in range(rowCount):
        for j in range(columnCount):
          tableWidget.setItem(i, j, QTableWidgetItem(table[i][j]))

          if (i > 2 and j == 7 and table[i][j] == '0'):
            tableWidget.item(i, j).setBackground(QtGui.QColor(155,0,0))
          if (i > 2 and j == 7 and table[i][j] == '1'):
            tableWidget.item(i, j).setBackground(QtGui.QColor(0,155,0))