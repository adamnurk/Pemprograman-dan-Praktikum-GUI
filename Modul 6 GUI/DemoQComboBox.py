import sys
from PyQt5.QtWidgets import *
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()


    def setupUi(self):
        self.resize(300, 100) # Untuk mengatur ukuran tampilan 
        self.move(300, 300) # Untuk mengatur letak tampilan
        self.setWindowTitle('Demo QComboBox') # Judul tampilan
        self.combo = QComboBox() # Membuat comboBox dengan perulangan
        for i in range(1, 11): # Looping 
            self.combo.addItem('Item ke-%d' % i) # Pada comboBox akan ditampilkan nilai yang ada pada looping
        self.getTextButton = QPushButton('Ambil Teks') # Membuat pushbutton dengan nama Ambil Teks
        layout = QVBoxLayout() 
        layout.addWidget(self.combo) 
        layout.addWidget(self.getTextButton)
        layout.addStretch()
        self.setLayout(layout)
        self.getTextButton.clicked.connect(self.getTextButtonClick) 


    # Function getTextButtonClick
    def getTextButtonClick(self):
        QMessageBox.information(self, 'Informasi',
                                'Anda memilih: ' + self.combo.currentText())


# Bagian utama untuk menjalankan program
if __name__ == '__main__':    a = QApplication(sys.argv)
form = MainForm()
form.show()
a.exec_()
