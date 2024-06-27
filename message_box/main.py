import sys
from PyQt6.QtWidgets import QApplication,  QMessageBox, QWidget, QHBoxLayout,  QPushButton


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QMessageBox')
        self.setGeometry(100, 100, 300, 100)

        layout = QHBoxLayout()
        self.setLayout(layout)

        btn_question = QPushButton('Question')
        btn_question.clicked.connect(self.question)

        btn_info = QPushButton('Information')
        btn_info.clicked.connect(self.info)

        btn_warning = QPushButton('Warning')
        btn_warning.clicked.connect(self.warning)

        btn_critical = QPushButton('Critical')
        btn_critical.clicked.connect(self.critical)

        layout.addWidget(btn_question)
        layout.addWidget(btn_info)
        layout.addWidget(btn_warning)
        layout.addWidget(btn_critical)

        self.show()

    def info(self):
        QMessageBox.information(
            self,
            'Information',
            'This is important information.'
        )

    def warning(self):
        QMessageBox.warning(
            self,
            'Warning',
            'This is a warning message.'
        )

    def critical(self):
        QMessageBox.critical(
            self,
            'Critical',
            'This is a critical message.'
        )

    def question(self):
        answer = QMessageBox.question(
            self,
            'Confirmation',
            'Do you want to quit?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.Yes:
            QMessageBox.information(
                self,
                'Information',
                'You selected Yes. The program will be terminated.',
                QMessageBox.StandardButton.Ok
            )
            self.close()
        else:
            QMessageBox.information(
                self,
                'Information',
                'You selected No.',
                QMessageBox.StandardButton.Ok
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
