import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QCheckBox')
        self.setGeometry(100, 100, 320, 210)
    
        layout = QGridLayout()
        self.setLayout(layout)

        # Checkbox
        checkbox = QCheckBox('I agree', self)

        layout.addWidget(checkbox, 0, 0, Qt.AlignmentFlag.AlignCenter)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
