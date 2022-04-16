import sys
import requests
import json

import datetime

from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

time_api = 'http://worldtimeapi.org/api/timezone/Europe/Berlin'


def fetch_time() -> datetime:
    try:
        response = requests.get(time_api)
    except Exception as e:
        print('Something went wrong')
        print(e)
        return datetime.datetime.now()
    data = json.loads(response.text)
    time = datetime.datetime.fromisoformat(data['datetime'])
    return time


class Qlocktwo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tile_size = 0
        self.NUM_ROWS = 10
        self.NUM_COLS = 11
        self.CLOCK_TEXT = "ESKISTAFÜNFZEHNZWANZIGDREIVIERTELVORFUNKNACHHALBAELF" \
                          "ÜNFEINSXAMZWEIDREIPMJVIERSECHSNLACHTSIEBENZWÖLFZEHNEUNKUHR"
        self.font_name = "Exodus Demo Stencil"
        self.background_color = "black"
        self.active_color = "white"
        self.inactive_color = "rgb(100,100,100)"
        self.pre_five = []
        self.pre_ten = []
        self.pre_quarter = []
        self.pre_twenty = []
        self.half = []
        self.before = []
        self.after = []
        self.hours = {}
        self.o_clock = []
        self.clock_area = None
        self.main_window = None
        self.init_ui()

    def init_ui(self):
        # self.main_window = QLabel(self)
        # self.setCentralWidget(self.main_window)
        self.show()
        self.showFullScreen()
        self.setStyleSheet(self.style_sheet(False))
        self.main_window = QLabel(self)
        layout = QHBoxLayout()
        self.main_window.setLayout(layout)
        self.setCentralWidget(self.main_window)
        self.clock_area = QLabel(self.main_window)
        layout.addWidget(self.clock_area)
        if self.height() > self.width():
            self.tile_size = self.width() // 12
        else:
            self.tile_size = self.height() // 13
        self.clock_area.setFixedWidth(self.tile_size * 11)
        self.clock_area.setFixedHeight(self.tile_size * 10)
        self.main_window.setAlignment(Qt.AlignCenter)
        self.clock_area.setStyleSheet(self.style_sheet(False))
        self.init_clock_area()

    def init_clock_area(self):
        layout = QGridLayout()
        self.clock_area.setLayout(layout)
        layout.setAlignment(Qt.AlignCenter)
        for i in range(len(self.CLOCK_TEXT)):
            label = QLabel(self.clock_area)
            label.setFixedSize(self.tile_size, self.tile_size)
            label.setAlignment(Qt.AlignCenter)
            label.setText(self.CLOCK_TEXT[i])
            label.setFont(QFont(self.font_name, int(self.tile_size * .65)))
            layout.addWidget(label, i // 11, i % 11)
        c = self.clock_area.children()
        # "ES IST" always on
        [s.setStyleSheet(self.style_sheet()) for s in c[1:3]]
        [s.setStyleSheet(self.style_sheet()) for s in c[4:7]]
        self.pre_five = c[8:12]
        self.pre_ten = c[12:16]
        self.pre_quarter = c[27:34]
        self.pre_twenty = c[16:23]
        self.half = c[45:49]
        self.before = c[34:37]
        self.after = c[41:45]
        self.hours = {
            1: c[56:60],
            2: c[63:67],
            3: c[67:71],
            4: c[74:77],
            5: c[52:56],
            6: c[77:83],
            7: c[89:95],
            8: c[85:89],
            9: c[103:107],
            10: c[100:104],
            11: c[50:53],
            12: c[95:100]
        }
        self.o_clock = c[108:]

    def style_sheet(self, active=True):
        return f"QLabel {{background-color: {self.background_color}; " \
               f"color: {self.active_color if active else self.inactive_color}}} "

    def activate_segment(self, segment):
        [s.setStyleSheet(self.style_sheet()) for s in segment]

    def deactivate_segment(self, segment):
        [s.setStyleSheet(self.style_sheet(False)) for s in segment]

    def reset(self):
        for segment in self.hours.values():
            self.deactivate_segment(segment)
        self.deactivate_segment(self.pre_five)
        self.deactivate_segment(self.pre_ten)
        self.deactivate_segment(self.pre_quarter)
        self.deactivate_segment(self.pre_twenty)
        self.deactivate_segment(self.half)
        self.deactivate_segment(self.before)
        self.deactivate_segment(self.after)
        self.deactivate_segment(self.o_clock)

    def start_timer(self):
        t = QTimer(self)
        t.setInterval(60_000)
        t.timeout.connect(self.timer_action)
        t.start(4000)

    def timer_action(self):
        time = fetch_time()
        hour = time.hour
        minute = time.minute
        self.reset()


def main():
    app = QApplication(sys.argv)
    c = Qlocktwo()
    # [s.setStyleSheet(c.style_sheet()) for s in c.o_clock]
    # [s.setStyleSheet(c.style_sheet()) for s in c.pre_five]
    # [s.setStyleSheet(c.style_sheet()) for s in c.pre_ten]
    # [s.setStyleSheet(c.style_sheet()) for s in c.pre_quarter]
    # [s.setStyleSheet(c.style_sheet()) for s in c.pre_twenty]
    # [s.setStyleSheet(c.style_sheet()) for s in c.before]
    # [s.setStyleSheet(c.style_sheet()) for s in c.after]
    # [s.setStyleSheet(c.style_sheet()) for s in c.one]
    # [s.setStyleSheet(c.style_sheet()) for s in c.two]
    # [s.setStyleSheet(c.style_sheet()) for s in c.three]
    # [s.setStyleSheet(c.style_sheet()) for s in c.four]
    # [s.setStyleSheet(c.style_sheet()) for s in c.five]
    # [s.setStyleSheet(c.style_sheet()) for s in c.six]
    # [s.setStyleSheet(c.style_sheet()) for s in c.seven]
    # [s.setStyleSheet(c.style_sheet()) for s in c.nine]
    # [s.setStyleSheet(c.style_sheet()) for s in c.ten]
    # [s.setStyleSheet(c.style_sheet()) for s in c.eleven]
    # [s.setStyleSheet(c.style_sheet()) for s in c.twelve]
    c.activate_segment(c.hours[12])
    c.activate_segment(c.o_clock)
    c.start_timer()
    app.exec()


if __name__ == '__main__':
    main()
