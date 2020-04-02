# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:59:40 2020

@author: nathaniel sicard
"""

from PyQt5.QtWidgets import QApplication, QWidget
#very popular GUI module for python

import sys
app = QApplication(sys.argv)
#what will be 'executed'

window = QWidget()
window.setGeometry(400, 100, 300, 200) 
#sets window to 300 by 200 pixels at 400 to the right and 100 down form the top

window.setWindowTitle('What is app development?!?')
#obviously the title.

window.show()

app.exec()