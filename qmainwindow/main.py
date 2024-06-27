import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QToolBar, QStatusBar
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Editor')
        self.setWindowIcon(QIcon('./assets/editor.png'))
        # Appear at (100,100) width 500px height 300px
        self.setGeometry(100, 100, 500, 300)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Setting menu
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('&File')  # & adds underscore
        edit_menu = menu_bar.addMenu('&Edit')
        help_menu = menu_bar.addMenu('&Help')

        file_menu.addAction('New', lambda: self.text_edit.clear())
        file_menu.addAction('Open', lambda: print('Open'))
        file_menu.addAction('Exit', self.destroy)

        undo_action = QAction(QIcon('./assets/undo.png'), 'Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.triggered.connect(self.text_edit.undo)
        # Add undo to edit tab
        edit_menu.addAction(undo_action)

        redo_action = QAction(QIcon('./assets/redo.png'), 'Redo', self)
        redo_action.setShortcut('Ctrl+Y')
        redo_action.triggered.connect(self.text_edit.redo)
        # Add redo to edit tab
        edit_menu.addAction(redo_action)

        # Adding toolbar
        toolbar = QToolBar('Main Toolbar')
        self.addToolBar(toolbar)

        toolbar.addAction(undo_action)
        toolbar.addAction(redo_action)

        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage('Awesome Editor v1.0')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
