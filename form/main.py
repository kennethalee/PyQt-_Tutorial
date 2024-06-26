import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,  QFormLayout


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Sign Up Form')

        layout = QFormLayout()
        self.setLayout(layout)

        layout.addRow('Name:', QLineEdit(self))
        layout.addRow('Email:', QLineEdit(self))
        layout.addRow('Password:', QLineEdit(
            self, echoMode=QLineEdit.EchoMode.Password))
        layout.addRow('Confirm Password:', QLineEdit(
            self, echoMode=QLineEdit.EchoMode.Password
        ))
        layout.addRow('Phone:', QLineEdit(self))
        layout.addRow(QPushButton('Sign Up'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
