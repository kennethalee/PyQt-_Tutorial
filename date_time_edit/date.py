import sys
from PyQt6.QtWidgets import QApplication, QWidget, QDateEdit, QLabel, QFormLayout
from datetime import date


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QDateEdit')
        self.setMinimumWidth(200)

        # create a grid layout
        layout = QFormLayout()
        self.setLayout(layout)

        self.date_edit = QDateEdit(self)
        self.date_edit.editingFinished.connect(self.update)

        self.result_label = QLabel('', self)

        layout.addRow('Date:', self.date_edit)
        layout.addRow(self.result_label)

        # show the window
        self.show()

    def update(self):
        value = self.date_edit.date()
        print(type(value))
        self.result_label.setText(str(value.toPyDate()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())