import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import urllib3
from urllib.parse import urlencode
import json
import requests


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(1440, 0, 300, 621)
        self.setWindowTitle("Weatherfy")
        self.setCentralWidget(WeatherWidget(self))
        self.setContentsMargins(0, 0, 0, 0)
        self.show()


class WeatherWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(WeatherWidget, self).__init__(parent)
        url = requests.get("https://query.yahooapis.com/v1/public/yql?q=select * from weather.forecast where woeid= 1591691 and u='c'&format=json")
        content = url.json()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # print(content['query']['results']['channel']['item']['forecast'][0]['date'])
        currentDay = content['query']['results']['channel']['item']['condition']
        location = content['query']['results']['channel']['location']
        forecast = content['query']['results']['channel']['item']['forecast']

        label = QtWidgets.QLabel(self)
        label.setText(currentDay['temp'] + "˚c")

        main_frame = QtWidgets.QListWidget()
        main_frame.setObjectName("city")
        main_frame.resize(300, 20)
        todays_weather = QtWidgets.QListWidget()
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addWidget(todays_weather)
        layout.addWidget(label)
        layout.addWidget(main_frame)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        print(currentDay)

        mainItem = QtWidgets.QListWidgetItem(location['city'])
        todays_weather.addItem(mainItem)
        todays_weather.setStyleSheet("background: rgba(0,48,88,0.65); max-width:300px; height: 50px;")

        # todays_weather.resize(300, 250)
        for cast in forecast:

            item = QtWidgets.QListWidgetItem("  " + cast['date'] + "     |         H: " + cast['high'] + "˙c" + "  L: " + cast['low'] + "˙c")
            item.setIcon(QtGui.QIcon('Icons/cloud.png'))

            main_frame.addItem(item)

            # layout.addWidget(main_frame)

        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.show()


class TopWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(TopWidget, self).__init__(parent)
        url = requests.get("https://query.yahooapis.com/v1/public/yql?q=select * from weather.forecast where woeid= 1591691&format=json")
        content = url.json()

        # print(content['query']['results']['channel']['item']['forecast'][0]['date'])
        currentDay = content['query']['results']['channel']['item']['condition']
        location = content['query']['results']['channel']['location']
        forecast = content['query']['results']['channel']['item']['forecast']

        main_frame = QtWidgets.QListWidget()
        todays_weather = QtWidgets.QListWidget()
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addWidget(todays_weather)
        layout.addWidget(main_frame)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        print(currentDay)

        mainItem = QtWidgets.QListWidgetItem(location['city'] + " | " + currentDay['temp'])
        todays_weather.addItem(mainItem)
        todays_weather.setStyleSheet(":item{background: rgba(0,255,0,20%); max-width:300px; height: 150px;}")
        todays_weather.setStyleSheet("background: rgba(0,255,0,20%); max-width:300px; height: 150px;")

        # todays_weather.resize(300, 250)

        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.show()
