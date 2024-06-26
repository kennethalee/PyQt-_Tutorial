import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Label Widget')
        self.setGeometry(100, 100, 320, 210)

        label = QLabel()
        pixmap = QPixmap('./logo.png')
        label.setPixmap(pixmap)

        # Place widget on window
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
