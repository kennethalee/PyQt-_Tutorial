import sys
from PyQt6.QtWidgets import QApplication, QWidget,  QLineEdit,  QFormLayout,  QHBoxLayout

# Container for other widgets

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt Widget Demo')

        # create an input pane
        layout = QHBoxLayout()
        self.setLayout(layout)

        # person pane
        person_pane = QWidget(self)
        form_layout = QFormLayout()
        person_pane.setLayout(form_layout)
        form_layout.addRow('First Name:', QLineEdit(person_pane))
        form_layout.addRow('Last Name:', QLineEdit(person_pane))
        form_layout.addRow('Date of Birth:', QLineEdit(person_pane))
        form_layout.addRow('Email Address:', QLineEdit(person_pane))
        form_layout.addRow('Phone Number:', QLineEdit(person_pane))
        layout.addWidget(person_pane)

        # address pane
        address_pane = QWidget(self)  # Making a container for other widgets
        form_layout = QFormLayout()
        address_pane.setLayout(form_layout)
        form_layout.addRow('Street:', QLineEdit(address_pane))
        form_layout.addRow('City:', QLineEdit(address_pane))
        form_layout.addRow('State/Province:', QLineEdit(address_pane))
        form_layout.addRow('Zip Code:', QLineEdit(address_pane))
        form_layout.addRow('Country:', QLineEdit(address_pane))
        layout.addWidget(address_pane)

        # show the window
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
