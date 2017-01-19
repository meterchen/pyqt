# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\TestSpace\pyqt\pyqtdemo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PYQTDIALOG(object):
    def setupUi(self, PYQTDIALOG):
        PYQTDIALOG.setObjectName(_fromUtf8("PYQTDIALOG"))
        PYQTDIALOG.resize(982, 611)
        PYQTDIALOG.setSizeGripEnabled(False)
        self.btn2 = QtGui.QPushButton(PYQTDIALOG)
        self.btn2.setEnabled(False)
        self.btn2.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.image = QtGui.QLabel(PYQTDIALOG)
        self.image.setGeometry(QtCore.QRect(20, 500, 101, 101))
        self.image.setText(_fromUtf8(""))
        self.image.setTextFormat(QtCore.Qt.PlainText)
        self.image.setObjectName(_fromUtf8("image"))
        self.btn1 = QtGui.QPushButton(PYQTDIALOG)
        self.btn1.setEnabled(True)
        self.btn1.setGeometry(QtCore.QRect(29, 9, 75, 23))
        self.btn1.setObjectName(_fromUtf8("btn1"))
        self.textEdit = QtGui.QTextEdit(PYQTDIALOG)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 101, 411))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.webView = QtWebKit.QWebView(PYQTDIALOG)
        self.webView.setGeometry(QtCore.QRect(139, 30, 841, 571))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.netaddr = QtGui.QLineEdit(PYQTDIALOG)
        self.netaddr.setGeometry(QtCore.QRect(140, 0, 351, 21))
        self.netaddr.setReadOnly(True)
        self.netaddr.setObjectName(_fromUtf8("netaddr"))
        self.btn3 = QtGui.QPushButton(PYQTDIALOG)
        self.btn3.setGeometry(QtCore.QRect(580, 0, 71, 23))
        self.btn3.setObjectName(_fromUtf8("btn3"))
        self.btncp = QtGui.QPushButton(PYQTDIALOG)
        self.btncp.setGeometry(QtCore.QRect(650, 0, 75, 23))
        self.btncp.setObjectName(_fromUtf8("btncp"))
        self.stLabel = QtGui.QLabel(PYQTDIALOG)
        self.stLabel.setGeometry(QtCore.QRect(510, 10, 54, 12))
        self.stLabel.setText(_fromUtf8(""))
        self.stLabel.setObjectName(_fromUtf8("stLabel"))

        self.retranslateUi(PYQTDIALOG)
        QtCore.QMetaObject.connectSlotsByName(PYQTDIALOG)

    def retranslateUi(self, PYQTDIALOG):
        PYQTDIALOG.setWindowTitle(_translate("PYQTDIALOG", "查找断码", None))
        self.btn2.setText(_translate("PYQTDIALOG", "查找", None))
        self.btn1.setText(_translate("PYQTDIALOG", "打开", None))
        self.btn3.setText(_translate("PYQTDIALOG", "外部浏览器", None))
        self.btncp.setText(_translate("PYQTDIALOG", "复制", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PYQTDIALOG = QtGui.QDialog()
    ui = Ui_PYQTDIALOG()
    ui.setupUi(PYQTDIALOG)
    PYQTDIALOG.show()
    sys.exit(app.exec_())

