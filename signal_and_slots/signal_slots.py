import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set window title
        self.setWindowTitle('Qt Signals & Slots')

        # Create button and connect signal to method
        button = QPushButton('Click me', clicked=self.button_clicked)
        # button.clicked.connect(self.button_clicked)

        # Place button on window using vertical box layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(button)

        # Show window
        self.show()

    def button_clicked(self):
        print('clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Main window and display
    window = MainWindow()

    # Start event loop
    sys.exit(app.exec())
