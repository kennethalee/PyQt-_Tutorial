import sys
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QRadioButton')
        self.setMinimumWidth(300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Please select a platform:', self)
        
        rb_android = QRadioButton('Android', self)
        # Connect update method to toggled signal
        rb_android.toggled.connect(self.update)

        rb_ios = QRadioButton('iOS', self)
        rb_ios.toggled.connect(self.update)

        rb_windows = QRadioButton('Windows', self)
        rb_windows.toggled.connect(self.update)

        self.result_label = QLabel('', self)

        layout.addWidget(label)
        layout.addWidget(rb_android)
        layout.addWidget(rb_ios)
        layout.addWidget(rb_windows)
        layout.addWidget(self.result_label)

        self.show()

    def update(self):
        # Get radio button to send signal
        # Find toggle button that sent signal
        rb = self.sender()

        # Check if radio button is checked
        if rb.isChecked():
            self.result_label.setText(f'You selected {rb.text()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


