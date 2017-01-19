# -*- coding: utf-8 -*-

"""
Module implementing PyqtDemo.
"""

import sys
import csv
from PIL import Image, ImageQt 
import urllib.request
import io

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui  import QDialog
from PyQt4 import QtGui, QtCore

from Ui_pyqtdemo import Ui_PYQTDIALOG


class PyqtDemo(QDialog, Ui_PYQTDIALOG):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(PyqtDemo, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_btn1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.filename = QtGui.QFileDialog.getOpenFileName(self,"Open file")
        #fname = open(filename,'r')   
        #self.fname = open(filename,'r',encoding="utf16")
        self.btn2.setEnabled(True)

    
    @pyqtSlot()
    def on_btn2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.fname = open(self.filename,'r',encoding="utf16")
        
        reader = csv.reader(self.fname,delimiter='\t')
        
        cnt = 1
        
        for line in reader: 
            if len(line)  ==1:         #first line
               continue
            elif line[0]=="title":
                skuIdx=line.index("skuProps")
                idIdx = line.index("outer_id")
                print(skuIdx)
            elif line[0]=="宝贝名称":
                    continue
            else:
                skuPropsStr=str(line[skuIdx])
                skuProps=skuPropsStr.split(";")
                #print(skuProps)
                sku_cnt=(int)((len(skuProps)-1)/2)
                if sku_cnt==0:
                    continue
                #self.textEdit.append(str(sku_cnt))
                j=0
                for i in range(0, len(skuProps)-1,  2):
                    if str(skuProps[i]).split(":")[1] !='0':
                        j+=1
                #print(j)
                if j/sku_cnt <0.5:
                    #self.textEdit.append("%s:%d" %(line[idIdx], cnt))
                    self.textEdit.append(line[idIdx])
                    cnt+=1
                
                
                
        self.fname.close()    
        
       
            
        
             
        
    @pyqtSlot()
    def on_btn3_clicked(self):
        """
        Slot documentation goes here.
        """
        '''
        # TODO: not implemented yet
        #raise NotImplementedError
        self.fname = open(self.filename,'r',encoding="utf16")
        
        reader = csv.reader(self.fname,delimiter='\t')
        zm = (self.zmnumber.text())
        print(zm[2:])
        find = 0
        for line in reader: 
            if len(line) > 33:	
                if (zm[2:6] in line[33]):
                     find=1
                     id = line[36]
                     picture=line[28]
                     print(id)
                     break
                #else:
                #     print(line[33])
                
        self.fname.close()    
        
        if find:
            netaddr="https://item.taobao.com/item.htm?id=543321968803"
            listaddr=netaddr.split("=")
            listaddr[1]=id
            print(listaddr)
            netaddr="=".join(listaddr)
            self.netaddr.setText(netaddr)
            
            listpic=picture.split("|")
            url = (listpic[1].split(";"))[0]
            #print(url)
            
            image_bytes =  urllib.request.urlopen(url).read()  
            data_stream = io.BytesIO(image_bytes)
            pil_image = Image.open(data_stream) 
            
            #pil_image = Image.open("1.jpg")
            #self.image.setGeometry(0,0,800,800);  
            pil_image_resize=pil_image.resize((100, 100),  Image.ANTIALIAS)
            self.image.resize(100, 100)
            #pil_image.show()
            qt_image1 = ImageQt.ImageQt(pil_image_resize)  
            #qt_image2 = QtGui.QImage(qt_image1)
            pixmap = QtGui.QPixmap.fromImage(qt_image1)
            
            self.image.setPixmap(pixmap)
        
            print(url)
        '''
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(self.netaddr.text()))
        
        
    @pyqtSlot()
    def on_textEdit_selectionChanged(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        zm=str(self.textEdit.textCursor ().selectedText ())
        print(zm)
        
        if zm[0:2]!="ZM":
            return
        self.stLabel.setText(zm)
        self.fname = open(self.filename,'r',encoding="utf16")
        
        reader = csv.reader(self.fname,delimiter='\t')
        #zm = (self.zmnumber.text())
        print(zm[2:])
        find = 0
        for line in reader: 
            if len(line) > 33:	
                if (zm[2:6] in line[33]):
                     find=1
                     id = line[36]
                     picture=line[28]
                     print(id)
                     break
                #else:
                #     print(line[33])
                
        self.fname.close()    
        
        if find:
            netaddr="https://item.taobao.com/item.htm?id=543321968803"
            listaddr=netaddr.split("=")
            listaddr[1]=id
            print(listaddr)
            netaddr="=".join(listaddr)
            self.netaddr.setText(netaddr)
            
            listpic=picture.split("|")
            url = (listpic[1].split(";"))[0]
            #print(url)
            
            image_bytes =  urllib.request.urlopen(url).read()  
            data_stream = io.BytesIO(image_bytes)
            pil_image = Image.open(data_stream) 
            
            #pil_image = Image.open("1.jpg")
            #self.image.setGeometry(0,0,800,800);  
            print(self.image.x(), self.image.y())
            pil_image_resize=pil_image.resize((100, 100),  Image.ANTIALIAS)
            #self.image.resize(100, 100)
            #pil_image.show()
            qt_image1 = ImageQt.ImageQt(pil_image_resize)  
            qt_image2 = QtGui.QImage(qt_image1)
            pixmap = QtGui.QPixmap.fromImage(qt_image2)
            
            self.image.setPixmap(pixmap)
        
            print(url)
        #QtGui.QDesktopServices.openUrl(QtCore.QUrl(self.netaddr.text()))
        self.webView.load(QtCore.QUrl(netaddr))
        self.webView.showMaximized()
        
    @pyqtSlot()
    def on_btncp_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(self.netaddr.text())
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    dlg = PyqtDemo()
    dlg.show()
    sys.exit(app.exec_())
    

