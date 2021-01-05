# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geradorDeNumerosBingo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random

B = []
I = []
N = []
G = []
O = []
lista = [0]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.labelB = QtWidgets.QLabel(self.centralwidget)
        self.labelB.setGeometry(QtCore.QRect(60, 225, 261, 41))
        self.labelB.setFont(font)
        self.labelB.setObjectName("labelB")

        self.labelI = QtWidgets.QLabel(self.centralwidget)
        self.labelI.setGeometry(QtCore.QRect(60, 275, 261, 41))
        self.labelI.setFont(font)
        self.labelI.setObjectName("labelI")

        self.labelN = QtWidgets.QLabel(self.centralwidget)
        self.labelN.setGeometry(QtCore.QRect(60, 325, 261, 41))
        self.labelN.setFont(font)
        self.labelN.setObjectName("labelN")
        
        self.labelG = QtWidgets.QLabel(self.centralwidget)
        self.labelG.setGeometry(QtCore.QRect(60, 375, 261, 41))
        self.labelG.setFont(font)     
        self.labelG.setObjectName("labelG")

        self.labelO = QtWidgets.QLabel(self.centralwidget)
        self.labelO.setGeometry(QtCore.QRect(60, 425, 261, 41))
        self.labelO.setFont(font)
        self.labelO.setObjectName("labelO")

        self.btnGerarNumero = QtWidgets.QPushButton(self.centralwidget)
        self.btnGerarNumero.setGeometry(QtCore.QRect(10, 20, 291, 161))
        self.btnGerarNumero.setFont(font)
        self.btnGerarNumero.setObjectName("btnGerarNumero")

        self.labelNumeroGerado = QtWidgets.QLabel(self.centralwidget)
        self.labelNumeroGerado.setGeometry(QtCore.QRect(500, 25, 281, 161))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.listaAll = QtWidgets.QLabel(self.centralwidget)
        self.listaAll.setGeometry(QtCore.QRect(500, 150, 261, 41))
        self.listaAll.setFont(font)
        self.listaAll.setObjectName("labelLista")
        
        
        self.labelRestaNumero = QtWidgets.QLabel(self.centralwidget)
        self.labelRestaNumero.setGeometry(QtCore.QRect(500, 500, 261, 41))
        self.labelRestaNumero.setFont(font)
        self.labelRestaNumero.setObjectName("labelRestaNumero")

        
        font = QtGui.QFont()
        font.setPointSize(36)
        self.labelNumeroGerado.setFont(font)
        self.labelNumeroGerado.setObjectName("labelNumeroGerado")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnGerarNumero.clicked.connect(self.geraNumero)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sorteador de numeros - BINGO"))
        self.labelB.setText(_translate("MainWindow", "Numeros de B"))
        self.labelI.setText(_translate("MainWindow", "Numeros de I"))
        self.labelN.setText(_translate("MainWindow", "Numeros de N"))
        self.labelG.setText(_translate("MainWindow", "Numeros de G"))
        self.labelO.setText(_translate("MainWindow", "Numeros de O"))

        self.listaAll.setText(_translate("MainWindow", "ultimo numero"))
        
        self.btnGerarNumero.setText(_translate("MainWindow", "Gerar numero"))
        self.labelNumeroGerado.setText(_translate("MainWindow", "0"))
        self.labelRestaNumero.setText(_translate("MainWindow", "Resta: 75 numeros"))

    def geraNumero(self):
        # print('ta aqui')
        self.sortearLetra()
        # print('-------------------------------------------------')
        # self.labelB.set
        self.labelB.setText('B: ' + str(B))
        self.labelB.adjustSize()
        # print(f'B: {B}')

        self.labelI.setText('I:  ' + str(I))
        self.labelI.adjustSize()

        # print(f'I: {I}')

        self.labelN.setText('N: ' + str(N))
        self.labelN.adjustSize()

        # print(f'N: {N}')

        self.labelG.setText('G: ' + str(G))
        self.labelG.adjustSize()

        # print(f'G: {G}')

        self.labelO.setText('O: ' + str(O))
        self.labelO.adjustSize()

        self.listaAll.setText(str(lista[-2]))
        self.listaAll.adjustSize()

        # print(f'O: {O}')

        # print('-------------------------------------------------')

    def __init__(self):
        self.sorteadoBnumero = 0
        self.sorteadoInumero = 0
        self.sorteadoNnumero = 0
        self.sorteadoGnumero = 0
        self.sorteadoOnumero = 0
        self.listOfBingo = [1,2,3,4,5]
        self.restaNumerosBingo = 0

    def sortearLetra(self):
        BINGO = random.choice(self.listOfBingo)

        if BINGO == 1:
            if self.sorteadoBnumero <= 14:
                self.sorteadoBnumero +=1 
                # print('sorteado G ',self.sorteadoBnumero)
                if self.sorteadoBnumero == 15:
                    # print('retirando B no 15')
                    self.listOfBingo.remove(1)
                self.BdeBingo()
            else:
                self.listOfBingo.remove(1)
                # print(self.listOfBingo)
                # print("sortenado novamente O")

                self.sortearLetra
                

        if BINGO == 2:
            if self.sorteadoInumero <= 14:
                self.sorteadoInumero +=1 
                # print('sorteado I',self.sorteadoInumero)
                if self.sorteadoInumero == 15:
                    # print('retirando I no 15')
                    self.listOfBingo.remove(2)
                self.IdeBingo()
    

            else:

                self.listOfBingo.remove(2)
                # print(self.listOfBingo)

                # print("sortenado novamente I")
                self.sortearLetra

        if BINGO == 3:
            if self.sorteadoNnumero <= 14:
                self.sorteadoNnumero +=1 
                # print('sorteadoN',self.sorteadoNnumero)
                if self.sorteadoNnumero == 15:
                    # print('retirando N no 15')
                    self.listOfBingo.remove(3)
                self.NdeBingo()
            else:
                self.listOfBingo.remove(3)
                # print(self.listOfBingo)

                # print("sortenado novamente N")

                self.sortearLetra

        if BINGO == 4:
            if self.sorteadoGnumero <= 14:
                self.sorteadoGnumero +=1 
                # print('sorteado G',self.sorteadoGnumero)
                if self.sorteadoGnumero == 15:
                    # print('retirando G no 15')
                    self.listOfBingo.remove(4)
                self.GdeBingo()
            else:
                self.listOfBingo.remove(4)
                # print(self.listOfBingo)

                # print("sortenado novamente G")

                self.sortearLetra

        if BINGO == 5:
            if self.sorteadoOnumero <= 14:
                self.sorteadoOnumero +=1 
                # print('sorteado O',self.sorteadoOnumero)
                self.OdeBingo()
                if self.sorteadoOnumero == 15:
                    # print('retirando O no 15')
                    self.listOfBingo.remove(5)
            else:
                self.listOfBingo.remove(5)
                # print(self.listOfBingo)

                # print("sortenado novamente O")

                self.sortearLetra


    def BdeBingo(self):
        if len(B) == 15:
            self.sortearLetra
        else:
            Bingo = random.randint(1, 15)
            if Bingo not in B:
                B.append(Bingo)
                lista.append(Bingo)
                # print(f'B: {Bingo}')
                self.labelNumeroGerado.setText('B: ' + str(Bingo))

                self.restaNumerosBingo+=1
                self.labelRestaNumero.setText('Resta: ' + str(75 - self.restaNumerosBingo) + ' numeros')

            else:
                self.BdeBingo()
            B.sort()



    def IdeBingo(self):
        if len(I) == 15:
            self.sortearLetra
        else:
            Bingo = random.randint(16, 30)
            if Bingo not in I:
                I.append(Bingo)
                lista.append(Bingo)
                # print(f'I: {Bingo}')
                self.labelNumeroGerado.setText('I: ' + str(Bingo))

                self.restaNumerosBingo+=1
                self.labelRestaNumero.setText('Resta: ' + str(75 - self.restaNumerosBingo) + ' numeros')
            else:
                self.IdeBingo()
            I.sort()



    def NdeBingo(self):
        if len(N) == 15:
            self.sortearLetra
        else:
            Bingo = random.randint(31, 45)
            if Bingo not in N:
                N.append(Bingo)
                lista.append(Bingo)
                # print(f'N: {Bingo}')
                self.labelNumeroGerado.setText('N: ' + str(Bingo))

                self.restaNumerosBingo+=1
                self.labelRestaNumero.setText('Resta: ' + str(75 - self.restaNumerosBingo) + ' numeros')
            else:
                self.NdeBingo()
            N.sort()


    def GdeBingo(self):
        if len(G) == 15:
            self.sortearLetra
        else:
            Bingo = random.randint(46, 60)
            if Bingo not in G:
                G.append(Bingo)
                lista.append(Bingo)
                # print(f'G: {Bingo}')

                self.labelNumeroGerado.setText('G: ' + str(Bingo))

                self.restaNumerosBingo+=1
                self.labelRestaNumero.setText('Resta: ' + str(75 - self.restaNumerosBingo) + ' numeros')
            else:
                self.GdeBingo()
            G.sort()


    def OdeBingo(self):
        if len(O) == 15:
            self.sortearLetra
        else:
            Bingo = random.randint(61, 75)
            if Bingo not in O:
                O.append(Bingo)
                lista.append(Bingo)
                # print(f'O: {Bingo}')
                self.labelNumeroGerado.setText('O: ' + str(Bingo))

                self.restaNumerosBingo+=1
                self.labelRestaNumero.setText('Resta: ' + str(75 - self.restaNumerosBingo) + ' numeros')
            else:
                self.OdeBingo()
            O.sort()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
