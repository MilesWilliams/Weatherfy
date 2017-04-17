import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from main_window import MainWindow


def run():
    qss_file = open('styles.qss').read()
    app = QtWidgets.QApplication(sys.argv)
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), "Icons/weathericon.png")
    app.setWindowIcon(QtGui.QIcon(path))
    app.setStyleSheet("Window {background: rgba(0,255,0,20%)}")
    app.setStyleSheet(qss_file)
    main_window = MainWindow()
    main_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    main_window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    main_window.setWindowOpacity(0.6)
    main_window.show()

    sys.exit(app.exec_())

run()
