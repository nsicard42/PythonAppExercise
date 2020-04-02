# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:46:32 2020

@author: nathaniel sicard
"""
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(10, 35, 700, 1000)
        self.setWindowTitle('GG loser!')
        
        self.label3= QLabel("", self)
        self.label3.setPixmap(QPixmap("babei.svg")) 
        self.label3.setFixedSize (850 ,750)
        self.label3.show ()
        self.label3.move (1 ,1)
        
        self.label1 = QLabel('What hath god brought upon thine?',self)
        self.label1.setFixedWidth(200)
        self.label1.move(10,10)
        
        self.label2 = QLabel("", self)
        self.label2.move(210,10)
        message ="<h3><b><font color='blue'>What exactly is HTML?!?</font></b>"
        self.label2.setText(message)
        self.label2.setFixedWidth(200)
        
        
        self.button1 = QPushButton('Free Him.', self)
        self.button1.setToolTip('Otherwise he only becomes angrier..')
        self.button1.move(50,50)
        self.button1.clicked.connect(self.on_click_button1)
        
    @pyqtSlot () # Push Button 1 signal
    def on_click_button1 (self):
        message="<h3><b><font color=’red’>HE IS FREED!</font ></b>"
        self.label2.setText(message)
        self.label2.setFixedWidth(120)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    sys.exit(app.exec_())