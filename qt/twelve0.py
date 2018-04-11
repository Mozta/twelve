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

mPiezasCorrectas = 0
mPiezasIncorrectas = 0
tiempoPrueba = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 781, 521))
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_bienvenida = QtWidgets.QWidget()
        self.page_bienvenida.setObjectName("page_bienvenida")
        self.layoutWidget = QtWidgets.QWidget(self.page_bienvenida)
        self.layoutWidget.setEnabled(True)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 430, 451, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(29)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPrueba = QtWidgets.QPushButton(self.layoutWidget)
        self.btnPrueba.setObjectName("btnPrueba")
        self.horizontalLayout.addWidget(self.btnPrueba)
        self.btnHistorial = QtWidgets.QPushButton(self.layoutWidget)
        self.btnHistorial.setEnabled(True)
        self.btnHistorial.setObjectName("btnHistorial")
        self.horizontalLayout.addWidget(self.btnHistorial)
        self.img_logo = QtWidgets.QLabel(self.page_bienvenida)
        self.img_logo.setGeometry(QtCore.QRect(290, 60, 200, 200))
        self.img_logo.setText("")
        self.img_logo.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.img_logo.setScaledContents(True)
        self.img_logo.setObjectName("img_logo")
        self.txt_logo = QtWidgets.QLabel(self.page_bienvenida)
        self.txt_logo.setGeometry(QtCore.QRect(250, 250, 281, 91))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.txt_logo.setFont(font)
        self.txt_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_logo.setObjectName("txt_logo")
        self.stackedWidget.addWidget(self.page_bienvenida)
        self.page_registro = QtWidgets.QWidget()
        self.page_registro.setObjectName("page_registro")
        self.txtNombre = QtWidgets.QTextEdit(self.page_registro)
        self.txtNombre.setGeometry(QtCore.QRect(240, 110, 361, 41))
        self.txtNombre.setObjectName("txtNombre")
        self.btnRegistrar = QtWidgets.QPushButton(self.page_registro)
        self.btnRegistrar.setGeometry(QtCore.QRect(550, 450, 171, 36))
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.label = QtWidgets.QLabel(self.page_registro)
        self.label.setGeometry(QtCore.QRect(160, 120, 63, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_registro)
        self.label_2.setGeometry(QtCore.QRect(160, 200, 63, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_registro)
        self.label_3.setGeometry(QtCore.QRect(160, 280, 63, 20))
        self.label_3.setObjectName("label_3")
        self.spinBoxEdad = QtWidgets.QSpinBox(self.page_registro)
        self.spinBoxEdad.setGeometry(QtCore.QRect(240, 270, 108, 36))
        self.spinBoxEdad.setObjectName("spinBoxEdad")
        self.comboBoxSexo = QtWidgets.QComboBox(self.page_registro)
        self.comboBoxSexo.setGeometry(QtCore.QRect(240, 190, 151, 36))
        self.comboBoxSexo.setObjectName("comboBoxSexo")
        self.comboBoxSexo.addItem("")
        self.comboBoxSexo.addItem("")
        self.stackedWidget.addWidget(self.page_registro)
        self.page_seleccion = QtWidgets.QWidget()
        self.page_seleccion.setObjectName("page_seleccion")

        self.frame = QtWidgets.QFrame(self.page_seleccion)
        self.frame.setGeometry(QtCore.QRect(20, 30, 276, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.listWidgetPresets = QtWidgets.QListWidget(self.frame)
        self.listWidgetPresets.setObjectName("listWidgetPresets")

        self.verticalLayout.addWidget(self.listWidgetPresets)

        self.btnSeleccionarTipo = QtWidgets.QPushButton(self.frame)
        self.btnSeleccionarTipo.setObjectName("btnSeleccionarTipo")

        self.verticalLayout.addWidget(self.btnSeleccionarTipo)
        self.btnAddPreset = QtWidgets.QPushButton(self.page_seleccion)
        self.btnAddPreset.setGeometry(QtCore.QRect(370, 440, 111, 36))
        self.btnAddPreset.setObjectName("btnAddPreset")
        self.label_5 = QtWidgets.QLabel(self.page_seleccion)
        self.label_5.setGeometry(QtCore.QRect(590, 150, 91, 20))
        self.label_5.setObjectName("label_5")
        self.spinBox_2 = QtWidgets.QSpinBox(self.page_seleccion)
        self.spinBox_2.setGeometry(QtCore.QRect(590, 180, 141, 36))
        self.spinBox_2.setObjectName("spinBox_2")
        self.timeEdit = QtWidgets.QTimeEdit(self.page_seleccion)
        self.timeEdit.setGeometry(QtCore.QRect(590, 300, 141, 36))
        self.timeEdit.setObjectName("timeEdit")
        self.label_6 = QtWidgets.QLabel(self.page_seleccion)
        self.label_6.setGeometry(QtCore.QRect(590, 270, 91, 20))
        self.label_6.setObjectName("label_6")
        self.btnRun = QtWidgets.QPushButton(self.page_seleccion)
        self.btnRun.setGeometry(QtCore.QRect(560, 440, 201, 36))
        self.btnRun.setObjectName("btnRun")
        self.comboBtnFicha1 = QtWidgets.QComboBox(self.page_seleccion)
        self.comboBtnFicha1.setGeometry(QtCore.QRect(330, 120, 191, 61))
        self.comboBtnFicha1.setObjectName("comboBtnFicha1")
        self.comboBtnFicha1.addItem("")
        self.comboBtnFicha1.addItem("")
        self.comboBtnFicha1.addItem("")
        self.comboBtnFicha2 = QtWidgets.QComboBox(self.page_seleccion)
        self.comboBtnFicha2.setGeometry(QtCore.QRect(330, 220, 191, 61))
        self.comboBtnFicha2.setObjectName("comboBtnFicha2")
        self.comboBtnFicha2.addItem("")
        self.comboBtnFicha2.addItem("")
        self.comboBtnFicha2.addItem("")
        self.comboBtnFicha3 = QtWidgets.QComboBox(self.page_seleccion)
        self.comboBtnFicha3.setGeometry(QtCore.QRect(330, 320, 191, 61))
        self.comboBtnFicha3.setObjectName("comboBtnFicha3")
        self.comboBtnFicha3.addItem("")
        self.comboBtnFicha3.addItem("")
        self.comboBtnFicha3.addItem("")

        self.stackedWidget.addWidget(self.page_seleccion)
        self.page_ejecucion = QtWidgets.QWidget()
        self.page_ejecucion.setObjectName("page_ejecucion")
        self.imgFicha1 = QtWidgets.QLabel(self.page_ejecucion)
        self.imgFicha1.setGeometry(QtCore.QRect(130, 30, 140, 140))
        self.imgFicha1.setText("")
        self.imgFicha1.setPixmap(QtGui.QPixmap("images/btnred.png"))
        self.imgFicha1.setScaledContents(True)
        self.imgFicha1.setObjectName("imgFicha1")
        self.imgFicha2 = QtWidgets.QLabel(self.page_ejecucion)
        self.imgFicha2.setGeometry(QtCore.QRect(130, 190, 140, 140))
        self.imgFicha2.setText("")
        self.imgFicha2.setPixmap(QtGui.QPixmap("images/btnblue.png"))
        self.imgFicha2.setScaledContents(True)
        self.imgFicha2.setObjectName("imgFicha2")
        self.imgFicha3 = QtWidgets.QLabel(self.page_ejecucion)
        self.imgFicha3.setGeometry(QtCore.QRect(130, 350, 140, 140))
        self.imgFicha3.setText("")
        self.imgFicha3.setPixmap(QtGui.QPixmap("images/btngreen.png"))
        self.imgFicha3.setScaledContents(True)
        self.imgFicha3.setObjectName("imgFicha3")
        self.frame_2 = QtWidgets.QFrame(self.page_ejecucion)
        self.frame_2.setGeometry(QtCore.QRect(420, 100, 291, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.lblTiempo = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTiempo.sizePolicy().hasHeightForWidth())
        self.lblTiempo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(77)
        self.lblTiempo.setFont(font)
        self.lblTiempo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTiempo.setWordWrap(False)
        self.lblTiempo.setObjectName("lblTiempo")
        self.gridLayout.addWidget(self.lblTiempo, 0, 0, 1, 1)
        self.btnStop = QtWidgets.QPushButton(self.page_ejecucion)
        self.btnStop.setGeometry(QtCore.QRect(610, 440, 92, 36))
        self.btnStop.setObjectName("btnStop")
        self.btnStart = QtWidgets.QPushButton(self.page_ejecucion)
        self.btnStart.setGeometry(QtCore.QRect(480, 260, 181, 61))
        self.btnStart.setObjectName("btnStart")
        self.btnFalso = QtWidgets.QPushButton(self.page_ejecucion)
        self.btnFalso.setGeometry(QtCore.QRect(350, 440, 211, 36))
        self.btnFalso.setObjectName("btnFalso")
        self.stackedWidget.addWidget(self.page_ejecucion)
        self.page_resultados = QtWidgets.QWidget()
        self.page_resultados.setObjectName("page_resultados")
        self.label_14 = QtWidgets.QLabel(self.page_resultados)
        self.label_14.setGeometry(QtCore.QRect(260, 30, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_resultados)
        self.label_15.setGeometry(QtCore.QRect(160, 160, 191, 20))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.page_resultados)
        self.label_16.setGeometry(QtCore.QRect(160, 280, 191, 20))
        self.label_16.setObjectName("label_16")
        self.lcdNumberWin = QtWidgets.QLCDNumber(self.page_resultados)
        self.lcdNumberWin.setGeometry(QtCore.QRect(440, 150, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lcdNumberWin.setFont(font)
        self.lcdNumberWin.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumberWin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberWin.setSmallDecimalPoint(False)
        self.lcdNumberWin.setDigitCount(2)
        self.lcdNumberWin.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumberWin.setProperty("intValue", 25)
        self.lcdNumberWin.setObjectName("lcdNumberWin")
        self.lcdNumberFail = QtWidgets.QLCDNumber(self.page_resultados)
        self.lcdNumberFail.setGeometry(QtCore.QRect(440, 250, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lcdNumberFail.setFont(font)
        self.lcdNumberFail.setFrameShape(QtWidgets.QFrame.Panel)
        self.lcdNumberFail.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumberFail.setSmallDecimalPoint(False)
        self.lcdNumberFail.setDigitCount(2)
        self.lcdNumberFail.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumberFail.setProperty("intValue", 5)
        self.lcdNumberFail.setObjectName("lcdNumberFail")
        self.btnReinicio = QtWidgets.QPushButton(self.page_resultados)
        self.btnReinicio.setGeometry(QtCore.QRect(210, 440, 131, 36))
        self.btnReinicio.setObjectName("btnReinicio")
        self.btnFinalizar = QtWidgets.QPushButton(self.page_resultados)
        self.btnFinalizar.setGeometry(QtCore.QRect(431, 440, 151, 36))
        self.btnFinalizar.setObjectName("btnFinalizar")
        self.stackedWidget.addWidget(self.page_resultados)
        self.page_historial = QtWidgets.QWidget()
        self.page_historial.setObjectName("page_historial")
        self.scrollArea = QtWidgets.QScrollArea(self.page_historial)
        self.scrollArea.setGeometry(QtCore.QRect(80, 60, 211, 211))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 207, 207))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidgetHistorial = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidgetHistorial.setObjectName("listWidgetHistorial")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetHistorial.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetHistorial.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetHistorial.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetHistorial.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetHistorial.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetHistorial.addItem(item)
        self.horizontalLayout_2.addWidget(self.listWidgetHistorial)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btnDelete = QtWidgets.QToolButton(self.page_historial)
        self.btnDelete.setGeometry(QtCore.QRect(460, 70, 36, 36))
        self.btnDelete.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelete.setIcon(icon)
        self.btnDelete.setObjectName("btnDelete")
        self.btnEdit = QtWidgets.QToolButton(self.page_historial)
        self.btnEdit.setGeometry(QtCore.QRect(510, 70, 36, 36))
        self.btnEdit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEdit.setIcon(icon1)
        self.btnEdit.setObjectName("btnEdit")
        self.btnExport = QtWidgets.QToolButton(self.page_historial)
        self.btnExport.setGeometry(QtCore.QRect(560, 70, 36, 36))
        self.btnExport.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExport.setIcon(icon2)
        self.btnExport.setObjectName("btnExport")
        self.stackedWidget.addWidget(self.page_historial)
        self.page_empresas = QtWidgets.QWidget()
        self.page_empresas.setObjectName("page_empresas")
        self.txtNombreEmpresa = QtWidgets.QTextEdit(self.page_empresas)
        self.txtNombreEmpresa.setGeometry(QtCore.QRect(350, 280, 361, 41))
        self.txtNombreEmpresa.setObjectName("txtNombreEmpresa")
        self.label_7 = QtWidgets.QLabel(self.page_empresas)
        self.label_7.setGeometry(QtCore.QRect(182, 290, 151, 20))
        self.label_7.setObjectName("label_7")
        self.btnRegistrar_2 = QtWidgets.QPushButton(self.page_empresas)
        self.btnRegistrar_2.setGeometry(QtCore.QRect(580, 550, 171, 36))
        self.btnRegistrar_2.setObjectName("btnRegistrar_2")
        self.label_8 = QtWidgets.QLabel(self.page_empresas)
        self.label_8.setGeometry(QtCore.QRect(270, 350, 63, 20))
        self.label_8.setObjectName("label_8")
        self.txtDireccionEmpresa = QtWidgets.QTextEdit(self.page_empresas)
        self.txtDireccionEmpresa.setGeometry(QtCore.QRect(350, 340, 361, 41))
        self.txtDireccionEmpresa.setObjectName("txtDireccionEmpresa")
        self.label_9 = QtWidgets.QLabel(self.page_empresas)
        self.label_9.setGeometry(QtCore.QRect(270, 410, 63, 20))
        self.label_9.setObjectName("label_9")
        self.spinBoxEmpresa = QtWidgets.QSpinBox(self.page_empresas)
        self.spinBoxEmpresa.setGeometry(QtCore.QRect(350, 400, 108, 36))
        self.spinBoxEmpresa.setObjectName("spinBoxEmpresa")
        self.btnGuardarEmpresa = QtWidgets.QPushButton(self.page_empresas)
        self.btnGuardarEmpresa.setGeometry(QtCore.QRect(611, 440, 131, 36))
        self.btnGuardarEmpresa.setObjectName("btnGuardarEmpresa")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_empresas)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 20, 731, 201))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 727, 197))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")



        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.btnSeleccionarEmpresa = QtWidgets.QPushButton(self.page_empresas)
        self.btnSeleccionarEmpresa.setGeometry(QtCore.QRect(610, 230, 131, 36))
        self.btnSeleccionarEmpresa.setObjectName("btnSeleccionarEmpresa")

        self.stackedWidget.addWidget(self.page_empresas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.actionInicio = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInicio.setIcon(icon3)
        self.actionInicio.setObjectName("actionInicio")
        self.actionInicio.setStatusTip('Regresar a inicio')
        self.actionInicio.triggered.connect(self.menu_inicio)

        self.actionConfiguraci_n = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/conf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfiguraci_n.setIcon(icon4)
        self.actionConfiguraci_n.setObjectName("actionConfiguraci_n")
        self.actionConfiguraci_n.setStatusTip('Configuraciones')
        self.actionConfiguraci_n.triggered.connect(self.configuraciones)

        self.actionSalir = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/exit24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon5)
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
        self.btnPrueba.clicked.connect(self.prueba)
        self.btnRegistrar.clicked.connect(self.registrarPersona)

        self.btnGuardarEmpresa.clicked.connect(self.anadirListaEmpresas)
        self.btnSeleccionarEmpresa.clicked.connect(self.seleccionarEmpresa)

        self.btnAddPreset.clicked.connect(self.anadirListaTipos)
        self.btnSeleccionarTipo.clicked.connect(self.seleccionarTipo)

        self.btnRun.clicked.connect(self.mostrarPrueba)
        self.btnStart.clicked.connect(self.ejecutarPrueba)
        #self.btnFalso.clicked.connect(self.ejecutarPrueba)

        self.btnReinicio.clicked.connect(self.reiniciarPrueba)
        self.btnFinalizar.clicked.connect(self.finalizarPrueba)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Twelve Technologies"))
        self.btnPrueba.setText(_translate("MainWindow", "Prueba"))
        self.btnHistorial.setText(_translate("MainWindow", "Historial"))
        self.txt_logo.setText(_translate("MainWindow", "twelve"))
        self.btnRegistrar.setText(_translate("MainWindow", "Siguiente"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.label_2.setText(_translate("MainWindow", "Sexo"))
        self.label_3.setText(_translate("MainWindow", "Edad"))
        self.comboBoxSexo.setItemText(0, _translate("MainWindow", "Masculino"))
        self.comboBoxSexo.setItemText(1, _translate("MainWindow", "Femenino"))
        self.label_4.setText(_translate("MainWindow", "Presets"))

        self.comboBtnFicha1.setItemText(0, _translate("MainWindow", "Rojo"))
        self.comboBtnFicha1.setItemText(1, _translate("MainWindow", "Verde"))
        self.comboBtnFicha1.setItemText(2, _translate("MainWindow", "Azul"))
        self.comboBtnFicha2.setItemText(0, _translate("MainWindow", "Rojo"))
        self.comboBtnFicha2.setItemText(1, _translate("MainWindow", "Verde"))
        self.comboBtnFicha2.setItemText(2, _translate("MainWindow", "Azul"))
        self.comboBtnFicha3.setItemText(0, _translate("MainWindow", "Rojo"))
        self.comboBtnFicha3.setItemText(1, _translate("MainWindow", "Verde"))
        self.comboBtnFicha3.setItemText(2, _translate("MainWindow", "Azul"))

        self.btnSeleccionarTipo.setText(_translate("MainWindow", "Seleccionar tipo de prueba"))
        self.btnAddPreset.setText(_translate("MainWindow", "Añadir preset"))
        self.label_5.setText(_translate("MainWindow", "No. Fichas"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "mm:ss"))
        self.label_6.setText(_translate("MainWindow", "Tiempo"))
        self.btnRun.setText(_translate("MainWindow", "Ejecutar"))
        self.lblTiempo.setText(_translate("MainWindow", "1:35"))
        self.btnStop.setText(_translate("MainWindow", "STOP"))
        self.btnStart.setText(_translate("MainWindow", "Inciar Prueba"))
        self.btnFalso.setText(_translate("MainWindow", "Insertar secuencia correcta"))
        self.label_14.setText(_translate("MainWindow", "Prueba finalizada"))
        self.label_15.setText(_translate("MainWindow", "Total de piezas correctas"))
        self.label_16.setText(_translate("MainWindow", "Total de piezas incorrectas"))
        self.btnReinicio.setText(_translate("MainWindow", "Reiniciar"))
        self.btnFinalizar.setText(_translate("MainWindow", "Finalizar"))
        __sortingEnabled = self.listWidgetHistorial.isSortingEnabled()
        self.listWidgetHistorial.setSortingEnabled(False)
        item = self.listWidgetHistorial.item(0)
        item.setText(_translate("MainWindow", "Prueba 1"))
        item = self.listWidgetHistorial.item(1)
        item.setText(_translate("MainWindow", "Prueba 2"))
        item = self.listWidgetHistorial.item(2)
        item.setText(_translate("MainWindow", "Prueba 3"))
        item = self.listWidgetHistorial.item(3)
        item.setText(_translate("MainWindow", "Prueba 4"))
        item = self.listWidgetHistorial.item(4)
        item.setText(_translate("MainWindow", "Prueba 5"))
        item = self.listWidgetHistorial.item(5)
        item.setText(_translate("MainWindow", "New Item"))
        self.listWidgetHistorial.setSortingEnabled(__sortingEnabled)
        self.btnSeleccionarEmpresa.setText(_translate("MainWindow", "Guardar empresa"))
        self.label_7.setText(_translate("MainWindow", "Nombre de la empresa"))
        self.btnRegistrar_2.setText(_translate("MainWindow", "Siguiente"))
        self.label_8.setText(_translate("MainWindow", "Dirección"))
        self.label_9.setText(_translate("MainWindow", "Surcursal"))
        self.btnGuardarEmpresa.setText(_translate("MainWindow", "Guardar empresa"))

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

    #Funcion para añadir el registro de una nueva prueba (datos de la persona)
    def registrarPersona(self):
        self.stackedWidget.setCurrentIndex(2)
        #print (self.txtNombre.toPlainText())
        #print (self.comboBoxSexo.currentText())
        #print (self.spinBoxEdad.value())

        #--------- BEGIN Registrar persona ------------
        #if self.comboBoxSexo.currentText() == 'Masculino' :
        #    sexo = 'm'
        #else :
        #    sexo = 'f'

        #table1 = [['nombre','sexo','edad'],[self.txtNombre.toPlainText(),sexo,self.spinBoxEdad.value()]]
        #etl.appenddb(table1, connection, 'personas')
        #--------- END Registrar persona ------------

        self.llenarListaTipos()
        #self.comboBoxSexo.text()
        #self.spinBoxEdad.text()

    #Funcion para cambiar al panel registro de prueba
    def mostrarPrueba(self):
        global tiempoPrueba

        self.stackedWidget.setCurrentIndex(3)

        tiempoPrueba = QtCore.QTime(0, 0, 0).secsTo(self.timeEdit.time());

        t = str(datetime.timedelta(seconds=tiempoPrueba))
        self.lblTiempo.setText(t[2:])

        #Cambiar contenido de elementos UI al tipo de prueba seleccionado
        self.cambiarFichas(midTipo)


    #Funcion para ejecutar prueba
    def ejecutarPrueba(self):
        global tiempoPrueba

        tiempoPrueba = QtCore.QTime(0, 0, 0).secsTo(self.timeEdit.time());

        for segundos in range(tiempoPrueba,-1,-1):
            self.actualizarEtiqueta(segundos)
            time.sleep(1)

        #Cuando el timer llega a 0 se cambia
        self.pruebaFinalizada()

    #Funcion que actualiza el la etiqueta timer
    def actualizarEtiqueta(self,seg):
        t = str(datetime.timedelta(seconds=seg))
        self.lblTiempo.setText(t[2:])
        self.lblTiempo.repaint()

    def cambiarFichas(self,tipo):
        tipos = etl.fromdb(connection, 'SELECT * FROM tipos')
        b = tipos.data()

        self.imgFicha1.setPixmap(QtGui.QPixmap(self.ponerImagenFicha(b[midTipo][4])))
        self.imgFicha2.setPixmap(QtGui.QPixmap(self.ponerImagenFicha(b[midTipo][5])))
        self.imgFicha3.setPixmap(QtGui.QPixmap(self.ponerImagenFicha(b[midTipo][6])))

    def ponerImagenFicha(self,img):
        if img == 1:
            return "images/btnred.png"
        elif img == 2:
            return "images/btngreen.png"
        else:
            return "images/btnblue.png"

    #Funcion cuando finaliza la prueba
    def pruebaFinalizada(self):
        self.stackedWidget.setCurrentIndex(4)

    #Funcion para cambiar al panel registro de prueba
    def reiniciarPrueba(self):
        self.stackedWidget.setCurrentIndex(3)

    #Funcion para cambiar al panel registro de prueba
    def finalizarPrueba(self):
        self.stackedWidget.setCurrentIndex(0)


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

    def seleccionarTipo(self):
        global midTipo
        a = self.listWidgetPresets.selectedIndexes()[0]
        midTipo = a.row()
        print (midTipo)
        tipos = etl.fromdb(connection, 'SELECT * FROM tipos')
        b = tipos.data()

        #Cambiar contenido de elementos UI al tipo de prueba seleccionado
        self.comboBtnFicha1.setCurrentIndex(b[midTipo][4] -1)
        self.comboBtnFicha2.setCurrentIndex(b[midTipo][5] -1)
        self.comboBtnFicha3.setCurrentIndex(b[midTipo][6] -1)

        self.spinBox_2.setValue(b[midTipo][2])
        x = b[midTipo][3]
        some_time = QtCore.QTime(0, 0, 0).addSecs(x);
        self.timeEdit.setTime(some_time)

    #Funcion para registrar un nuevo tipo de prueba en la BD
    def anadirListaTipos(self):
        global iTipos

        text, okPressed = QtWidgets.QInputDialog.getText(MainWindow, "Guardar preset","Nombre del preset:", QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)
        seconds = QtCore.QTime(0, 0, 0).secsTo(self.timeEdit.time());

        table1 = [['nombre','nofichas','tiempo','ficha1','ficha2','ficha3'],[text,self.spinBox_2.value(),seconds,self.comboBtnFicha1.currentIndex() +1,self.comboBtnFicha2.currentIndex() +1,self.comboBtnFicha3.currentIndex() +1]]
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

        #self.listWidgetPresets = QtWidgets.QListWidget(self.frame)
        #self.listWidgetPresets.setObjectName("listWidgetPresets")

        tipos = etl.fromdb(connection, 'SELECT * FROM tipos')

        for tipo in etl.data(tipos):
            item = QtWidgets.QListWidgetItem()
            self.listWidgetPresets.addItem(item)

        #self.horizontalLayout_3.addWidget(self.listWidgetPresets)

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
            MainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
