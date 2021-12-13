from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect( # Instância do MYSQL Connector
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)

def main():
    caixaCodigo = index.txtCodigo.text() # Recebe o valor do que foi digitado na caixa de texto de "código"
    print(f"Codigo: {caixaCodigo}") # Printa o que foi recebido em caixaCodigo

    caixaDescricao = index.txtDescricao.text() # Recebe o valor do que foi digitado na caixa de texto de "descrição"
    print(f"Descricao: {caixaDescricao}")

    caixaPreco = index.txtPreco.text() # Recebe o valor do que foi digitado na caixa de texto de "Preço"
    print(f"Valor: {caixaPreco}")
    

    categoria = ""
    # Condições que verificam se o radio button foi selecionado
    # Imprime o RadioButton que foi selecionado
    if index.radioInformatica.isChecked(): 
        print("\nCategoria: Informatica")
        categoria = "Informatica"

    elif index.radioAlimentos.isChecked():
        print("\nCategoria: Alimentos")
        categoria = "Alimentos"

    elif index.radioEletronicos.isChecked():
        print("\nCategoria: Eletronicos")
        categoria = "Eletronicos"
    
    else:
        print("\nNenhuma categoria selecionada")

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s, %s, %s, %s)"
    dados = (str(caixaCodigo), str(caixaDescricao), str(caixaPreco), categoria) # Desempacotamento convertendo pra string
    cursor.execute(comando_SQL, dados)
    banco.commit()


app = QtWidgets.QApplication([]) # Objeto
index = uic.loadUi("index.ui") # Chama a tela index do aplicativo
index.btnCadastrar.clicked.connect(main) # Quando eu clicar em "cadastrar produto", ele retorma a função main

index.show()
app.exec()