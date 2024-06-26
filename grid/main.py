import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Login Form')

        # set the grid layout
        layout = QGridLayout()
        self.setLayout(layout)

        # parent.setLayout(layout)
        # layout.addWidget(widget, row, column, rowSpan, columnSpan, alignment)

        # Username
        layout.addWidget(QLabel('Username:'), 0, 0)
        layout.addWidget(QLineEdit(), 0, 1)

        # Password
        layout.addWidget(QLabel('Password:'), 1, 0)
        layout.addWidget(QLineEdit(echoMode=QLineEdit.EchoMode.Password), 1, 1)

        # Buttons
        layout.addWidget(QPushButton('Log in'), 2, 0,
                         alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QPushButton('Close'), 2, 1,
                         alignment=Qt.AlignmentFlag.AlignRight)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
