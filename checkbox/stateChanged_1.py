import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QGridLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QCheckBox')
        self.setGeometry(100, 100, 320, 210)

        # create a grid layout
        layout = QGridLayout()
        self.setLayout(layout)

        # Attribute of class Checkbox
        self.checkbox = QCheckBox('I agree', self)

        check_button = QPushButton('Check', self)
        check_button.clicked.connect(self.check)

        uncheck_button = QPushButton('Uncheck', self)
        uncheck_button.clicked.connect(self.uncheck)

        layout.addWidget(self.checkbox, 0, 0, 0, 2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(check_button, 1, 0)
        layout.addWidget(uncheck_button, 1, 1)

        self.show()

    # Programmatically check and uncheck
    def check(self):
        self.checkbox.setChecked(True)

    def uncheck(self):
        self.checkbox.setChecked(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
