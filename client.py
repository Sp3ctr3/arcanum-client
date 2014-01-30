from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QFileDialog,QMessageBox,QStringListModel
import sys
from PyQt4.QtCore import QString
from login import Ui_Dialog as Ui_Form1
from main import Ui_Dialog as Ui_Form2 
from register import Ui_Dialog as Ui_Form3
import requests as req
from keyczar.keys import RsaPrivateKey,RsaPublicKey,AesKey
from decrypt import decrypt
fromUtf8 = QtCore.QString.fromUtf8
global creds
class LoginForm(QtGui.QWidget, Ui_Form1):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.Login.clicked.connect(self.handleButton)
        self.register_2.clicked.connect(self.handleRegister)
        self.window2 = None

    def handleButton(self):
        if self.window2 is None:
            global creds
            creds=(str(self.username.text()),str(self.password.text()))
            if req.get("http://localhost:5000/auth/",auth=creds).status_code==200:
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
        global creds
        r=req.get("http://localhost:5000/send/all",auth=creds)
        ls=r.json()
        self.userBox.addItems(ls)
        model  = QStringListModel()
        r=req.get("http://localhost:5000/receive/all",auth=creds)
        self.files=r.json()
        model.setStringList(self.files)
        self.listView.setModel(model)
        self.pushButton.clicked.connect(self.openButton)
        self.sendButton.clicked.connect(self.sButton)
        self.getFile.clicked.connect(self.getfile)
        self.exiter.clicked.connect(self.end)
    def end(self):
        QtCore.QCoreApplication.instance().quit()
    def openButton(self):
        self.filen=QFileDialog.getOpenFileName()
        self.Filename.setText(self.filen)
    def sButton(self):
        if self.filen:
            usern=self.userBox.currentText()
            r=req.get("http://localhost:5000/send/"+usern,auth=creds)
            key=RsaPublicKey.Read(r.json()["key"])
            data=open(self.filen,"r").read()
            aesk=AesKey.Generate()
            symencdata=aesk.Encrypt(data)
            akey=key.Encrypt(str(aesk))
            filename =str(self.filen).split("/")[-1]
            files = {'file': akey+symencdata}
            req.post("http://localhost:5000/send/"+usern+"/"+filename,files=files,auth=creds)
    def getfile(self):
        items=self.listView.selectedIndexes()
        r=req.get("http://localhost:5000/receive/"+str(items[0].row()+1),auth=creds)
        filename=self.files[items[0].row()]
        open(filename,"w").write(decrypt(r.content,creds[0]+"key"))
        QMessageBox.about(self,"Info","File written to "+filename)
class RegisterForm(QtGui.QWidget, Ui_Form3):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.RegisterButton.clicked.connect(self.register)
        self.exiter.clicked.connect(self.end)
    def register(self):
        if self.password.text()!=self.password2.text():
            QMessageBox.about(self,"Error","Passwords don't match")
        else:
            key=RsaPrivateKey.Generate()
            open(self.username.text()+"key","w").write(str(key))
            data=self.username.text()+":"+self.password.text()+":"+self.email.text()+":"+str(key.public_key)
            r=req.get("http://localhost:5000/create/"+data)
            print r.text
            if r.text:
                QMessageBox.about(self,"Info","Account created")
    def end(self):
        QtCore.QCoreApplication.instance().quit()
if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec_())
