import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import choices, choice


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.setWindowTitle('Simulator of Japan flag')
        self.pushButton.clicked.connect(self.repaint)

    def draw(self, qp):
        qp.begin(self)
        qp.setBrush(QtGui.QBrush(QtGui.QColor('#FF0000')))
        qp.drawEllipse(self.rect().center(), *self.random_size())

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        self.draw(qp)
        qp.end()
        
    def random_size(self):
        return choices(range(256), k=2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())