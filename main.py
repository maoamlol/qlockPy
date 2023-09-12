import datetime
import json
import sys

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel, QApplication

time_api = 'http://worldtimeapi.org/api/timezone/Europe/Berlin'


def fetch_time() -> datetime:
    try:
        response = requests.get(time_api, timeout=30)
    except Exception as e:
        print('Something went wrong')
        print(e)
        return datetime.datetime.now()
    data = json.loads(response.text)
    time = datetime.datetime.fromisoformat(data['datetime'])
    return time

# Testkommentar
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
            4: c[74:78],
            5: c[52:56],
            6: c[78:83],
            7: c[89:95],
            8: c[85:89],
            9: c[103:107],
            10: c[100:104],
            11: c[50:53],
            0: c[95:100]
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
        t.setInterval(5_000)
        t.timeout.connect(self.timer_action)
        t.start(0)

    def timer_action(self):
        time = fetch_time()
        hour = time.hour % 12
        minute = time.minute
        self.reset()
        print(hour if minute < 23 else hour + 1)
        self.activate_segment(self.hours[hour if minute < 23 else (hour + 1) % 12])
        if 2 < minute < 23 or 32 < minute < 38:
            self.activate_segment(self.after)
        elif 22 < minute < 28 or 58 > minute > 37:
            self.activate_segment(self.before)

        minute_diff = abs(minute - 30)

        if minute_diff < 3:
            self.activate_segment(self.half)
        elif minute_diff < 8:
            self.activate_segment(self.half)
            self.activate_segment(self.pre_five)
        elif minute_diff < 13:
            self.activate_segment(self.pre_twenty)
        elif minute_diff < 18:
            self.activate_segment(self.pre_quarter)
        elif minute_diff < 23:
            self.activate_segment(self.pre_ten)
        elif minute_diff < 28:
            self.activate_segment(self.pre_five)
        else:
            self.activate_segment(self.o_clock)


def main():
    app = QApplication(sys.argv)
    c = Qlocktwo()
    c.start_timer()
    app.exec()


if __name__ == '__main__':
    main()
