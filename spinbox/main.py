import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSpinBox, QLabel, QFormLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QSpinBox')
        self.setMinimumWidth(300)

        # create a grid layout
        layout = QFormLayout()
        self.setLayout(layout)

        amount = QSpinBox(minimum=1, maximum=100, value=20, prefix='$')

        # Connect valueChanged signal to update method
        amount.valueChanged.connect(self.update)

        self.result_label = QLabel('', self)

        layout.addRow('Amount', amount)
        layout.addRow(self.result_label)

        self.show()
    
    def update(self, value):
        self.result_label.setText(f'Current value: {value}')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())