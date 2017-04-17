import sys
from PyQt5 import QtWidgets, QtCore
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
        self.show()


class WeatherWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(WeatherWidget, self).__init__(parent)
        url = requests.get("https://query.yahooapis.com/v1/public/yql?q=select * from weather.forecast where woeid= 1591691&format=json")
        content = url.json()
        with open('data.json', 'w') as outfile:
            json.dump(content, outfile)

        # print(content['query']['results']['channel']['item']['forecast'][0]['date'])

        main_frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout()
        main_frame.resize(300, 321)
        main_frame.setStyleSheet("background-color: rgb(200, 255, 255)")
        layout.addWidget(main_frame)
        self.setLayout(layout)

        forecast = content['query']['results']['channel']['item']['forecast']

        for cast in forecast:
            print(cast)
            label = QtWidgets.QLabel(self)
            label.setText(cast['date'])
            layout.addWidget(label)
            label.setStyleSheet("background-color: rgb(200, 255, 255)")
        # self.setWindowState(QtCore.Qt.WindowMaximized)
        self.show()

    def WeatherApi():
        http = urllib3.PoolManager()
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select * from weather.forecast where woeid= 1591691"
        yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
        result = http.request('GET', yql_url)
        data = json.loads(result.data.decode('utf-8'))
        print(data)
        print (data['query']['results'])

        widget_frame = QtWidgets.QFrame()
        layout = QtWidgets.QVBoxLayout()
        widget_frame.resize(300, 300)
        layout.addWidget(widget_frame)
        self.setLayout(layout)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        label = QtWidgets.QLabel(self)
        label.setText("hi")
        self.show()
