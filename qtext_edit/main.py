import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QFormLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt TexEdit')
        self.setMinimumWidth(200)

        layout = QFormLayout()
        self.setLayout(layout)
        # Text edit widget
        text_edit = QTextEdit(self)
        layout.addRow(text_edit)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
