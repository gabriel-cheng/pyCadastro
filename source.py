from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastros.sql"
)

def main():
    caixaCodigo = index.txtCodigo.text() # Recebe o valor do que foi digitado na caixa de texto de "código"
    print(f"Codigo: {caixaCodigo}") # Printa o que foi recebido em caixaCodigo

    caixaDescricao = index.txtDescricao.text() # Recebe o valor do que foi digitado na caixa de texto de "descrição"
    print(f"Descricao: {caixaDescricao}")

    caixaPreco = index.txtPreco.text() # Recebe o valor do que foi digitado na caixa de texto de "Preço"
    print(f"Valor: {caixaPreco}")
    
    # Condições que verificam se o radio button foi selecionado
    # Imprime o RadioButton que foi selecionado
    if index.radioInformatica.isChecked(): 
        print("\nCategoria: Informatica")
    
    elif index.radioAlimentos.isChecked():
        print("\nCategoria: Alimentos")

    elif index.radioEletronicos.isChecked():
        print("\nCategoria: Eletronicos")
    
    else:
        print("\nNenhuma categoria selecionada")



app = QtWidgets.QApplication([]) # Objeto
index = uic.loadUi("index.ui") # Chama a tela index do aplicativo
index.btnCadastrar.clicked.connect(main) # Quando eu clicar em "cadastrar produto", ele retorma a função main

index.show()
app.exec()