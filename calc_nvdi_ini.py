import sys
from PyQt5 import QtWidgets, uic
from calc_nvdi_logica import Calc_ndvi

app = QtWidgets.QApplication(sys.argv)
MyApp = Calc_ndvi()
MyApp.show()
sys.exit(app.exec_())