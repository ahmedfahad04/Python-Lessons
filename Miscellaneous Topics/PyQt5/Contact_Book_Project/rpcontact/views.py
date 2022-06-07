# -*- coding: utf-8 -*-
# rpcontacts/views.py

"""This module provides views to manage the contacts table."""

from PyQt5.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("RP Contacts")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.setupUi()

    def setupUi(self):
        """Setup the main window's GUI."""

        # Create the table view widget
        self.table = QTableView()
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        # Create buttons
        self.addButton = QPushButton("Add...")
        self.deleteButton = QPushButton("Delete")
        self.clearAllButton = QPushButton("Clear All")
        self.modify = QPushButton("Update")
        self.plus = QPushButton("+")
        self.minus = QPushButton("-")

        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        layout.addWidget(self.modify)
        layout.addStretch()
        layout.addWidget(self.plus)
        layout.addWidget(self.minus)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
