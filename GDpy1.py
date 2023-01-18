import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class DorkingApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.selected_query = "site"
        self.input_text = ""

        self.query_group = QtWidgets.QButtonGroup(self)
        self.site_button = QtWidgets.QRadioButton("site", self)
        self.filetype_button = QtWidgets.QRadioButton("filetype", self)
        self.query_group.addButton(self.site_button)
        self.query_group.addButton(self.filetype_button)
        self.site_button.setChecked(True)

        self.input_field = QtWidgets.QLineEdit(self)

        self.generate_key_button = QtWidgets.QPushButton("Generate Key", self)
        self.generate_key_button.clicked.connect(self.generate_key)

        self.key_label = QtWidgets.QLabel("", self)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.site_button)
        layout.addWidget(self.filetype_button)
        layout.addWidget(self.input_field)
        layout.addWidget(self.generate_key_button)
        layout.addWidget(self.key_label)

        self.setLayout(layout)
        self.setWindowTitle("Google Dorking App")

    def generate_key(self):
        self.selected_query = self.query_group.checkedButton().text()
        self.input_text = self.input_field.text()
        response = requests.get(f'https://www.google.com/search?q={self.selected_query}:{self.input_text}')
        # parse the response to extract the relevant information
        # ...
        key = extracted_key
        self.key_label.setText(key)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dorking_app = DorkingApp()
    dorking_app.show()
    sys.exit(app.exec_())
