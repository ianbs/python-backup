# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainGui(object):
    def setupUi(self, MainGui):
        if not MainGui.objectName():
            MainGui.setObjectName(u"MainGui")
        MainGui.resize(650, 200)
        self.label = QLabel(MainGui)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 171, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(MainGui)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 171, 21))
        self.label_2.setFont(font)
        self.lineEdit = QLineEdit(MainGui)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 20, 481, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit.setFont(font1)
        self.lineEdit_2 = QLineEdit(MainGui)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 50, 481, 21))
        self.lineEdit_2.setFont(font1)
        self.progressBar = QProgressBar(MainGui)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 100, 621, 23))
        self.progressBar.setValue(0)
        self.pushButton = QPushButton(MainGui)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 150, 301, 31))
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(MainGui)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 150, 301, 31))
        self.pushButton_2.setFont(font1)

        self.retranslateUi(MainGui)

        QMetaObject.connectSlotsByName(MainGui)
    # setupUi

    def retranslateUi(self, MainGui):
        MainGui.setWindowTitle(QCoreApplication.translate("MainGui", u"Simple Backup", None))
        self.label.setText(QCoreApplication.translate("MainGui", u"Caminho de Origem:", None))
        self.label_2.setText(QCoreApplication.translate("MainGui", u"Caminho de Destino:", None))
        self.pushButton.setText(QCoreApplication.translate("MainGui", u"Realizar Backup", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainGui", u"Minimizar para a bandeja", None))
    # retranslateUi

