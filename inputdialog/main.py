import sys
from PyQt6.QtWidgets import QApplication,  QInputDialog, QWidget, QVBoxLayout,  QPushButton


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Input Dialog')
        self.setGeometry(100, 100, 300, 100)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # File selection
        btn = QPushButton('Set Window Title')
        btn.clicked.connect(self.open_input_dialog)

        layout.addWidget(btn)

        self.show()

    def open_input_dialog(self):
        title, ok = QInputDialog.getText(self, 'Title Setting', 'Title:')
        if ok and title:
            self.setWindowTitle(title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
