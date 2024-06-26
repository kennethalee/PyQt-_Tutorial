import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QMovie


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QLabel Widget')
        self.setGeometry(100, 100, 320, 210)

        # GIF
        label = QLabel()
        movie = QMovie('python.gif')
        label.setMovie(movie)
        movie.start()

        # place the widget on the window
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())
