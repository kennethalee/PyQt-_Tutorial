import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QHBoxLayout')

        # Create a layout
        layout = QHBoxLayout()
        self.setLayout(layout)

        titles = ['Yes', 'No', 'Cancel']
        buttons = [QPushButton(title) for title in titles]

        # Add buttons and stretch factor for button size
        layout.addWidget(buttons[0], 2)
        layout.addWidget(buttons[1], 2)

        # Stretcher
        layout.addStretch()

        # Add last button
        layout.addWidget(buttons[2])

        # add layout spacing
        layout.setSpacing(50)

        # Add margin left, top, right, bottom
        layout.setContentsMargins(50, 50, 50, 50)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
