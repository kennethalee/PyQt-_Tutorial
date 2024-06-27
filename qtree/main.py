import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('PyQt QTreeWidget')
        self.setGeometry(100, 100, 400, 200)

        # Tree
        tree = QTreeWidget(self)
        tree.setColumnCount(2)
        tree.setHeaderLabels(['Departments', 'Employees'])

        departments = ['Sales', 'Marketing', 'HR']
        employees = {
            'Sales': ['John', 'Jane', 'Peter'],
            'Marketing': ['Alice', 'Bob'],
            'HR': ['David'],
        }

        # Add data to tree
        for department in departments:
            department_item = QTreeWidgetItem(tree)
            department_item.setText(0, department)

            # Set child
            for employee in employees[department]:
                employee_item = QTreeWidgetItem(tree)
                employee_item.setText(1, employee)

                department_item.addChild(employee_item)

        # Place tree on main window
        self.setCentralWidget(tree)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
