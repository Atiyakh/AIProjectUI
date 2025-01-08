import typing
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import PyQt5.QtCore as QtCore
import sqlite3 as sql, time
import sys, requests, os
from PyQt5.QtWidgets import QWidget
import QCustomWidgets
import QTools, QPloting
import pandas as pd

class QPreviewModelWindow(QWidget):
    def __init__(self, model_info):
        super().__init__()
        self.layout_ = QVBoxLayout()
        self.setLayout(self.layout_)
        self.model_info = model_info
        self.initui()
    def initui(self):
        id, family, alg_type, name, binary, reg, bio, related, parameters, plot_ability, import_path, C, alpha, degree, criterion, n_estimators, learning_rate, gamma = self.model_info
        self.setWindowTitle(f'AI Algorithms Preview Model - {name.replace("_", " ")}')
        self.setFixedSize(600, 450)
        self.show()