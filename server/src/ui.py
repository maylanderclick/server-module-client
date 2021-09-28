# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerifSWfc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 774, 574))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setElideMode(Qt.ElideRight)
        self.block_1 = QWidget()
        self.block_1.setObjectName(u"block_1")
        self.gridLayout_3 = QGridLayout(self.block_1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget = QTableWidget(self.block_1)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.block_1, "")
        self.block_2 = QWidget()
        self.block_2.setObjectName(u"block_2")
        self.gridLayout_4 = QGridLayout(self.block_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget_2 = QTableWidget(self.block_2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_4.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.block_2, "")
        self.block_3 = QWidget()
        self.block_3.setObjectName(u"block_3")
        self.gridLayout_5 = QGridLayout(self.block_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableWidget_3 = QTableWidget(self.block_3)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.gridLayout_5.addWidget(self.tableWidget_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.block_3, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle('Мониторинг состояния ВАСК')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.block_1), 'Абонент 1')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.block_2), 'Абонент 2')
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.block_3), 'Абонент 3')
    # retranslateUi

