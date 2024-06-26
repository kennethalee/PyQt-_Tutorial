import sys
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QComboBox
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QComboBox')
        self.setMinimumWidth(300)

        # create a grid layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        cb_label = QLabel('Please select a platform:', self)

        # Create combobox
        self.cb_platform = QComboBox(self)
        self.cb_platform.addItem('Android')
        self.cb_platform.addItem('iOS')
        self.cb_platform.addItem('Windows')

        self.cb_platform.activated.connect(self.update)

        self.result_label = QLabel('', self)

        layout.addWidget(cb_label)
        layout.addWidget(self.cb_platform)
        layout.addWidget(self.result_label)

        self.show()

    def update(self):
        self.result_label.setText(
            f'You selected {self.cb_platform.currentText()}'
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())