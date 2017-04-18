import sys
import math
from PyQt5 import QtWidgets, QtCore, QtGui
import requests


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(1120, 20, 300, 621)
        self.setWindowTitle("Weatherfy")
        self.setCentralWidget(WeatherWidget(self))
        self.setContentsMargins(0, 0, 0, 0)
        settings = QtWidgets.QAction("Location", self)
        extractAction = QtWidgets.QAction("Close Weatherly  ctr+Q", self)

        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Quit")
        menubar = self.menuBar()

        file = menubar.addMenu("Weatherfy")
        file.addAction(settings)
        file.addAction(extractAction)

        def menu(self):
            extractAction = QtWidgets.QAction("&Quit", self)
            extractAction.setShortcut("Ctrl+Q")
            extractAction.triggered.connect(self.quitApplication)

        def quitApplication(self):
            print("Application Closed")
            sys.exit()


class WeatherWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(WeatherWidget, self).__init__(parent)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.startDownload()
        spinner = Overlay()
        spinner
        self.show()

    def startDownload(self):
        url = "https://query.yahooapis.com/v1/public/yql?q=select * from weather.forecast where woeid= 1591691 and u='c'&format=json"
        self.threads = []
        download = YahooApi(url)
        download.data_downloaded.connect(self.on_data_ready)
        self.threads.append(download)
        download.start()

    def on_data_ready(self, data):
        content = data
        currentDay = content['query']['results']['channel']['item']['condition']
        location = content['query']['results']['channel']['location']
        forecast = content['query']['results']['channel']['item']['forecast']
        self.setGeometry(1440, 0, 300, 621)
        label = QtWidgets.QLabel(self)
        label.setText(currentDay['temp'] + "˚c")

        main_frame = QtWidgets.QListWidget()
        main_frame.setObjectName("city")
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

        for cast in forecast:

            item = QtWidgets.QListWidgetItem("  " + cast['date'] + "     |         H: " + cast['high'] + "˙c" + "  L: " + cast['low'] + "˙c")
            item.setIcon(QtGui.QIcon('Icons/cloud.png'))

            main_frame.addItem(item)


class YahooApi(QtCore.QThread):
    data_downloaded = QtCore.pyqtSignal(object)

    def __init__(self, url):
        QtCore.QThread.__init__(self)
        self.url = url

    def run(self):
        info = requests.get(self.url)
        content = info.json()
        print(content)
        self.data_downloaded.emit(content)


class Overlay(QtWidgets.QWidget):

    def __init__(self, parent=None):

        QtWidgets.QWidget.__init__(self, parent)
        palette = QtGui .QPalette(self.palette())
        palette.setColor(palette.Background, QtCore.Qt.transparent)
        self.setPalette(palette)

    def paintEvent(self, event):

        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 127)))
        painter.setPen(QPen(Qt.NoPen))

        for i in range(6):
            if (self.counter / 5) % 6 == i:
                painter.setBrush(QBrush(QColor(127 + (self.counter % 5) * 32, 127, 127)))
            else:
                painter.setBrush(QBrush(QColor(127, 127, 127)))
            painter.drawEllipse(
                self.width() / 2 + 30 * math.cos(2 * math.pi * i / 6.0) - 10,
                self.height() / 2 + 30 * math.sin(2 * math.pi * i / 6.0) - 10,
                20, 20)

        painter.end()

    def showEvent(self, event):

        self.timer = self.startTimer(50)
        self.counter = 0

    def timerEvent(self, event):

        self.counter += 1
        self.update()
        if self.counter == 60:
            self.killTimer(self.timer)
            self.hide()
