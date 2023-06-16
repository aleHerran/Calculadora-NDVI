####Importar librerias
import sys, math
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
###Llamado del archivo encargado de la interface (Creado en Qt Deisigner)
DialogUi, DialogType = uic.loadUiType("calc_nvdi_gui.ui")

###A continuación se crea la clase principal del conversor de temperatura, 
###la cual se denominará Calc_ndvi y heredará de las clases QMainWindow y UI MainWindow. (Estos nombres probienen del archivo cargado en la anterior línea)
class Calc_ndvi(DialogType, DialogUi):
    """
    Aplicación que calcula el valor los pixeles 
    """
###Se asigna una función a cada clase heredada del UI
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnConvertir.clicked.connect(self.btnConvetir_clicked)
        self.btnSalir.clicked.connect(self.btnSalir_clicked)
        self.btnLimpiar.clicked.connect(self.btnLimpiar_clicked)
        self.btnNormal.clicked.connect(self.btnNormal_clicked)


    def btnConvetir_clicked(self):
        """
        Realiza el cálculo indicado que se accionará al clickear 
        en el boton calcular llamando los datos del UI
        """
        try:
            fltRoj = float(self.txtRoja.text())
            fltInfRoj = float(self.txtInfr_roja.text())
            fltndvi = round(((fltInfRoj - fltRoj)/(fltInfRoj + fltRoj)),3)
            self.txtNDVI.setText(self.txtNDVI.text())
            self.txtNDVI.setText(str(fltndvi))

            
            if fltndvi < 0:
                self.txt_interp.setText('Áreas con superficies de agua, estructuras artificiales, rocas, nubes, nieve')
            elif fltndvi>=0 and fltndvi< 0.33:
                self.txt_interp.setText('Vegetación dispersa, praderas, vegetación enferma')
            elif fltndvi>=0.33 and fltndvi< 0.66:
                self.txt_interp.setText('Zonas de alta vegetación, bosques de zonas templadas y tropicales')
            elif fltndvi>=0.66 and fltndvi<=1:
                self.txt_interp.setText('Zonas de alta vegetación, vegetación muy sana')
        except:
            #print("El valor ingresado no es valido")
            QMessageBox.warning(self,"Validación","El valor ingresado no es valido")
            
    
    def btnNormal_clicked(self):
        """
        Función que permite realizar los calculos para normalizar los valores (0-255)
        """
        try:
            fltndvi = float(self.txtNDVI.text())
            ndvi_8b = (math.trunc((fltndvi*127)))+128
            self.txt_ndvi8b.setText(self.txt_ndvi8b.text())
            self.txt_ndvi8b.setText(str(ndvi_8b))
        
        except:
            QMessageBox.critical(self,"Validación","No debe modificar el valor de NDVI")
                        

    def btnLimpiar_clicked(self):
        """ 
        Función que limpia las cajas para volver a calcular el NDVI
        """
        self.txtInfr_roja.clear()
        self.txtRoja.clear()
        self.txtNDVI.clear()
        self.txt_interp.clear()
        self.txt_ndvi8b.clear()
    
    
    def btnSalir_clicked(self):
        """
        Función que cierra la herramienta
        """
        self.close()


        
