import sys
from PyQt6.QtWidgets import QApplication, QWidget, QFormLayout, QGridLayout, QTabWidget, QLineEdit, QDateEdit, QPushButton
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QTabWidget')

        main_layout = QGridLayout(self)
        self.setLayout(main_layout)

        # Create tab widget
        # Instance variable -> global variable, accessible throughout MainWindow class
        self.tab_widget = QTabWidget(self, tabsClosable=True, movable=True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)

        # Personal page
        personal_page = QWidget(self)  # Container
        personal_layout = QFormLayout()  # Form
        personal_page.setLayout(personal_layout)

        # Form properties
        personal_layout.addRow('First Name:', QLineEdit(self))
        personal_layout.addRow('Last Name:', QLineEdit(self))
        personal_layout.addRow('DOB:', QDateEdit(self))

        # Contact page
        contact_page = QWidget(self)
        contact_layout = QFormLayout()
        contact_page.setLayout(contact_layout)
        contact_layout.addRow('Phone Number:', QLineEdit(self))
        contact_layout.addRow('Email Address:', QLineEdit(self))

        # Add panes to tab widget
        self.tab_widget.addTab(personal_page, 'Personal Info')
        self.tab_widget.addTab(contact_page, 'Contact Info')

        main_layout.addWidget(self.tab_widget, 0, 0, 2, 2)  # row, col, row_span, colspan
        main_layout.addWidget(QPushButton('Save'), 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        main_layout.addWidget(QPushButton('Cancel'), 2, 1, alignment=Qt.AlignmentFlag.AlignRight)

        self.show()

    def close_tab(self, index):
        self.tab_widget.removeTab(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
