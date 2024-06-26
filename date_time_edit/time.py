import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTimeEdit, QLabel, QFormLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QTimeEdit')
        self.setMinimumWidth(200)

        # create a grid layout
        layout = QFormLayout()
        self.setLayout(layout)

        self.time_edit = QTimeEdit(self)
        self.time_edit.editingFinished.connect(self.update)

        self.result_label = QLabel('', self)

        layout.addRow('Time:', self.time_edit)
        layout.addRow(self.result_label)

        self.show()

    def update(self):
        value = self.time_edit.time()
        self.result_label.setText(str(value.toPyTime()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())