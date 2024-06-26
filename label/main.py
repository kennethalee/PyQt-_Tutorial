import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Label Widget')
        self.setGeometry(100, 100, 320, 210)

        # QLabel widget
        label = QLabel('This is Qlabel widget')

        # Also valid syntax
        # label = QLabel()
        # label.setText('This is QLabel widget')

        # Place on window
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())
