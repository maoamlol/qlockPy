import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


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
        self.one = []
        self.two = []
        self.three = []
        self.four = []
        self.five = []
        self.six = []
        self.seven = []
        self.eight = []
        self.nine = []
        self.ten = []
        self.eleven = []
        self.twelve = []
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
        [s.setStyleSheet(self.style_sheet()) for s in c[1:3]]
        [s.setStyleSheet(self.style_sheet()) for s in c[4:7]]
        self.pre_five = c[8:12]
        self.pre_ten = c[12:16]
        self.pre_quarter = c[27:34]
        self.pre_twenty = c[16:23]
        self.half = c[45:49]
        self.before = c[34:37]
        self.after = c[41:45]
        self.one = c[56:60]
        self.two = c[63:67]
        self.three = c[67:71]
        self.four = c[74:77]
        self.five = c[52:56]
        self.six = c[77:83]
        self.seven = c[89:95]
        self.eight = c[85:89]
        self.nine = c[103:107]
        self.ten = c[100:104]
        self.eleven = c[50:53]
        self.twelve = c[95:100]
        self.o_clock = c[108:]

    def style_sheet(self, active=True):
        return f"QLabel {{background-color: {self.background_color}; color: {self.active_color if active else self.inactive_color}}} "

    def activate_segment(self, segment):
        [s.setStyleSheet(self.style_sheet()) for s in segment]

    def deactivate_segment(self, segment):
        [s.setStyleSheet(self.style_sheet(False)) for s in segment]

    def example_timer(self):
        t = QTimer(self)
        t.setSingleShot(True)
        t.timeout.connect(self.timer_action)
        t.start(4000)

    def timer_action(self):
        self.deactivate_segment(self.twelve)
        print("timer expired loool")


def main():
    app = QApplication(sys.argv)
    c = Qlocktwo()
    # [s.setStyleSheet(c.style_sheet()) for s in c.o_clock]
    # [s.setStyleSheet(c.style_sheet()) for s in c.pre_five]
    # [s.setStyleSheet(c.style_sheet()) for s in c.pre_ten]
    # [s.setStyleSheet(c.style_sheet()) for s in c.pre_quarter]
    # [s.setStyleSheet(c.style_sheet()) for s in c.pre_twenty]
    [s.setStyleSheet(c.style_sheet()) for s in c.half]
    # [s.setStyleSheet(c.style_sheet()) for s in c.before]
    # [s.setStyleSheet(c.style_sheet()) for s in c.after]
    # [s.setStyleSheet(c.style_sheet()) for s in c.one]
    # [s.setStyleSheet(c.style_sheet()) for s in c.two]
    # [s.setStyleSheet(c.style_sheet()) for s in c.three]
    # [s.setStyleSheet(c.style_sheet()) for s in c.four]
    # [s.setStyleSheet(c.style_sheet()) for s in c.five]
    # [s.setStyleSheet(c.style_sheet()) for s in c.six]
    # [s.setStyleSheet(c.style_sheet()) for s in c.seven]
    [s.setStyleSheet(c.style_sheet()) for s in c.eight]
    # [s.setStyleSheet(c.style_sheet()) for s in c.nine]
    # [s.setStyleSheet(c.style_sheet()) for s in c.ten]
    # [s.setStyleSheet(c.style_sheet()) for s in c.eleven]
    # [s.setStyleSheet(c.style_sheet()) for s in c.twelve]
    c.activate_segment(c.twelve)
    c.example_timer()
    app.exec()


if __name__ == '__main__':
    main()
