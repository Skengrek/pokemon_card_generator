# -*- coding: utf-8 -*-

"""

"""

import sys

from PySide2 import QtCore, QtGui, QtWidgets

from resources.style import stylesheet


# !############################################################################
# ! Miscellaneous classes
# !############################################################################

class AddMinusButtons(QtWidgets.QWidget):
    """
    Basic +/- buttons. it sends one sig per button.
    """

    add_sig = QtCore.Signal()
    min_sig = QtCore.Signal()

    def __init__(self, width=None, height=None):
        super(AddMinusButtons, self).__init__()

        self.setStyleSheet(stylesheet.MISC_BUTTON)

        if width is not None:
            self.setFixedWidth(width)
        if height is not None:
            self.setFixedHeight(height)

        self.button_add = QtWidgets.QPushButton('+')
        self.button_min = QtWidgets.QPushButton('-')
        self.button_add.clicked.connect(self.add_slot)
        self.button_min.clicked.connect(self.min_slot)

        if width is not None:
            self.button_add.setFixedWidth((width/2))
            self.button_min.setFixedWidth((width/2))

        if height is not None:
            self.button_add.setFixedHeight(height)
            self.button_min.setFixedHeight(height)

        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(self.button_add)
        layout.addWidget(self.button_min)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)

    def add_slot(self):
        self.add_sig.emit()

    def min_slot(self):
        self.min_sig.emit()


class LabelEdit(QtWidgets.QWidget):
    """
    Basic Label + Edit zone
    """

    edit_sig = QtCore.Signal(str)

    def __init__(self, name):
        super(LabelEdit, self).__init__()

        self.label = QtWidgets.QLabel(name)
        self.edit = QtWidgets.QLineEdit()
        self.edit.textChanged.connect(self.edit_sig.emit)

        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.edit)

        self.setLayout(layout)


class LabelComboBox(QtWidgets.QWidget):
    """
    Basic label + comboBox zone
    """
    edit_sig = QtCore.Signal()

    def __init__(self, name, _list):
        super(LabelComboBox, self).__init__()

        self.label = QtWidgets.QLabel(name)
        self.combo = QtWidgets.QComboBox()
        self.combo.addItems(_list)

        self.combo.currentTextChanged.connect(self.edit_sig.emit)

        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.combo)

        self.setLayout(layout)


# *############################################################################
# * Main function
# *############################################################################


def main():
    # execute only if run as a script
    app = QtWidgets.QApplication(sys.argv)

    app.exec_()


if __name__ == "__main__":
    main()
