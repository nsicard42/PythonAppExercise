# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:46:32 2020

@author: nathaniel sicard
"""
import sys
from PyQt5. QtWidgets import QApplication , QMainWindow , QLabel
from PyQt5.QtGui import QPixmap
class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(400, 100, 1500, 1000)
        self.setWindowTitle('GG loser!')
        
        label3= QLabel("", self)
        label3.setPixmap(QPixmap("babei.svg")) 
        label3.setFixedSize (850 ,750)
        label3.show ()
        label3.move (1 ,1)
        label1 = QLabel('What hath god brought upon thine?',self)
        label1.setFixedWidth(200)
        label1.move(15,15)
        label2 = QLabel("", self)
        message ="<h3><b><font color='blue'>What exactly is HTML?!?</font></b>"
        label2.setText(message)
        label2.setFixedWidth(200)
        label2.move(5,5)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    app.exec_()