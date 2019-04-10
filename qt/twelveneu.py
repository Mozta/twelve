# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'twelve.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

#My imports
import petl as etl
import psycopg2
import datetime
import time
from datetime import date
import serial
arduino = serial.Serial('/dev/ttyUSB0',9600)
print("starting!")

# Variables globales
connection = psycopg2.connect('dbname=twelveBD user=postgres password=admin')
table_personas = etl.fromdb(connection, 'SELECT * FROM personas')

#indice para recorrrer la lista de empresas
iEmpresa = 0
iTipos = 0

#Obtener empresa seleccionada para los registros de pruebas
midEmpresa = 1
#Obtener tipo de prueba seleccionada para los registros de pruebas
midTipo = 1
midPersona = 1

noFichas = 0
mPiezasCorrectas = 0
mPiezasIncorrectas = 0
tiempoPrueba = 0
tiempoTerminado = False #Bandera para determinar el fin de la prueba
milista = [0,0,0,0,0]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showMaximized()
        #MainWindow.resize(1280, 800)
        
        MainWindow.setStyleSheet("#centralwidget \n"
"{\n"
"    background: #D9DFE8;\n"
"}\n"
"QToolBar{\n"
"    background: rgba(255, 255, 255, 100); \n"
"}\n"
"QStatusBar{\n"
"    background: rgba(255, 255, 255, 100); \n"
"}\n"
"#page_bienvenida{\n"
"background-image: url(:/ASSETS/fondo_home.jpg);\n"
"}\n"
"#page_registro{\n"
"background-image: url(:/ASSETS/fondo.jpg);\n"
"}\n"
"#page_resultados{\n"
"background-image: url(:/ASSETS/fondo.jpg);\n"
"}\n"
"QPushButton\n"
"{\n"
"  color: white;\n"
"  font: 57 14pt \"Exo\";\n"
"  border: 0px;\n"
"  padding: 0 8px;\n"
"  border-radius: 18px;\n"
"  background: #243046;\n"
"  height: 41px;\n"
"}\n"
"\n"
"QPushButton#btnPrueba\n"
"{\n"
"    background: #D9DFE8;    \n"
"    background-image: url(:/ASSETS/prueba.png);\n"
"}\n"
"QPushButton#btnHistorial\n"
"{\n"
"    background: #D9DFE8;    \n"
"    background-image: url(:/ASSETS/historial.png);\n"
"}\n"
"\n"
"QPushButton#pushButton_3\n"
"{\n"
"  border: 2px solid gray;\n"
"  border-radius: 10px;\n"
"  padding: 0 8px;\n"
"  background: yellow;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"  font: 57 14pt \"Exo\";\n"
"  border: 2px solid silver;\n"
"  padding: 5px 8px 5px 8px;\n"
"  border-radius: 10px;\n"
"  background: #fff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1280, 714))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(40)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_bienvenida = QtWidgets.QWidget()
        self.page_bienvenida.setObjectName("page_bienvenida")
        self.img_logo = QtWidgets.QLabel(self.page_bienvenida)
        self.img_logo.setGeometry(QtCore.QRect(150, 150, 311, 411))
        self.img_logo.setText("")
        self.img_logo.setPixmap(QtGui.QPixmap("ASSETS/logo.png"))
        self.img_logo.setScaledContents(True)
        self.img_logo.setObjectName("img_logo")
        self.btnHistorial = QtWidgets.QPushButton(self.page_bienvenida)
        self.btnHistorial.setEnabled(True)
        self.btnHistorial.setGeometry(QtCore.QRect(890, 400, 269, 87))
        self.btnHistorial.setText("")
        self.btnHistorial.setObjectName("btnHistorial")
        self.btnPrueba = QtWidgets.QPushButton(self.page_bienvenida)
        self.btnPrueba.setGeometry(QtCore.QRect(890, 290, 269, 87))
        self.btnPrueba.setText("")
        self.btnPrueba.setObjectName("btnPrueba")

        ## SECCION BIENVENIDA O PAGINA INICIAL
        self.stackedWidget.addWidget(self.page_bienvenida)
        self.page_registro = QtWidgets.QWidget()
        self.page_registro.setObjectName("page_registro")
        self.txtNombre = QtWidgets.QTextEdit(self.page_registro)
        self.txtNombre.setGeometry(QtCore.QRect(270, 240, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.txtNombre.setFont(font)
        self.txtNombre.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.txtNombre.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtNombre.setObjectName("txtNombre")
        self.btnRegistrar = QtWidgets.QPushButton(self.page_registro)
        self.btnRegistrar.setGeometry(QtCore.QRect(1040, 580, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.label = QtWidgets.QLabel(self.page_registro)
        self.label.setGeometry(QtCore.QRect(160, 250, 120, 21))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(238, 238, 236);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_registro)
        self.label_2.setGeometry(QtCore.QRect(190, 330, 63, 20))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_registro)
        self.label_3.setGeometry(QtCore.QRect(190, 410, 63, 20))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_3.setObjectName("label_3")
        self.spinBoxEdad = QtWidgets.QSpinBox(self.page_registro)
        self.spinBoxEdad.setGeometry(QtCore.QRect(270, 400, 131, 36))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        self.spinBoxEdad.setFont(font)
        self.spinBoxEdad.setObjectName("spinBoxEdad")
        self.comboBoxSexo = QtWidgets.QComboBox(self.page_registro)
        self.comboBoxSexo.setGeometry(QtCore.QRect(270, 320, 201, 36))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        self.comboBoxSexo.setFont(font)
        self.comboBoxSexo.setObjectName("comboBoxSexo")
        self.comboBoxSexo.addItem("")
        self.comboBoxSexo.addItem("")
        self.loguito = QtWidgets.QLabel(self.page_registro)
        self.loguito.setGeometry(QtCore.QRect(30, 634, 45, 41))
        self.loguito.setText("")
        self.loguito.setPixmap(QtGui.QPixmap(":/ASSETS/logo_icono.png"))
        self.loguito.setScaledContents(True)
        self.loguito.setObjectName("loguito")

        ## SECCION DE REGISTRO DE EMPRESA
        self.stackedWidget.addWidget(self.page_registro)
        self.page_seleccion = QtWidgets.QWidget()
        self.page_seleccion.setObjectName("page_seleccion")
        
        self.btnAddPreset = QtWidgets.QPushButton(self.page_seleccion)
        self.btnAddPreset.setGeometry(QtCore.QRect(570, 600, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.btnAddPreset.setFont(font)
        self.btnAddPreset.setObjectName("btnAddPreset")
        
        self.label_5 = QtWidgets.QLabel(self.page_seleccion)
        self.label_5.setGeometry(QtCore.QRect(990, 120, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.spinBox_2 = QtWidgets.QSpinBox(self.page_seleccion)
        self.spinBox_2.setGeometry(QtCore.QRect(990, 150, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setObjectName("spinBox_2")
        
        self.timeEdit = QtWidgets.QTimeEdit(self.page_seleccion)
        self.timeEdit.setGeometry(QtCore.QRect(990, 290, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        
        self.label_6 = QtWidgets.QLabel(self.page_seleccion)
        self.label_6.setGeometry(QtCore.QRect(990, 260, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.btnRun = QtWidgets.QPushButton(self.page_seleccion)
        self.btnRun.setGeometry(QtCore.QRect(960, 600, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.btnRun.setFont(font)
        self.btnRun.setStyleSheet("background-color: #00D5A8;")
        self.btnRun.setObjectName("btnRun")
        
        self.comboBtnFicha1 = QtWidgets.QComboBox(self.page_seleccion)
        self.comboBtnFicha1.setGeometry(QtCore.QRect(570, 170, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        self.comboBtnFicha1.setFont(font)
        self.comboBtnFicha1.setObjectName("comboBtnFicha1")
        self.comboBtnFicha1.addItem("")
        self.comboBtnFicha1.addItem("")
        self.comboBtnFicha1.addItem("")
        
        self.comboBtnFicha2 = QtWidgets.QComboBox(self.page_seleccion)
        self.comboBtnFicha2.setGeometry(QtCore.QRect(570, 270, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        self.comboBtnFicha2.setFont(font)
        self.comboBtnFicha2.setObjectName("comboBtnFicha2")
        self.comboBtnFicha2.addItem("")
        self.comboBtnFicha2.addItem("")
        self.comboBtnFicha2.addItem("")
        self.comboBtnFicha3 = QtWidgets.QComboBox(self.page_seleccion)
        self.comboBtnFicha3.setGeometry(QtCore.QRect(570, 370, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        self.comboBtnFicha3.setFont(font)
        self.comboBtnFicha3.setObjectName("comboBtnFicha3")
        self.comboBtnFicha3.addItem("")
        self.comboBtnFicha3.addItem("")
        self.comboBtnFicha3.addItem("")
        
        self.btnSeleccionarTipo = QtWidgets.QPushButton(self.page_seleccion)
        self.btnSeleccionarTipo.setGeometry(QtCore.QRect(150, 600, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.btnSeleccionarTipo.setFont(font)
        self.btnSeleccionarTipo.setObjectName("btnSeleccionarTipo")
        
        self.listWidgetPresets = QtWidgets.QListWidget(self.page_seleccion)
        self.listWidgetPresets.setGeometry(QtCore.QRect(120, 80, 291, 431))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        self.listWidgetPresets.setFont(font)
        self.listWidgetPresets.setStyleSheet("border: 2px solid silver;\n"
"  padding: 5px 8px 5px 8px;\n"
"  border-radius: 10px;\n"
"  background: #fff;")
        self.listWidgetPresets.setObjectName("listWidgetPresets")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetPresets.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetPresets.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetPresets.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetPresets.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetPresets.addItem(item)
        
        self.label_10 = QtWidgets.QLabel(self.page_seleccion)
        self.label_10.setGeometry(QtCore.QRect(140, 50, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        
        self.loguito_2 = QtWidgets.QLabel(self.page_seleccion)
        self.loguito_2.setGeometry(QtCore.QRect(30, 634, 45, 41))
        self.loguito_2.setText("")
        self.loguito_2.setPixmap(QtGui.QPixmap(":/ASSETS/logo_icono.png"))
        self.loguito_2.setScaledContents(True)
        self.loguito_2.setObjectName("loguito_2")

        self.speedBox = QtWidgets.QSpinBox(self.page_seleccion)
        self.speedBox.setGeometry(QtCore.QRect(990, 430, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        self.speedBox.setFont(font)
        self.speedBox.setObjectName("speedBox")
        
        self.label_12 = QtWidgets.QLabel(self.page_seleccion)
        self.label_12.setGeometry(QtCore.QRect(990, 400, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        
        self.stackedWidget.addWidget(self.page_seleccion)
        ## SECCION DE SELECCION DE PRUEBA

        self.page_ejecucion = QtWidgets.QWidget()
        self.page_ejecucion.setObjectName("page_ejecucion")
        self.imgFicha1 = QtWidgets.QLabel(self.page_ejecucion)
        self.imgFicha1.setGeometry(QtCore.QRect(180, 80, 140, 161))
        self.imgFicha1.setText("")
        self.imgFicha1.setPixmap(QtGui.QPixmap("images/btnred.png"))
        self.imgFicha1.setScaledContents(True)
        self.imgFicha1.setObjectName("imgFicha1")
        self.imgFicha2 = QtWidgets.QLabel(self.page_ejecucion)
        self.imgFicha2.setGeometry(QtCore.QRect(180, 260, 140, 161))
        self.imgFicha2.setText("")
        self.imgFicha2.setPixmap(QtGui.QPixmap("images/btnblue.png"))
        self.imgFicha2.setScaledContents(True)
        self.imgFicha2.setObjectName("imgFicha2")
        self.imgFicha3 = QtWidgets.QLabel(self.page_ejecucion)
        self.imgFicha3.setGeometry(QtCore.QRect(180, 440, 140, 161))
        self.imgFicha3.setText("")
        self.imgFicha3.setPixmap(QtGui.QPixmap("images/btnyellow.png"))
        self.imgFicha3.setScaledContents(True)
        self.imgFicha3.setObjectName("imgFicha3")
        self.btnStop = QtWidgets.QPushButton(self.page_ejecucion)
        self.btnStop.setGeometry(QtCore.QRect(1060, 600, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.btnStop.setFont(font)
        self.btnStop.setStyleSheet("background-color: #00D5A8;")
        self.btnStop.setObjectName("btnStop")
        self.btnStart = QtWidgets.QPushButton(self.page_ejecucion)
        self.btnStart.setGeometry(QtCore.QRect(650, 380, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnStart.setFont(font)
        self.btnStart.setStyleSheet("font: \"Exo\";")
        self.btnStart.setObjectName("btnStart")
        
        
        self.lblTiempo = QtWidgets.QLabel(self.page_ejecucion)
        self.lblTiempo.setGeometry(QtCore.QRect(510, 130, 541, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTiempo.sizePolicy().hasHeightForWidth())
        self.lblTiempo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(107)
        font.setBold(False)
        font.setWeight(50)
        self.lblTiempo.setFont(font)
        self.lblTiempo.setStyleSheet("border: 2px solid silver;\n"
"  border-radius: 20px;\n"
"  background: #fff;")
        self.lblTiempo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTiempo.setWordWrap(False)
        self.lblTiempo.setObjectName("lblTiempo")
        self.loguito_3 = QtWidgets.QLabel(self.page_ejecucion)
        self.loguito_3.setGeometry(QtCore.QRect(30, 634, 45, 41))
        self.loguito_3.setText("")
        self.loguito_3.setPixmap(QtGui.QPixmap(":/ASSETS/logo_icono.png"))
        self.loguito_3.setScaledContents(True)
        self.loguito_3.setObjectName("loguito_3")
        self.stackedWidget.addWidget(self.page_ejecucion)

        ##SECCION DE RESULTADOS
        self.page_resultados = QtWidgets.QWidget()
        self.page_resultados.setObjectName("page_resultados")
        self.label_14 = QtWidgets.QLabel(self.page_resultados)
        self.label_14.setGeometry(QtCore.QRect(260, 40, 400, 61))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(32)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_resultados)
        self.label_15.setGeometry(QtCore.QRect(210, 270, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.page_resultados)
        self.label_16.setGeometry(QtCore.QRect(200, 460, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_16.setObjectName("label_16")
        self.lcdNumberWin = QtWidgets.QLCDNumber(self.page_resultados)
        self.lcdNumberWin.setGeometry(QtCore.QRect(530, 220, 300, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lcdNumberWin.setFont(font)
        self.lcdNumberWin.setStyleSheet("border: 2px solid silver;\n"
"  border-radius: 20px;\n"
"  background: #fff;")
        self.lcdNumberWin.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumberWin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberWin.setSmallDecimalPoint(False)
        self.lcdNumberWin.setDigitCount(2)
        self.lcdNumberWin.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumberWin.setProperty("intValue", 25)
        self.lcdNumberWin.setObjectName("lcdNumberWin")
        self.lcdNumberFail = QtWidgets.QLCDNumber(self.page_resultados)
        self.lcdNumberFail.setGeometry(QtCore.QRect(530, 410, 300, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lcdNumberFail.setFont(font)
        self.lcdNumberFail.setStyleSheet("border: 2px solid silver;\n"
"  border-radius: 20px;\n"
"  background: #fff;")
        self.lcdNumberFail.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumberFail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberFail.setSmallDecimalPoint(False)
        self.lcdNumberFail.setDigitCount(2)
        self.lcdNumberFail.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumberFail.setProperty("intValue", 5)
        self.lcdNumberFail.setObjectName("lcdNumberFail")
        self.btnReinicio = QtWidgets.QPushButton(self.page_resultados)
        self.btnReinicio.setGeometry(QtCore.QRect(1050, 500, 200, 41))
        self.btnReinicio.setObjectName("btnReinicio")
        self.btnFinalizar = QtWidgets.QPushButton(self.page_resultados)
        self.btnFinalizar.setGeometry(QtCore.QRect(1050, 580, 200, 41))
        self.btnFinalizar.setStyleSheet("background-color: #00D5A8;")
        self.btnFinalizar.setObjectName("btnFinalizar")
        self.loguito_4 = QtWidgets.QLabel(self.page_resultados)
        self.loguito_4.setGeometry(QtCore.QRect(30, 634, 45, 41))
        self.loguito_4.setText("")
        self.loguito_4.setPixmap(QtGui.QPixmap(":/ASSETS/logo_icono.png"))
        self.loguito_4.setScaledContents(True)
        self.loguito_4.setObjectName("loguito_4")
        self.stackedWidget.addWidget(self.page_resultados)

        ## SECCION HISTORIAL
        self.page_historial = QtWidgets.QWidget()
        self.page_historial.setObjectName("page_historial")
        # self.scrollArea = QtWidgets.QScrollArea(self.page_historial)
        # self.scrollArea.setGeometry(QtCore.QRect(80, 60, 211, 211))
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 207, 207))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.listWidgetHistorial = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        # font = QtGui.QFont()
        # font.setFamily("Exo")
        # font.setPointSize(14)
        # self.listWidgetHistorial.setFont(font)
        # self.listWidgetHistorial.setObjectName("listWidgetHistorial")
        # item = QtWidgets.QListWidgetItem()
        # self.listWidgetHistorial.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidgetHistorial.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidgetHistorial.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidgetHistorial.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidgetHistorial.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidgetHistorial.addItem(item)
        # self.horizontalLayout_2.addWidget(self.listWidgetHistorial)
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btnDelete = QtWidgets.QToolButton(self.page_historial)
        self.btnDelete.setGeometry(QtCore.QRect(1090, 560, 36, 36))
        self.btnDelete.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelete.setIcon(icon)
        self.btnDelete.setObjectName("btnDelete")
        self.btnEdit = QtWidgets.QToolButton(self.page_historial)
        self.btnEdit.setGeometry(QtCore.QRect(1140, 560, 36, 36))
        self.btnEdit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEdit.setIcon(icon1)
        self.btnEdit.setObjectName("btnEdit")
        self.btnExport = QtWidgets.QToolButton(self.page_historial)
        self.btnExport.setGeometry(QtCore.QRect(1190, 560, 36, 36))
        self.btnExport.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExport.setIcon(icon2)
        self.btnExport.setObjectName("btnExport")
        self.loguito_5 = QtWidgets.QLabel(self.page_historial)
        self.loguito_5.setGeometry(QtCore.QRect(30, 634, 45, 41))
        self.loguito_5.setText("")
        self.loguito_5.setPixmap(QtGui.QPixmap(":/ASSETS/logo_icono.png"))
        self.loguito_5.setScaledContents(True)
        self.loguito_5.setObjectName("loguito_5")
        self.label_11 = QtWidgets.QLabel(self.page_historial)
        self.label_11.setGeometry(QtCore.QRect(60, 29, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.tableWidgetHistorial = QtWidgets.QTableWidget(self.page_historial)
        self.tableWidgetHistorial.setGeometry(QtCore.QRect(40, 60, 1201, 491))
        self.tableWidgetHistorial.setAutoFillBackground(True)
        self.tableWidgetHistorial.setStyleSheet(" font: 57 14pt \"Exo\";")
        self.tableWidgetHistorial.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidgetHistorial.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidgetHistorial.setRowCount(2)
        self.tableWidgetHistorial.setColumnCount(8)
        self.tableWidgetHistorial.setObjectName("tableWidgetHistorial")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetHistorial.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetHistorial.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetHistorial.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetHistorial.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetHistorial.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetHistorial.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetHistorial.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetHistorial.setHorizontalHeaderItem(7, item)
        self.tableWidgetHistorial.horizontalHeader().setDefaultSectionSize(147)
        self.stackedWidget.addWidget(self.page_historial)

        ## SECCION DE REGISTRO DE EMPRESAS
        self.page_empresas = QtWidgets.QWidget()
        self.page_empresas.setObjectName("page_empresas")
        self.txtNombreEmpresa = QtWidgets.QTextEdit(self.page_empresas)
        self.txtNombreEmpresa.setGeometry(QtCore.QRect(380, 440, 361, 41))
        self.txtNombreEmpresa.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtNombreEmpresa.setObjectName("txtNombreEmpresa")
        self.label_7 = QtWidgets.QLabel(self.page_empresas)
        self.label_7.setGeometry(QtCore.QRect(130, 450, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.btnRegistrar_2 = QtWidgets.QPushButton(self.page_empresas)
        self.btnRegistrar_2.setGeometry(QtCore.QRect(650, 650, 171, 41))
        self.btnRegistrar_2.setObjectName("btnRegistrar_2")
        self.label_8 = QtWidgets.QLabel(self.page_empresas)
        self.label_8.setGeometry(QtCore.QRect(260, 530, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txtDireccionEmpresa = QtWidgets.QTextEdit(self.page_empresas)
        self.txtDireccionEmpresa.setGeometry(QtCore.QRect(380, 520, 361, 41))
        self.txtDireccionEmpresa.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtDireccionEmpresa.setObjectName("txtDireccionEmpresa")
        self.label_9 = QtWidgets.QLabel(self.page_empresas)
        self.label_9.setGeometry(QtCore.QRect(260, 610, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.spinBoxEmpresa = QtWidgets.QSpinBox(self.page_empresas)
        self.spinBoxEmpresa.setGeometry(QtCore.QRect(380, 600, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        self.spinBoxEmpresa.setFont(font)
        self.spinBoxEmpresa.setObjectName("spinBoxEmpresa")
        self.btnGuardarEmpresa = QtWidgets.QPushButton(self.page_empresas)
        self.btnGuardarEmpresa.setGeometry(QtCore.QRect(990, 630, 221, 41))
        self.btnGuardarEmpresa.setStyleSheet("background-color: #00D5A8;")
        self.btnGuardarEmpresa.setObjectName("btnGuardarEmpresa")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_empresas)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 20, 1191, 291))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1187, 287))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.listEmpresas = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        # font = QtGui.QFont()
        # font.setFamily("Exo")
        # font.setPointSize(14)
        # self.listEmpresas.setFont(font)
        # self.listEmpresas.setObjectName("listEmpresas")
        # item = QtWidgets.QListWidgetItem()
        # self.listEmpresas.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listEmpresas.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listEmpresas.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listEmpresas.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listEmpresas.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listEmpresas.addItem(item)
        # self.horizontalLayout_3.addWidget(self.listEmpresas)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.btnSeleccionarEmpresa = QtWidgets.QPushButton(self.page_empresas)
        self.btnSeleccionarEmpresa.setGeometry(QtCore.QRect(980, 320, 231, 41))
        self.btnSeleccionarEmpresa.setObjectName("btnSeleccionarEmpresa")
        self.loguito_6 = QtWidgets.QLabel(self.page_empresas)
        self.loguito_6.setGeometry(QtCore.QRect(30, 634, 45, 41))
        self.loguito_6.setText("")
        self.loguito_6.setPixmap(QtGui.QPixmap(":/ASSETS/logo_icono.png"))
        self.loguito_6.setScaledContents(True)
        self.loguito_6.setObjectName("loguito_6")
        self.stackedWidget.addWidget(self.page_empresas)

        ##SECCION PRINCIPAL
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Exo")
        self.toolBar.setFont(font)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInicio = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInicio.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Exo")
        self.actionInicio.setFont(font)
        self.actionInicio.setObjectName("actionInicio")
        self.actionInicio.setStatusTip('Regresar a inicio')
        self.actionInicio.triggered.connect(self.menu_inicio)
        self.actionConfiguraci_n = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/conf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfiguraci_n.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Exo")
        self.actionConfiguraci_n.setFont(font)
        self.actionConfiguraci_n.setObjectName("actionConfiguraci_n")
        self.actionConfiguraci_n.setStatusTip('Configuraciones')
        self.actionConfiguraci_n.triggered.connect(self.configuraciones)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/exit24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Exo")
        self.actionSalir.setFont(font)
        self.actionSalir.setObjectName("actionSalir")
        self.actionSalir.setStatusTip('Salir de la aplicación')
        self.actionSalir.triggered.connect(self.closeEvent)
        self.toolBar.addAction(self.actionInicio)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConfiguraci_n)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSalir)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Mio
        self.btnPrueba.clicked.connect(self.prueba) #Al hacer clic en este boton mandamos a llamar a la funcion prueba
        self.btnHistorial.clicked.connect(self.historial)#Al hacer clic en este boton mandamos a llamar a la funcion historial
        self.btnRegistrar.clicked.connect(self.registrarPersona)#Al hacer clic en este boton mandamos a llamar a la funcion registrarPersona

        self.btnGuardarEmpresa.clicked.connect(self.anadirListaEmpresas)#Al hacer clic en este boton mandamos a llamar a la funcion anadirListaEmpresas
        self.btnSeleccionarEmpresa.clicked.connect(self.seleccionarEmpresa)#Al hacer clic en este boton mandamos a llamar a la funcion seleccionarEmpresa

        self.btnAddPreset.clicked.connect(self.anadirListaTipos)#Al hacer clic en este boton mandamos a llamar a la funcion anadirListaTipos
        self.btnSeleccionarTipo.clicked.connect(self.seleccionarTipo)

        self.btnRun.clicked.connect(self.mostrarPrueba)
        self.btnStart.clicked.connect(self.ejecutarPrueba)
  
        self.btnStop.clicked.connect(self.detenerPrueba)

        self.btnReinicio.clicked.connect(self.reiniciarPrueba)
        self.btnFinalizar.clicked.connect(self.finalizarPrueba)

        self.btnDelete.clicked.connect(self.borarRegistro)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Twelve Technologies"))
        self.txtNombre.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Exo\'; font-size:14pt; font-weight:56; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Cantarell\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.btnRegistrar.setText(_translate("MainWindow", "Siguiente"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.label_2.setText(_translate("MainWindow", "Sexo"))
        self.label_3.setText(_translate("MainWindow", "Edad"))
        self.comboBoxSexo.setItemText(0, _translate("MainWindow", "Masculino"))
        self.comboBoxSexo.setItemText(1, _translate("MainWindow", "Femenino"))
        self.btnAddPreset.setText(_translate("MainWindow", "Añadir prueba"))
        self.label_5.setText(_translate("MainWindow", "No. Piezas"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "mm:ss"))
        self.label_6.setText(_translate("MainWindow", "Tiempo"))
        self.btnRun.setText(_translate("MainWindow", "Ejecutar prueba"))
        self.comboBtnFicha1.setItemText(0, _translate("MainWindow", "Azul"))
        self.comboBtnFicha1.setItemText(1, _translate("MainWindow", "Rojo"))
        self.comboBtnFicha1.setItemText(2, _translate("MainWindow", "Amarillo"))
        self.comboBtnFicha2.setItemText(0, _translate("MainWindow", "Azul"))
        self.comboBtnFicha2.setItemText(1, _translate("MainWindow", "Rojo"))
        self.comboBtnFicha2.setItemText(2, _translate("MainWindow", "Amarillo"))
        self.comboBtnFicha3.setItemText(0, _translate("MainWindow", "Azul"))
        self.comboBtnFicha3.setItemText(1, _translate("MainWindow", "Rojo"))
        self.comboBtnFicha3.setItemText(2, _translate("MainWindow", "Amarillo"))
        self.btnSeleccionarTipo.setText(_translate("MainWindow", "Seleccionar prueba"))
        __sortingEnabled = self.listWidgetPresets.isSortingEnabled()
        self.listWidgetPresets.setSortingEnabled(False)

        self.listWidgetPresets.setSortingEnabled(__sortingEnabled)
        self.label_10.setText(_translate("MainWindow", "Tipo de Pruebas"))
        self.label_12.setText(_translate("MainWindow", "Velocidad"))
        self.btnStop.setText(_translate("MainWindow", "STOP"))
        self.btnStart.setText(_translate("MainWindow", "Iniciar Prueba"))

        self.lblTiempo.setText(_translate("MainWindow", "00:00"))
        self.label_14.setText(_translate("MainWindow", "Prueba finalizada"))
        self.label_15.setText(_translate("MainWindow", "Total de piezas correctas"))
        self.label_16.setText(_translate("MainWindow", "Total de piezas incorrectas"))
        self.btnReinicio.setText(_translate("MainWindow", "Reiniciar"))
        self.btnFinalizar.setText(_translate("MainWindow", "Finalizar"))
        self.label_11.setText(_translate("MainWindow", "Registros"))
        item = self.tableWidgetHistorial.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "idPrueba"))
        item = self.tableWidgetHistorial.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "idEmpresa"))
        item = self.tableWidgetHistorial.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "idPersona"))
        item = self.tableWidgetHistorial.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "idTipo"))
        item = self.tableWidgetHistorial.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.tableWidgetHistorial.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "no.Aciertos"))
        item = self.tableWidgetHistorial.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "no.Fallas"))
        item = self.tableWidgetHistorial.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "aprobado"))

        #__sortingEnabled = self.listWidgetHistorial.isSortingEnabled()
        #self.listWidgetHistorial.setSortingEnabled(False)
        # item = self.listWidgetHistorial.item(0)
        # item.setText(_translate("MainWindow", "Prueba 1"))
        # item = self.listWidgetHistorial.item(1)
        # item.setText(_translate("MainWindow", "Prueba 2"))
        # item = self.listWidgetHistorial.item(2)
        # item.setText(_translate("MainWindow", "Prueba 3"))
        # item = self.listWidgetHistorial.item(3)
        # item.setText(_translate("MainWindow", "Prueba 4"))
        # item = self.listWidgetHistorial.item(4)
        # item.setText(_translate("MainWindow", "Prueba 5"))
        # item = self.listWidgetHistorial.item(5)
        # item.setText(_translate("MainWindow", "New Item"))
        # self.listWidgetHistorial.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "Nombre de la empresa"))
        self.btnRegistrar_2.setText(_translate("MainWindow", "Siguiente"))
        self.label_8.setText(_translate("MainWindow", "Dirección"))
        self.label_9.setText(_translate("MainWindow", "Surcursal"))
        self.btnGuardarEmpresa.setText(_translate("MainWindow", "Guardar empresa"))
        # __sortingEnabled = self.listEmpresas.isSortingEnabled()
        # self.listEmpresas.setSortingEnabled(False)
        # item = self.listEmpresas.item(0)
        # item.setText(_translate("MainWindow", "Prueba 1"))
        # item = self.listEmpresas.item(1)
        # item.setText(_translate("MainWindow", "Prueba 2"))
        # item = self.listEmpresas.item(2)
        # item.setText(_translate("MainWindow", "Prueba 3"))
        # item = self.listEmpresas.item(3)
        # item.setText(_translate("MainWindow", "Prueba 4"))
        # item = self.listEmpresas.item(4)
        # item.setText(_translate("MainWindow", "Prueba 5"))
        # item = self.listEmpresas.item(5)
        # item.setText(_translate("MainWindow", "New Item"))
        # self.listEmpresas.setSortingEnabled(__sortingEnabled)
        self.btnSeleccionarEmpresa.setText(_translate("MainWindow", "Seleccionar empresa"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionInicio.setText(_translate("MainWindow", "Inicio"))
        self.actionInicio.setToolTip(_translate("MainWindow", "Regresar a inicio"))
        self.actionConfiguraci_n.setText(_translate("MainWindow", "Configuración"))
        self.actionConfiguraci_n.setToolTip(_translate("MainWindow", "Configuraciones"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setToolTip(_translate("MainWindow", "Salir de la aplicación"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+Q"))

    #Funcion para cambiar al panel inicio
    def menu_inicio(self):
        self.stackedWidget.setCurrentIndex(0)

    #Funcion para cambiar al panel registro de prueba
    def prueba(self):
        self.stackedWidget.setCurrentIndex(1)

    #Funcion para cambiar al panel registro de prueba
    def historial(self):
        self.stackedWidget.setCurrentIndex(5)
        pruebas = etl.fromdb(connection, 'SELECT * FROM pruebas')

        self.tableWidgetHistorial.setRowCount(0)

        for row_number, row_data in enumerate(pruebas.data()):
            self.tableWidgetHistorial.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidgetHistorial.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))


    #Funcion para añadir el registro de una nueva prueba (datos de la persona)
    def registrarPersona(self):
        global midPersona

        self.stackedWidget.setCurrentIndex(2)
        #print (self.txtNombre.toPlainText())
        #print (self.comboBoxSexo.currentText())
        #print (self.spinBoxEdad.value())

        #--------- BEGIN Registrar persona ------------
        if self.comboBoxSexo.currentText() == 'Masculino' :
           sexo = 'm'
        else :
           sexo = 'f'

        table1 = [['nombre','sexo','edad'],[self.txtNombre.toPlainText(),sexo,self.spinBoxEdad.value()]]
        etl.appenddb(table1, connection, 'personas')
        #--------- END Registrar persona ------------

        #Obtener datos para previo registro de la prueba que se ejecute
        midPersona = etl.fromdb(connection, "SELECT idpersona FROM personas WHERE nombre='" + self.txtNombre.toPlainText() + "'")
        midPersona = midPersona[1][0]

        self.llenarListaTipos()
        self.txtNombre.clear()
        self.spinBoxEdad.clear()
        #self.comboBoxSexo.text()
        #self.spinBoxEdad.text()

    #Funcion para cambiar al panel registro de prueba
    def mostrarPrueba(self):
        global tiempoPrueba

        milista[0]=int(self.speedBox.text()) #velocidad de giro
        milista[1]=self.comboBtnFicha3.currentIndex()+1 #ficha inferior
        milista[2]=self.comboBtnFicha2.currentIndex()+1 #ficha media
        milista[3]=self.comboBtnFicha1.currentIndex()+1 #ficha superior
        milista[4]=1
        
        self.stackedWidget.setCurrentIndex(3)

        tiempoPrueba = QtCore.QTime(0, 0, 0).secsTo(self.timeEdit.time());

        t = str(datetime.timedelta(seconds=tiempoPrueba))
        self.lblTiempo.setText(t[2:])

        #Cambiar contenido de elementos UI al tipo de prueba seleccionado
        self.cambiarFichas(milista)

        #Ocultar boton de stop
        self.btnStop.hide()

        self.btnStart.setEnabled(True)
        

    #Funcion para ejecutar prueba
    def ejecutarPrueba(self):
 
        c = 10000*milista[0]+1000*milista[1]+100*milista[2]+10*milista[3]+milista[4]
        arduino.write(str(c).encode())
        arduino.flush()
        #arduino.close()

        global tiempoPrueba

        #Seteo de elementos UI
        self.lblTiempo.setStyleSheet("color: rgb(0,0,0)")
        self.btnStop.setEnabled(True)
        self.btnStart.setEnabled(False)


        #Se establece la variable tiempoPrueba al tiempo de la prueba seleccionado de forma global
        tiempoPrueba = QtCore.QTime(0, 0, 0).secsTo(self.timeEdit.time());

        #Mostrar boton de stop
        self.btnStop.show()

        #------ BEGIN: Hilo para el contador ------------
        self.threadclass = ThreadClass()
        self.threadclass.start()
        self.threadclass.holi.connect(self.actualizarEtiquetaThread)
        #------ END: Hilo para el contador ------------

    #Funcion de paro de emergencia
    def detenerPrueba(self):
        stop="00000"
        arduino.write(stop.encode())
        #arduino.flush()
        #arduino.close()
        self.threadclass.terminate()
        #Seteo de elementos UI
        self.lblTiempo.setStyleSheet("color: rgb(255,0,0)")
        self.btnStop.setEnabled(False)
        self.btnStart.setEnabled(True)
        self.btnStart.setText("Reiniciar prueba")

    #Funcion en hilo que cambia la UI del contador y verifica cuando finaliza
    def actualizarEtiquetaThread(self,val):
        global mPiezasCorrectas
        global noFichas

        #Parseo de int a segundos en time
        t = str(datetime.timedelta(seconds=val))
        self.lblTiempo.setText(t[2:])
        self.lblTiempo.repaint()
        #Si el contador llega a 0 finaliza y cambia de panel
        if val == 0:
            time.sleep(2)

            text=arduino.read(arduino.inWaiting())
            mPiezasCorrectas=int(text)
            print(text)
            self.stackedWidget.setCurrentIndex(4)
            self.lcdNumberWin.setProperty("intValue", mPiezasCorrectas)
            self.lcdNumberFail.setProperty("intValue", noFichas - mPiezasCorrectas)

    #Funcion que actualiza el la etiqueta timer
    def actualizarEtiqueta(self,tiempoPrueba):
        #print("Dentro")
        for segundos in range(tiempoPrueba,-1,-1):
            t = str(datetime.timedelta(seconds=segundos))
            self.lblTiempo.setText(t[2:])
            self.lblTiempo.repaint()


            time.sleep(1)

    #Funcion que cambia la UI de las fichas dependiendo de la prueba seleccionada
    def cambiarFichas(self,tipo):
        self.imgFicha1.setPixmap(QtGui.QPixmap(self.ponerImagenFicha(milista[3])))
        self.imgFicha2.setPixmap(QtGui.QPixmap(self.ponerImagenFicha(milista[2])))
        self.imgFicha3.setPixmap(QtGui.QPixmap(self.ponerImagenFicha(milista[1])))

    #Funcion que devuelve la imagen de la ficha
    def ponerImagenFicha(self,img):
        if img == 2:
            return "images/btnred.png"
        elif img == 3:
            return "images/btnyellow.png"
        else:
            return "images/btnblue.png"

    #Funcion cuando finaliza la prueba
    def pruebaFinalizada(self):
        global tiempoTerminado

        while tiempoTerminado:
            self.stackedWidget.setCurrentIndex(4)
        print ("Debo cambiar")



    #Funcion para cambiar al panel registro de prueba
    def reiniciarPrueba(self):
        global mPiezasCorrectas
        global mPiezasIncorrectas

        self.guardarPrueba()

        mPiezasCorrectas = 0
        mPiezasIncorrectas = 0
        self.ejecutarPrueba()
        self.stackedWidget.setCurrentIndex(3)

    #Funcion para cambiar al panel registro de prueba
    def finalizarPrueba(self):
        global mPiezasCorrectas

        self.guardarPrueba()

        mPiezasCorrectas = 0
        mPiezasIncorrectas = 0
        self.stackedWidget.setCurrentIndex(0)

    #Funcion para guardar los resultados de la prueba ejecutada
    def guardarPrueba(self):
        global midEmpresa
        global mPiezasCorrectas
        global noFichas
        global midPersona
        global midTipo

        today = date.today()
        mPiezasIncorrectas = noFichas-mPiezasCorrectas
        if (mPiezasIncorrectas < 0):
            mPiezasIncorrectas = 0

        if (mPiezasIncorrectas == 0):
            aprobado = True
        else:
            aprobado = False

        #--------- BEGIN Registrar persona ------------
        tablePrueba = [['idempresa','idpersona','idtipos', 'fecha', 'noaciertos', 'nofallas', 'aprobado'],[midEmpresa, midPersona, midTipo, today, mPiezasCorrectas, mPiezasIncorrectas, aprobado]]
        etl.appenddb(tablePrueba, connection, 'pruebas')
        #--------- END Registrar persona ------------

    #Funcion para registrar una nueva empresa en la BD
    def anadirListaEmpresas(self):
        global iEmpresa

        table1 = [['nombre','sucursal','direccion'],[self.txtNombreEmpresa.toPlainText(),self.spinBoxEmpresa.value(),self.txtDireccionEmpresa.toPlainText()]]
        etl.appenddb(table1, connection, 'empresas')

        item = QtWidgets.QListWidgetItem()
        self.listEmpresas.addItem(item)

        item = self.listEmpresas.item(iEmpresa)
        item.setText(self.txtNombreEmpresa.toPlainText())

    #Funcion para obtener el id de la empresa configurada
    def seleccionarEmpresa(self):
        global midEmpresa
        a = self.listEmpresas.selectedIndexes()[0]
        midEmpresa = a.row() + 1
        print (midEmpresa)
        self.stackedWidget.setCurrentIndex(0)

    #Funcion para eliminar el registro seleccionado
    def borarRegistro(self):
        a = self.tableWidgetHistorial.selectedIndexes()[0]
        cell = self.tableWidgetHistorial.item(a.row(),0).text()
        print (cell)

        reply = QtWidgets.QMessageBox.question(MainWindow, 'Message',
            "Estas seguro de borrar el registro: "+cell+"?", QtWidgets.QMessageBox.Yes |
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            #Metodo para borrar un registro
            cur = connection.cursor()
            cur.execute("DELETE FROM pruebas WHERE idprueba='" + cell + "';")
            connection.commit()
            cur.close()

            #Volvemos a consultar los datos
            pruebas = etl.fromdb(connection, "SELECT * FROM pruebas")
            #Reseteamos el widget
            self.tableWidgetHistorial.setRowCount(0)
            #Rellenamos el widget con los datos de la nueva consulta
            for row_number, row_data in enumerate(pruebas.data()):
                self.tableWidgetHistorial.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidgetHistorial.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))


    #Funcion que cambia los elementos de la UI dependiendo de la prueba seleccionada en la lista
    def seleccionarTipo(self):
        global midTipo
        global noFichas
        a = self.listWidgetPresets.selectedIndexes()[0]
        midTipo = a.row()
        tipos = etl.fromdb(connection, 'SELECT * FROM tipos') #obtenemos la informacion a partir de la DB
        b = tipos.data() #guardamos esa info en una variable
        #print(b)
        #print(b[midTipo][4])
        #print(b[midTipo][5])
        #print(b[midTipo][6])
        #Cambiar contenido de elementos UI al tipo de prueba seleccionado
        self.comboBtnFicha1.setCurrentIndex(b[midTipo][4] -1) # cambiamos el indice de la ficha y restamos 1 para asegurar el 0
        self.comboBtnFicha2.setCurrentIndex(b[midTipo][5] -1) # cambiamos el indice de la ficha y restamos 1 para asegurar el 0
        self.comboBtnFicha3.setCurrentIndex(b[midTipo][6] -1) # cambiamos el indice de la ficha y restamos 1 para asegurar el 0
        self.speedBox.setValue(b[midTipo][7])
        #print(str(b[midTipo][7]))
        #temp = comando
        #arduino.write(temp.encode())
        #arduino.close()
        noFichas = b[midTipo][2] #o btenemos el valor del numero de fichas a partir de la DB
        self.spinBox_2.setValue(noFichas) # seteamos el valor de noFichas a partir de la DB    
        xTime = b[midTipo][3] # obtenemos el valor del tiempo a partir de la DB
        some_time = QtCore.QTime(0, 0, 0).addSecs(xTime); # convertirmos el valor del tiempo a un formato horario 00:00 
        self.timeEdit.setTime(some_time)# seteamos el valor del tiempo convertido a partir de la DB  

    #Funcion para registrar un nuevo tipo de prueba en la BD
    def anadirListaTipos(self):
        global iTipos

        text, okPressed = QtWidgets.QInputDialog.getText(MainWindow, "Guardar preset","Nombre del preset:", QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)
        seconds = QtCore.QTime(0, 0, 0).secsTo(self.timeEdit.time());

        table1 = [['nombre','nofichas','tiempo','ficha1','ficha2','ficha3','velocidad'],[text,self.spinBox_2.value(),seconds,self.comboBtnFicha1.currentIndex() +1,self.comboBtnFicha2.currentIndex() +1,self.comboBtnFicha3.currentIndex() +1,self.speedBox.value()]]
        etl.appenddb(table1, connection, 'tipos')

        item = QtWidgets.QListWidgetItem()
        self.listWidgetPresets.addItem(item)

        item = self.listWidgetPresets.item(iTipos)
        item.setText(text)

    #Funcion para mostrar el panel de configuraciones
    def configuraciones(self):
        self.stackedWidget.setCurrentIndex(6)
        self.llenarListaEmpresas()

    #Funcion que hace el query para llenar la lista de empresas de la BD
    def llenarListaEmpresas(self):
        global iEmpresa

        self.listEmpresas = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Exo")
        font.setPointSize(14)
        self.listEmpresas.setFont(font)
        self.listEmpresas.setObjectName("listEmpresas")

        empresas = etl.fromdb(connection, 'SELECT * FROM empresas')

        for empresa in etl.data(empresas):
            item = QtWidgets.QListWidgetItem()
            self.listEmpresas.addItem(item)

        self.horizontalLayout_3.addWidget(self.listEmpresas)

        __sortingEnabled = self.listEmpresas.isSortingEnabled()
        self.listEmpresas.setSortingEnabled(False)

        iEmpresa = 0
        for empresa in etl.data(empresas):
            item = self.listEmpresas.item(iEmpresa)
            item.setText(empresa[1])
            iEmpresa += 1

        self.listEmpresas.setSortingEnabled(__sortingEnabled)

    #Funcion que hace el query para llenar la lista de empresas de la BD
    def llenarListaTipos(self):
        global iTipos

        tipos = etl.fromdb(connection, 'SELECT * FROM tipos')

        for tipo in etl.data(tipos):
            item = QtWidgets.QListWidgetItem()
            self.listWidgetPresets.addItem(item)

        __sortingEnabled = self.listWidgetPresets.isSortingEnabled()
        self.listWidgetPresets.setSortingEnabled(False)

        iTipos = 0
        for tipo in etl.data(tipos):
            item = self.listWidgetPresets.item(iTipos)
            item.setText(tipo[1])
            iTipos += 1

        self.listWidgetPresets.setSortingEnabled(__sortingEnabled)

    #Funcion que cierra la aplicación
    def closeEvent(self):
        reply = QtWidgets.QMessageBox.question(MainWindow, 'Message',
            "Estas seguro de salir?", QtWidgets.QMessageBox.Yes |
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            connection.close()
            MainWindow.close()


class ThreadClass(QtCore.QThread):
    holi = QtCore.pyqtSignal(int)

    def __init__(self, parent = None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        global tiempoPrueba
        global tiempoTerminado
        for segundos in range(tiempoPrueba,-1,-1):
            #print ("Conteo: " + str(segundos))
            if segundos <= 0:
                stop="00000"
                arduino.write(stop.encode())
            self.holi.emit(segundos)
            self.sleep(1)
            #time.sleep(2)


        tiempoTerminado = True

import myresource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
