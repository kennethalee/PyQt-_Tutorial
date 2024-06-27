import sys
from PyQt6.QtWidgets import QApplication,  QFileDialog, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel
from pathlib import Path


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt File Dialog')
        self.setGeometry(100, 100, 400, 100)

        layout = QGridLayout()
        self.setLayout(layout)

        # directory selection
        dir_btn = QPushButton('Browse')
        dir_btn.clicked.connect(self.open_dir_dialog)
        self.dir_name_edit = QLineEdit()

        layout.addWidget(QLabel('Directory:'), 1, 0)
        layout.addWidget(self.dir_name_edit, 1, 1)
        layout.addWidget(dir_btn, 1, 2)

        self.show()

    def open_dir_dialog(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory")
        if dir_name:
            path = Path(dir_name)
            self.dir_name_edit.setText(str(path))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
