import sys
from PyQt6.QtWidgets import QInputDialog, QApplication, QWidget,  QGridLayout, QListWidget,  QPushButton
from PyQt6.QtGui import QIcon


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('My Wish List')
        self.setWindowIcon(QIcon('./assets/wishlist.png'))
        self.setGeometry(100, 100, 400, 100)

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.list_widget = QListWidget(self)
        self.list_widget.addItems(['Learn Python', 'Master PyQt'])
        layout.addWidget(self.list_widget, 0, 0, 4, 1)

        # Create buttons
        add_button = QPushButton('Add')
        add_button.clicked.connect(self.add)

        insert_button = QPushButton('Insert')
        insert_button.clicked.connect(self.insert)

        remove_button = QPushButton('Remove')
        remove_button.clicked.connect(self.remove)

        clear_button = QPushButton('Clear')
        clear_button.clicked.connect(self.clear)

        layout.addWidget(add_button, 0, 1)
        layout.addWidget(insert_button, 1, 1)
        layout.addWidget(remove_button, 2, 1)
        layout.addWidget(clear_button, 3, 1)

        self.show()

    def add(self):
        text, ok = QInputDialog.getText(self, 'Add a new wish', 'New Wish:')
        if ok and text:
            self.list_widget.addItem(text)

    def insert(self):
        text, ok = QInputDialog.getText(self, 'Insert a New Wish', 'New Wish:')
        if ok and text:
            current_row = self.list_widget.currentRow()
            self.list_widget.insertItem(current_row+1, text)

    def remove(self):
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            current_item = self.list_widget.takeItem(current_row)
            del current_item

    def clear(self):
        self.list_widget.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
