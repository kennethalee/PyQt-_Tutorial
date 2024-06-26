import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QVBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QlineEdit Widget')
        self.setGeometry(100, 100, 320, 210)

        search_box = QLineEdit(
            self,
            placeholderText='Enter a keyword to search...',
            clearButtonEnabled=True
        )

        # Place widget on window
        layout = QVBoxLayout()
        layout.addWidget(search_box)
        self.setLayout(layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
