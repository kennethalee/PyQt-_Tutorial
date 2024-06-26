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

        checkbox = QCheckBox('I agree', self)
        # stateChanged
        checkbox.stateChanged.connect(self.on_checkbox_changed)

        layout.addWidget(checkbox, 0, 0, Qt.AlignmentFlag.AlignCenter)

        self.show()

    # Check state
    def on_checkbox_changed(self, value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            print('Checked')
        elif state == Qt.CheckState.Unchecked:
            print('Unchecked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())