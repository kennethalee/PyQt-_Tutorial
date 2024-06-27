import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QProgressBar
from PyQt6.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(100, 100, 300, 50)
        self.setWindowTitle('QProgressBar Demo')

        layout = QVBoxLayout()
        self.setLayout(layout)

        hbox = QHBoxLayout()
        self.progress_bar = QProgressBar(self)
        hbox.addWidget(self.progress_bar)

        layout.addLayout(hbox)

        hbox = QHBoxLayout()
        self.btn_progress = QPushButton('Progress', clicked=self.progress)
        self.btn_reset = QPushButton('Reset', clicked=self.reset)

        # Center button
        hbox.addStretch()
        hbox.addWidget(self.btn_progress)
        hbox.addWidget(self.btn_reset)
        hbox.addStretch()

        layout.addLayout(hbox)
        self.current_value = 0

        self.show()

    def reset(self):
        self.current_value = 0
        self.progress_bar.reset()

    def progress(self):
        if self.current_value <= self.progress_bar.maximum():
            self.current_value += 5
            self.progress_bar.setValue(self.current_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
