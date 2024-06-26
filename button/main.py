import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QPushButton Widget')
        self.setGeometry(100, 100, 320, 210)

        button = QPushButton('Delete')
        button.setIcon(QIcon('trash.png'))

        button.setFixedSize(QSize(100, 30))

        # Place widget on window
        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())
