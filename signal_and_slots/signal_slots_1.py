import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set window title
        self.setWindowTitle('Qt Signals & Slots')

        # Create widgets
        label = QLabel()  # Receiver
        line_edit = QLineEdit()  # Sender
        line_edit.textChanged.connect(label.setText)

        # textChanged signal sends text
        # QLabel receives, send to setText() -> method

        # Place widgets
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)
        self.setLayout(layout)

        # Show window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
