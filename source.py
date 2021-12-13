from PyQt5 import uic,QtWidgets

def main():
    print("Teste")


app = QtWidgets.QApplication([])
index = uic.loadUi("index.ui")
index.pushButton.Clicked.connect(main)

index.show()
app.exec()