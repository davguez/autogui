#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# autogui/gui.py
# @Author : David Guez (guezdav@gmail.com)
# @Link   :
# @Date   : 11/06/2019, 22:58:22

from typing import Dict
from PyQt5 import Qt,QtCore,QtGui,QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

class GuiObj:
    def __init__(self,name) -> None:
        self.name = name
        self.type = None
        self.widget : QtWidgets.QWidget = None
        
class Gui(QtWidgets.QWidget):
    def __init__(self, parent: QWidget | None = ..., flags: WindowFlags | WindowType = ...) -> None:
        super().__init__(parent, flags)
        self.vars : Dict[str,GuiObj]= {}
    def add_str(self,name,init_val=''):
        obj = GuiObj(name)
        obj.widget = QtWidgets.QTextInpput(self,text=init_val)
        self.vars[name] = obj
    def add_int(self,name,init_val=0,range=None,entry_type='text'):
        obj = GuiObj(name)
        # case(entry_type)
        obj.widget = QtWidgets.QTextInpput(self,text=init_val)
        self.vars[name] = obj
    def add_float(self,name,init_val=0,range=None,entry_type='text'):
        obj = GuiObj(name)
        # case(entry_type)
        obj.widget = QtWidgets.QTextInpput(self,text=init_val)
        self.vars[name] = obj
    def add_choice(self,name,ini_value=None,chjoices=[]):
        obj = GuiObj(name)
        # case(entry_type)
        obj.widget = QtWidgets.QTextInpput(self,text=init_val)
        self.vars[name] = obj
    def add_list(self,name,ini_value=None,chjoices=[]):
        obj = GuiObj(name)
        # case(entry_type)
        obj.widget = QtWidgets.QTextInpput(self,text=init_val)
        self.vars[name] = obj
