import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox,  QGridLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QCheckBox')
        self.setGeometry(100, 100, 320, 210)

        # create a grid layout
        layout = QGridLayout()
        self.setLayout(layout)

        # create a tristate checkbox (partially checked -> neither check/uncheck)
        self.checkbox = QCheckBox('A Tristate Checkbox', self)
        self.checkbox.setTristate(True)

        layout.addWidget(self.checkbox, 0, 0, Qt.AlignmentFlag.AlignCenter)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())