import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog, QMessageBox, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon, QAction


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowIcon(QIcon('./assets/editor.png'))
        self.setGeometry(100, 100, 500, 300)

        self.title = 'Editor'
        self.filters = 'Text Files (*.txt)'
        self.set_title()

        self.path = None  # Currently open/saved file path

        self.text_edit = QTextEdit(self)
        # self.setCentralWidget(self.text_edit)

        # Make text edit widget
        container = QWidget(self)
        container.setLayout(QVBoxLayout())
        container.layout().addWidget(self.text_edit)
        self.setCentralWidget(container)
        # container.setContentsMargins(5, 5, 5, 5)

        # Menu bar
        menu_bar = self.menuBar()

        # Menu bar propreties
        file_menu = menu_bar.addMenu('&File')  # & -> ctrl + F shortcut
        edit_menu = menu_bar.addMenu('&Edit')
        help_menu = menu_bar.addMenu('&Help')

        # new menu item
        new_action = QAction(QIcon('./assets/new.png'), '&New', self)
        new_action.setStatusTip('Create a new document')  # Set status
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.new_document)
        file_menu.addAction(new_action)  # Add to file tab

        # open menu item
        open_action = QAction(QIcon('./assets/open.png'), '&Open...', self)
        open_action.triggered.connect(self.open_document)
        open_action.setStatusTip('Open a document')
        open_action.setShortcut('Ctrl+O')
        file_menu.addAction(open_action)

        # save menu item
        save_action = QAction(QIcon('./assets/save.png'), '&Save', self)
        save_action.setStatusTip('Save the document')
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_document)
        file_menu.addAction(save_action)

        file_menu.addSeparator()  # Seperator

        # exit menu item
        exit_action = QAction(QIcon('./assets/exit.png'), '&Exit', self)
        exit_action.setStatusTip('Exit')
        exit_action.setShortcut('Alt+F4')
        exit_action.triggered.connect(self.quit)
        file_menu.addAction(exit_action)

        # edit menu
        undo_action = QAction(QIcon('./assets/undo.png'), '&Undo', self)
        undo_action.setStatusTip('Undo')
        undo_action.setShortcut('Ctrl+Z')
        undo_action.triggered.connect(self.text_edit.undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction(QIcon('./assets/redo.png'), '&Redo', self)
        redo_action.setStatusTip('Redo')
        redo_action.setShortcut('Ctrl+Y')
        redo_action.triggered.connect(self.text_edit.redo)
        edit_menu.addAction(redo_action)

        about_action = QAction(QIcon('./assets/about.png'), 'About', self)
        help_menu.addAction(about_action)
        about_action.setStatusTip('About')
        about_action.setShortcut('F1')

        # status bar
        self.status_bar = self.statusBar()
        self.show()

    def set_title(self, filename=None):
        title = f"{filename if filename else 'Untitled'} - {self.title}"
        self.setWindowTitle(title)

    def confirm_save(self):
        # Check for unsaved changes (is it modified since last saved/opened)
        if not self.text_edit.document().isModified():
            return True

        message = f"Do you want to save changes to {
            self.path if self.path else 'Untitled'}?"
        MsgBoxBtn = QMessageBox.StandardButton
        MsgBoxBtn = MsgBoxBtn.Save | MsgBoxBtn.Discard | MsgBoxBtn.Cancel

        button = QMessageBox.question(
            self, self.title, message, buttons=MsgBoxBtn
        )

        if button == MsgBoxBtn.Cancel:
            return False

        if button == MsgBoxBtn.Save:
            self.save_document()

        return True

    def new_document(self):
        if self.confirm_save():
            self.text_edit.clear()
            self.set_title()

    def save_document(self):
        # save the currently openned file
        if (self.path):
            return self.path.write_text(self.text_edit.toPlainText())

        # save a new file
        filename, _ = QFileDialog.getSaveFileName(
            self, 'Save File', filter=self.filters
        )

        if not filename:
            return

        self.path = Path(filename)
        self.path.write_text(self.text_edit.toPlainText())
        self.set_title(filename)

    def open_document(self):
        filename, _ = QFileDialog.getOpenFileName(self, filter=self.filters)
        if filename:
            self.path = Path(filename)
            self.text_edit.setText(self.path.read_text())
            self.set_title(filename)

    def quit(self):
        if self.confirm_save():
            self.destroy()


if __name__ == '__main__':
    try:
        import ctypes
        myappid = 'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    finally:
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec())
