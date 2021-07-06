import sys, os
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QLine, Qt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image

import sqlite3
con = sqlite3.connect('skuyisi.db')
cur = con.cursor()


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my project")
        self.setGeometry(350,85,850,700)
        self.ui()
        self.show()
    def ui(self):
        self.mdesign()
        self.layouts()
        self.getskuyisi()
        self.displayfirst()
    def mdesign(self):
        self.setStyleSheet("font-size:10pt; font-family:Lucida Sans; font-style:Bold; color:green")
        self.title=QLabel("MENU")
        self.icon=QLabel()
        self.icon.setPixmap(QPixmap("images/menusy.png"))
        self.employelist=QListWidget()
        self.employelist.itemClicked.connect(self.singleclick)
        self.cek=QCheckBox("pilih semua")
        self.btn = QPushButton("Kalkulasi")
        self.btnnew=QPushButton("NEW")
        self.btnupdate=QPushButton("UPDATE")
        self.btndel=QPushButton("DELETE")
        self.btnset=QPushButton("Pengaturan")
        self.btnset.setStyleSheet("border-radius:50;")
        self.btnset.setIcon(QIcon("images/menuicon.png"))
        self.btnset.clicked.connect(self.set)
        self.btnnew.clicked.connect(self.addEmployee)
        self.btndel.clicked.connect(self.delemployee)
        self.btnupdate.clicked.connect(self.updateemployee)
        self.btn.clicked.connect(self.kalkulasi)
    def layouts(self):
        self.mlayout=QVBoxLayout()
        self.toplayout=QVBoxLayout()
        self.lefttoplayout=QVBoxLayout()
        self.leftlayout=QFormLayout()
        self.bottomlayout=QVBoxLayout()
        self.righttoplayout=QVBoxLayout()
        self.rightbottomlayout=QHBoxLayout()
#       main layout
        self.bottomlayout.addLayout(self.righttoplayout)
        self.bottomlayout.addLayout(self.rightbottomlayout)
        #BaGI LaYOUT
        self.mlayout.addLayout(self.lefttoplayout)
        self.mlayout.addLayout(self.toplayout)
        self.mlayout.addLayout(self.leftlayout,90)
        self.mlayout.addLayout(self.bottomlayout)
        #aDD WIDGET TO RIGHT LaYOUT
        self.lefttoplayout.addWidget(self.btnset)
        self.lefttoplayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        #3##
        self.toplayout.addWidget(self.icon)
        self.toplayout.addWidget(self.title)
        self.toplayout.addStretch()
        self.toplayout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.title.setStyleSheet('color: green;font-size: 20pt;font-family:Lucida Sans')
        #bottom
        self.righttoplayout.addWidget(self.btn)
        self.righttoplayout.addWidget(self.employelist)
        self.righttoplayout.addWidget(self.cek)
        self.rightbottomlayout.addWidget(self.btnnew)
        self.rightbottomlayout.addWidget(self.btnupdate)
        self.rightbottomlayout.addWidget(self.btndel)

        self.setLayout(self.mlayout)
    def displayfirst(self):
        query = " SELECT * FROM skuyisi ORDER BY ROWID ASC LIMIT 1"
        employee = cur.execute(query).fetchone()
        img =QLabel()
        img.setPixmap(QPixmap("images/kentank.png"+employee[5]))
        name = QLabel(employee[1])
        nmbelakang=QLabel(employee[2])
        ukuran = QLabel(employee[3])
        jumlah = QLabel(employee[4])
        infoo = QLabel(employee[6])
        
        self.leftlayout.setVerticalSpacing(15)
        self.leftlayout.addRow("Nama      :", name)
        self.leftlayout.addRow("jenis :", nmbelakang)
        self.leftlayout.addRow("Ukuran         :", ukuran)
        self.leftlayout.addRow("Jumlah          :", jumlah)
        self.leftlayout.addRow("Info        :", infoo)
        self.leftlayout.addRow(img)
    def val(self):pass
    
    def singleclick(self):
        for i in reversed(range(self.leftlayout.count())):
            widget = self.leftlayout.takeAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        self.employee = self.employelist.currentItem().text()
        self.id = self.employee.split(("-"))[0]
        self.query = "SELECT * FROM skuyisi WHERE id = ?"
        self.person = cur.execute(self.query, (self.id,)).fetchone()
        img =QLabel()
        img.setPixmap(QPixmap("images/"+self.person[5]))
        name = QLabel(self.person[1])
        nmbelakang=QLabel(self.person[2])
        ukuran = QLabel(self.person[3])
        jumlah = QLabel(self.person[4])
        infoo = QLabel(self.person[6])
        self.leftlayout.setVerticalSpacing(15)
        self.leftlayout.addRow("Nama     :", name)
        self.leftlayout.addRow("Jenis    :", nmbelakang)
        self.leftlayout.addRow("Ukuran   :", ukuran)
        self.leftlayout.addRow("Jumlah   :", jumlah)
        self.leftlayout.addRow("Informasi:", infoo)
        self.leftlayout.addRow(img)
    def delemployee(self):
        if self.employelist.selectedIndexes():
            mbox = QMessageBox.question(self, "WaRNING", "apa anda ingin menghapus data?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if mbox == QMessageBox.Yes:
                try:
                    query = "DELETE FROM skuyisi WHERE id=?"
                    cur.execute(query, (self.id,))
                    con.commit() 
                    QMessageBox.information(self, "yeay","Data berhasil dihapus")
             
                    self.employelist.clear()
                    self.getskuyisi()
                except:
                    QMessageBox.information(self,"warning","Data tidak dihapus")
        else:
            QMessageBox.information(self,"perhaatian","pilih dulu data yang akan dihapus")

    def addEmployee(self):
        from addNew import addEmployee
        self.newEmployee=addEmployee()
        self.close()
    def getAll(self):
        pass

    def getskuyisi(self):
        query = "SELECT id, nama, ukuran FROM skuyisi"
        skuyisi = cur.execute(query).fetchall()
        for skuyisi in skuyisi:
            self.employelist.addItem(str(skuyisi[0])+" - "+skuyisi[1]+" - "+skuyisi[2])
    def updateemployee(self):
        if self.employelist.selectedItems():
            person= self.employelist.currentItem().text()
            id_person = self.employee.split(("-"))[0]

            query=" SELECT * FROM skuyisi WHERE id =?"
            person=cur.execute(query, (id_person,)).fetchone()
            img="images/"+self.person[5]
            name=self.person[1]
            jeniss=self.person[2]
            ukuran=self.person[3]
            jumlah=self.person[4]
            infoo=self.person[6]

            from update import updates
            self.ubah=updates()

            self.ubah.imgadd.setPixmap(QPixmap(img))
            self.ubah.namaimg.setText(self.person[5])
            self.ubah.identry.setText(id_person)
            self.ubah.nameentry.setText(name)
            self.ubah.jenisBox.setCurrentText(jeniss)
            self.ubah.ukuranentry.value()
            self.ubah.jumlahentry.setText(jumlah)
            self.ubah.infoeditor.setText(infoo)
            self.close()
        else:
            QMessageBox.information(self, "perhatian","Pilih dulu data yang akan di update")

    def set(self):
        from setting import Setng
        self.oke=Setng()
        self.close()
    def kalkulasi(self):
        from kalkulasi import Kalkulasi
        self.gas=Kalkulasi()
        self.close()

def main():
    app=QApplication(sys.argv)
    window=Main()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()