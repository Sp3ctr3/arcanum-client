#!/usr/bin/python2.7
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QFileDialog,QMessageBox,QStringListModel
import sys,os,re
from PyQt4.QtCore import QString
from login import Ui_Dialog as Ui_Form1
from main import Ui_Dialog as Ui_Form2 
from register import Ui_Dialog as Ui_Form3
import requests as req
import binascii
import hashlib
from keyczar.keys import RsaPrivateKey,RsaPublicKey,AesKey
from decrypt import decrypt,encrypt_file,decrypt_file
fromUtf8 = QtCore.QString.fromUtf8
global creds,address
class LoginForm(QtGui.QWidget, Ui_Form1):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.Login.clicked.connect(self.handleButton)
        self.register_2.clicked.connect(self.handleRegister)
        self.window2 = None

    def handleButton(self):
        if self.window2 is None:
            global creds,address
            creds=(str(self.username.text()),str(self.password.text()))
            address=self.address.text()
            if req.get(address+"/auth/",auth=creds,verify=False).status_code==200:
                self.window2 = MainForm(self)
                self.window2.show()
            else:
                QMessageBox.about(self,"Error","Could not authenticate")
    def handleRegister(self):
            self.window3 = RegisterForm(self)
            self.window3.show()

class MainForm(QtGui.QWidget, Ui_Form2):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        global creds,address
        r=req.get(address+"/send/all",auth=creds,verify=False)
        ls=r.json()
        self.userBox.addItems(ls)
        self.model  = QStringListModel()
        r=req.get(address+"/receive/get/all",auth=creds,verify=False)
        self.files=r.json()
        self.model.setStringList(self.files)
        self.listView.setModel(self.model)
        self.pushButton.clicked.connect(self.openButton)
        self.sendButton.clicked.connect(self.sButton)
        self.getFile.clicked.connect(self.getfile)
        self.exiter.clicked.connect(self.end)
        self.pushButton_2.clicked.connect(self.change)
        self.delete_button.clicked.connect(self.del_file)
    def del_file(self):
        items=self.listView.selectedIndexes()
        r=req.get(address+"/receive/delete/"+str(items[0].row()+1),auth=creds,verify=False)
        r=req.get(address+"/receive/get/all",auth=creds,verify=False)
        self.files=r.json()
        self.model.setStringList(self.files)
        self.listView.setModel(self.model)
    def change(self):
        oldp=str(self.oldpassword.text())
        newp1=str(self.newpassword1.text())
        newp2=self.newpassword2.text()
        if not newp1==newp2:
            QMessageBox.about(self,"Error","Passwords don't match")
        else:
            ch=req.get(address+"/change/"+oldp+"/"+newp1,auth=creds,verify=False)
            if "changed" in ch.text:
                decrypt_file(hashlib.sha256(oldp).digest(),creds[0]+"key.enc")
                os.remove(creds[0]+"key.enc")
                encrypt_file(hashlib.sha256(newp1).digest(),creds[0]+"key")
                os.remove(creds[0]+"key")
                QMessageBox.about(self,"Info","Passwords successfully changed")
            else:
                QMessageBox.about(self,"Info","Password could not be changed")
    def end(self):
        QtCore.QCoreApplication.instance().quit()
    def openButton(self):
        self.filen=QFileDialog.getOpenFileName()
        self.Filename.setText(self.filen)
    def sButton(self):
        if self.filen:
            usern=self.userBox.currentText()
            r=req.get(address+"/send/"+usern,auth=creds,verify=False)
            key=RsaPublicKey.Read(r.json()["key"])
            data=open(self.filen,"r").read()
            aesk=AesKey.Generate()
            symencdata=aesk.Encrypt(data)
            decrypt_file(hashlib.sha256(str(creds[1])).digest(),creds[0]+"key.enc")
            privatekey=RsaPrivateKey.Read(open(str(creds[0])+"key").read())
            os.remove(creds[0]+"key")
            akey=key.Encrypt(str(aesk))
            filename =str(self.filen).split("/")[-1]
            finaldata=akey+symencdata
            files = {'file': finaldata}
            signed=privatekey.Sign(finaldata)
            signhex=binascii.hexlify(signed)
            send=req.post(address+"/send/"+usern+"/"+filename+"/"+signhex,files=files,auth=creds,verify=False)
            if send.status_code==200:
                QMessageBox.about(self,"Info","File sent successfully")
            else:
                QMessageBox.about(self,"Info","File not send")
    def getfile(self):
        items=self.listView.selectedIndexes()
        r=req.get(address+"/receive/get/"+str(items[0].row()+1),auth=creds,verify=False)
        filename=self.files[items[0].row()]
        ver=req.get(address+"/receive/verify/"+str(items[0].row()+1),auth=creds,verify=False)
        signature=binascii.unhexlify(ver.json()["sign"])
        keycall=req.get(address+"/send/"+ver.json()["user"],auth=creds,verify=False)
        key=RsaPublicKey.Read(keycall.json()["key"])
        if key.Verify(r.content,signature):
            QMessageBox.about(self,"Info","File verified to be from "+ver.json()["user"])
        else:
            QMessageBox.about(self,"Info","Verification failed")
        decrypt_file(hashlib.sha256(str(creds[1])).digest(),creds[0]+"key.enc")
        open(filename,"w").write(decrypt(r.content,creds[0]+"key"))
        QMessageBox.about(self,"Info","File written to "+filename)
        os.remove(creds[0]+"key")
        os.system("gnome-open "+filename)
class RegisterForm(QtGui.QWidget, Ui_Form3):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.RegisterButton.clicked.connect(self.register)
        self.exiter.clicked.connect(self.end)
    def register(self):
        if self.password.text()!=self.password2.text():
            QMessageBox.about(self,"Error","Passwords don't match")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", self.email.text()):
            QMessageBox.about(self,"Error","Email not valid")
        else:
            key=RsaPrivateKey.Generate()
            open(self.username.text()+"key","w").write(str(key))
            print self.username.text()
            encrypt_file(hashlib.sha256(str(self.password.text())).digest(),self.username.text()+"key")
            os.remove(self.username.text()+"key")
            data=self.username.text()+":"+self.password.text()+":"+self.email.text()+":"+str(key.public_key)
            r=req.get(self.address.text()+"/create/"+data,verify=False)
            print r.text
            if r.json().keys()[0] != "Error":
                QMessageBox.about(self,"Info","Account created")
    def end(self):
        QtCore.QCoreApplication.instance().quit()
if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec_())
