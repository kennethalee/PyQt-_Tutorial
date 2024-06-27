import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel
from pathlib import Path

# Opening multiple file using openfilenames


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt File Dialog')
        self.setGeometry(100, 100, 400, 100)

        layout = QGridLayout()
        self.setLayout(layout)

        # file selection
        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.open_file_dialog)
        self.filename_edit = QLineEdit()

        layout.addWidget(QLabel('File:'), 0, 0)
        layout.addWidget(self.filename_edit, 0, 1)
        layout.addWidget(file_browse, 0, 2)

        self.show()

    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            "D:\\icons\\avatar\\",
            "Images (*.png *.jpg)"
        )
        if filename:
            path = Path(filename)
            self.filename_edit.setText(str(path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
