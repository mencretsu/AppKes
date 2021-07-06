from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import QLine, Qt
from PyQt5.QtCore import center, right
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QFont
from PIL import Image
import sys, os

from main import Main 
class Kalkulasi(QWidget):
    def __init__(self, ):
        super().__init__()
        self.setWindowTitle("KALKULASI")
        self.setGeometry(350,85,850,700)
        self.setStyleSheet("font-size:12pt; font-family:Lucida Sans")
        self.ui()
        self.show()
    def ui(self):
        self.mdesign()
        self.layouts()
    def closeEvent(self, event):
        self.mainwin=Main()
    def layouts(self):
        self.mlayout=QVBoxLayout()
        self.toplayout=QVBoxLayout()
        self.bottomlayout=QFormLayout()
        self.mlayout.addLayout(self.toplayout)
        self.mlayout.addLayout(self.bottomlayout)
        self.mlayout.addStretch()
 
        self.toplayout.addWidget(self.title)
        self.toplayout.addStretch()
        self.toplayout.setAlignment(Qt.AlignHCenter)
        self.bottomlayout.addWidget(QLabel("Tinggi badan(cm)"))
        self.bottomlayout.addRow(self.label,self.slid)
        self.bottomlayout.addWidget(QLabel("Berat Badan(kg)"))
        self.bottomlayout.addRow(self.label2, self.slid2)
        self.bottomlayout.addWidget(self.btneks)
        self.bottomlayout.addWidget(self.lblhasil)
        self.bottomlayout.addWidget(self.qmbbox)
        self.bottomlayout.setSpacing(40)
        self.setLayout(self.mlayout)
    def mdesign(self):
        self.title=QLabel("kalkulasi")
        self.title.setStyleSheet('color: green;font-size: 18pt;font-family:Lucida Sans')
        #TINGGI BADAN
        self.slid=QSlider(self)
        self.slid.setOrientation(Qt.Horizontal)
        self.slid.setRange(1,200)
        self.slid.valueChanged.connect(self.labelslid)
        #BERAT BADAN
        self.slid2=QSlider(self)
        self.slid2.setOrientation(Qt.Horizontal)
        self.slid2.setRange(1,200)
        self.slid2.valueChanged.connect(self.labelslid2)

        self.label=QLabel()
        self.label2=QLabel()

        self.qmbbox=QComboBox()
        self.qmbbox.addItems(["Detail skor","18.4 <= berat badan kurang","24.9 <= ideal","29.9 <= kelebihan berat badan","34.9 <= obesitas","39,9 <= hyper obesitas"])
        
        self.lblhasil=QLabel()
        self.btneks=QPushButton("Hitung")
        self.btneks.clicked.connect(self.hasil)

    def labelslid(self):
        self.a = str(self.slid.value())
        self.label.setText(self.a)
    def labelslid2(self):
        self.b = str(self.slid2.value())
        self.label2.setText(self.b)
    def hasil(self):
        z = self.label2.text()
        w = self.label.text()
        if (z and w!=""):
            try:
                self.z = int(self.label2.text())
                self.w = int(self.label.text())
                self.oke =self.z/((self.w/100)**2)
                self.output="Skor anda : "+str(self.oke)+"\n"
                if self.oke <= 18.4:
                    self.lblhasil.setText(self.output+"anda gizi buruk")
                elif self.oke <= 24.9:
                    self.lblhasil.setText(self.output+ "anda mantap manusia idaman ukhty")
                elif self.oke <= 29.9:
                    self.lblhasil.setText(self.output + "anda kurang diet")
                elif self.oke <= 34.9:
                    self.lblhasil.setText(self.output+"anda gk pernah diet")
                elif self.oke <=39.9:
                    self.lblhasil.setText(self.output + "anda makan 3 mie instan setiap 1 jam")
                else:
                    self.lblhasil.setText(self.output+ "anda tidak pernah berhenti makan 1 detik pun")
            except:
                QMessageBox.information(self, "Perhatian","Data tidak dapat dihitung")
        else:
            QMessageBox.warning(self, "Perhatian!","Jalankan dengan benar")

def main():
    app=QApplication(sys.argv)
    window = Kalkulasi()
    sys.exit(app.exec_())
    from main import Main
    Main.show()
    
if __name__ == '__main__':
    main()