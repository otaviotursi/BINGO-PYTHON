# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geradorDeNumerosBingo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.MainWindow = MainWindow
        font = QtGui.QFont()
        font.setPointSize(20)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.labelB = QtWidgets.QLabel(self.centralwidget)
        self.labelB.setGeometry(QtCore.QRect(60, 350, 261, 41))
        self.labelB.setFont(font)
        self.labelB.setObjectName("labelB")

        self.labelI = QtWidgets.QLabel(self.centralwidget)
        self.labelI.setGeometry(QtCore.QRect(60, 400, 261, 41))
        self.labelI.setFont(font)
        self.labelI.setObjectName("labelI")

        self.labelN = QtWidgets.QLabel(self.centralwidget)
        self.labelN.setGeometry(QtCore.QRect(60, 450, 261, 41))
        self.labelN.setFont(font)
        self.labelN.setObjectName("labelN")
        
        self.labelG = QtWidgets.QLabel(self.centralwidget)
        self.labelG.setGeometry(QtCore.QRect(60, 500, 261, 41))
        self.labelG.setFont(font)     
        self.labelG.setObjectName("labelG")

        self.labelO = QtWidgets.QLabel(self.centralwidget)
        self.labelO.setGeometry(QtCore.QRect(60, 550, 261, 41))
        self.labelO.setFont(font)
        self.labelO.setObjectName("labelO")

        self.btnGerarNumero = QtWidgets.QPushButton(self.centralwidget)
        self.btnGerarNumero.setGeometry(QtCore.QRect(60, 20, 291, 161))
        self.btnGerarNumero.setFont(font)
        self.btnGerarNumero.setObjectName("btnGerarNumero")

        self.labelNumeroGerado = QtWidgets.QLabel(self.centralwidget)
        self.labelNumeroGerado.setGeometry(QtCore.QRect(650, 25, 300, 161))

        font = QtGui.QFont()
        font.setPointSize(23)

        self.listaAll = QtWidgets.QLabel(self.centralwidget)
        self.listaAll.setGeometry(QtCore.QRect(650, 200, 300, 50))
        self.listaAll.setFont(font)
        self.listaAll.setObjectName("labelLista")
        
        
        self.labelRestaNumero = QtWidgets.QLabel(self.centralwidget)
        self.labelRestaNumero.setGeometry(QtCore.QRect(350, 700, 350, 41))
        self.labelRestaNumero.setFont(font)
        self.labelRestaNumero.setObjectName("labelRestaNumero")

        
        font = QtGui.QFont()
        font.setPointSize(72)
        self.labelNumeroGerado.setFont(font)
        self.labelNumeroGerado.setObjectName("labelNumeroGerado")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sorteador de números - BINGO"))
        self.labelB.setText(_translate("MainWindow", "Números de B"))
        self.labelI.setText(_translate("MainWindow", "Números de I"))
        self.labelN.setText(_translate("MainWindow", "Números de N"))
        self.labelG.setText(_translate("MainWindow", "Números de G"))
        self.labelO.setText(_translate("MainWindow", "Números de O"))

        self.listaAll.setText(_translate("MainWindow", "último número"))
        
        self.btnGerarNumero.setText(_translate("MainWindow", "Gerar número"))
        self.labelNumeroGerado.setText(_translate("MainWindow", "0"))
        self.labelRestaNumero.setText(_translate("MainWindow", "Resta: 75 números"))

        # paramentros iniciais, as listas estão aqui para conseguirmos removers os indices, conforme for preciso.
        self.listOfBingo = ['B','I','N','G','O']

        self.sorteadoNumeroB = []
        self.listaB = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.sorteadoNumeroI = []
        self.listaI = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.sorteadoNumeroN = []
        self.listaN = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
        self.sorteadoNumeroG = []
        self.listaG = [46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
        self.sorteadoNumeroO = []
        self.listaO = [61,62,63,64,65,66,67,68,69,70,71,72,73,74,75]
        
        self.listaSorteados = [0]
        self.btnGerarNumero.clicked.connect(self.geraNumero)

    def geraNumero(self):
        # vai chamar a funcao de sortear o numero e atualizar o texto na GUI 
        self.sortearLetra()
        self.labelB.setText('B: ' + str(self.sorteadoNumeroB))
        self.labelB.adjustSize()

        self.labelI.setText('I:  ' + str(self.sorteadoNumeroI))
        self.labelI.adjustSize()

        self.labelN.setText('N: ' + str(self.sorteadoNumeroN))
        self.labelN.adjustSize()

        self.labelG.setText('G: ' + str(self.sorteadoNumeroG))
        self.labelG.adjustSize()

        self.labelO.setText('O: ' + str(self.sorteadoNumeroO))
        self.labelO.adjustSize()

        self.listaAll.setText(str(self.listaSorteados[-2]))
        self.listaAll.adjustSize()

        self.labelRestaNumero.setText(f'Resta: {str(76 - len(self.listaSorteados))} números')

    def sortearLetra(self):
        BINGO = None

        # vamos sortear uma letra do BINGO

        if len(self.listOfBingo) > 0:
            BINGO = random.choice(self.listOfBingo)

        #chamando a funcao que vai escolher o numero 
        if BINGO == 'B':

            self.sortearLetraB()
    
        elif BINGO == 'I':
            
            self.sortearLetraI()
    
        elif BINGO == 'N':
            
            self.sortearLetraN()
        
        elif BINGO == 'G':
            
            self.sortearLetraG()

        elif BINGO == 'O':
            
            self.sortearLetraO()

        else:
            QtWidgets.QMessageBox.about(self.MainWindow, "ATENÇÃO!", "Todos os números ja foram sorteados!\n\nFeche abra novamente o programa para gerar outro bingo.")
        
    def sortearLetraB(self):
        # aqui vamos usar uma lista com o random.choice para conseguir remover o numero, se usarmos o random.randint, não teremos essa possibilidade. 
        numero = random.choice(self.listaB)
        self.listaB.remove(numero)
        self.labelNumeroGerado.setText('B: ' + str(numero))

        # armazenando e ordenando o numero sorteado do tipo 'B', para colocar na GUI posteriormente.
        self.sorteadoNumeroB.append(numero)
        self.sorteadoNumeroB.sort()

        # coloca todos os numeros sorteados nessa lista, depois vamos analisar quantos numeros restam para sortear
        self.listaSorteados.append(numero)

        # se nao tiver nenhum numero na lista de numeros de sorteio, vai remover a possibilidade de sortear a letra 'B'
        if len(self.listaB) <= 0:
            self.listOfBingo.remove('B')

    def sortearLetraI(self):
        # aqui vamos usar uma lista com o random.choice para conseguir remover o numero, se usarmos o random.randint, não teremos essa possibilidade. 
        numero = random.choice(self.listaI)
        self.listaI.remove(numero)
        self.labelNumeroGerado.setText('I: ' + str(numero))

        # armazenando e ordenando o numero sorteado do tipo 'I', para colocar na GUI posteriormente.
        self.sorteadoNumeroI.append(numero)
        self.sorteadoNumeroI.sort()

        # coloca todos os numeros sorteados nessa lista, depois vamos analisar quantos numeros restam para sortear
        self.listaSorteados.append(numero)

        # se nao tiver nenhum numero na lista de numeros de sorteio, vai remover a possibilidade de sortear a letra 'I'
        if len(self.listaI) <= 0:
            self.listOfBingo.remove('I')
    
    def sortearLetraN(self):
        # aqui vamos usar uma lista com o random.choice para conseguir remover o numero, se usarmos o random.randint, não teremos essa possibilidade. 
        numero = random.choice(self.listaN)
        self.listaN.remove(numero)
        self.labelNumeroGerado.setText('N: ' + str(numero))

        # armazenando e ordenando o numero sorteado do tipo 'N', para colocar na GUI posteriormente.
        self.sorteadoNumeroN.append(numero)
        self.sorteadoNumeroN.sort()

        # coloca todos os numeros sorteados nessa lista, depois vamos analisar quantos numeros restam para sortear
        self.listaSorteados.append(numero)

        # se nao tiver nenhum numero na lista de numeros de sorteio, vai remover a possibilidade de sortear a letra 'N'
        if len(self.listaN) <= 0:
            self.listOfBingo.remove('N')

    def sortearLetraG(self):
        # aqui vamos usar uma lista com o random.choice para conseguir remover o numero, se usarmos o random.randint, não teremos essa possibilidade. 
        numero = random.choice(self.listaG)
        self.listaG.remove(numero)
        self.labelNumeroGerado.setText('G: ' + str(numero))

        # armazenando e ordenando o numero sorteado do tipo 'G', para colocar na GUI posteriormente.
        self.sorteadoNumeroG.append(numero)
        self.sorteadoNumeroG.sort()
        
        # coloca todos os numeros sorteados nessa lista, depois vamos analisar quantos numeros restam para sortear
        self.listaSorteados.append(numero)

        # se nao tiver nenhum numero na lista de numeros de sorteio, vai remover a possibilidade de sortear a letra 'G'
        if len(self.listaG) <= 0:
            self.listOfBingo.remove('G')

    def sortearLetraO(self):
        # aqui vamos usar uma lista com o random.choice para conseguir remover o numero, se usarmos o random.randint, não teremos essa possibilidade. 
        numero = random.choice(self.listaO)
        self.listaO.remove(numero)
        self.labelNumeroGerado.setText('O: ' + str(numero))

        # armazenando e ordenando o numero sorteado do tipo 'O', para colocar na GUI posteriormente.
        self.sorteadoNumeroO.append(numero)
        self.sorteadoNumeroO.sort()
        
        # coloca todos os numeros sorteados nessa lista, depois vamos analisar quantos numeros restam para sortear
        self.listaSorteados.append(numero)

        # se nao tiver nenhum numero na lista de numeros de sorteio, vai remover a possibilidade de sortear a letra 'O'
        if len(self.listaO) <= 0:
            self.listOfBingo.remove('O')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

