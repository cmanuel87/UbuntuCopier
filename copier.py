# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'copier.ui'
#
# Created: Fri Aug 16 08:36:21 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(470, 373)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 50, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 50, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.progressBar_1 = QtGui.QProgressBar(Form)
        self.progressBar_1.setGeometry(QtCore.QRect(10, 50, 451, 23))
        self.progressBar_1.setProperty("value", 24)
        self.progressBar_1.setObjectName(_fromUtf8("progressBar_1"))
        self.progressBar_2 = QtGui.QProgressBar(Form)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 90, 451, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.more_btn = QtGui.QPushButton(Form)
        self.more_btn.setGeometry(QtCore.QRect(10, 120, 85, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("resources/1376674312_read_more.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.more_btn.setIcon(icon)
        self.more_btn.setIconSize(QtCore.QSize(15, 15))
        self.more_btn.setObjectName(_fromUtf8("more_btn"))
        self.cancel_btn = QtGui.QPushButton(Form)
        self.cancel_btn.setGeometry(QtCore.QRect(380, 120, 81, 27))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("resources/1376674461_cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_btn.setIcon(icon1)
        self.cancel_btn.setIconSize(QtCore.QSize(14, 14))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.pause_btn = QtGui.QPushButton(Form)
        self.pause_btn.setGeometry(QtCore.QRect(290, 120, 85, 27))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("resources/1376674063_media-play-pause-resume.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_btn.setIcon(icon2)
        self.pause_btn.setIconSize(QtCore.QSize(16, 16))
        self.pause_btn.setObjectName(_fromUtf8("pause_btn"))
        self.treeWidget = QtGui.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(10, 160, 451, 201))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "UCopier", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "From:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "To:", None, QtGui.QApplication.UnicodeUTF8))
        self.more_btn.setText(QtGui.QApplication.translate("Form", "More", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("Form", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pause_btn.setText(QtGui.QApplication.translate("Form", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("Form", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("Form", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("Form", "State", None, QtGui.QApplication.UnicodeUTF8))

