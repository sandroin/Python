import sys
import math
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from design import Ui_MainWindow


class MainWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # loadUi('calculator.ui', self)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.main)
        self.select.clicked.connect(self.select_shape)
        self.back.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main))
        self.calculate.clicked.connect(self.calculate_area)

    def select_shape(self):
        checked_button = self.shape_group.checkedButton()
        if not checked_button is None:
            self.stackedWidget.setCurrentWidget(
                getattr(self, f'{checked_button.objectName()}_page', self.main)
            )

    def calculate_area(self):
        if self.stackedWidget.currentWidget().objectName() == "main":
            return

        if self.shape_group.checkedButton().objectName() == "samkutxedi":
            side1 = self.s1.value()
            side2 = self.s2.value()
            side3 = self.s3.value()

            if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
                QMessageBox.warning(self, "არასწორი მონაცემები", "ასეთი სამკუთხედი არ არსებობს!")
                return

            p = (side1 + side2 + side3) / 2
            self.lcd_s_area.display(math.sqrt(p * (p - side1) * (p - side2) * (p - side3)))
            self.lcd_s_perimeter.display(2 * p)

        if self.shape_group.checkedButton().objectName() == "wre":
            radius = self.r1.value()
            self.lcd_r_area.display(math.pi * math.pow(radius, 2))
            self.lcd_r_perimeter.display(2 * math.pi * radius)

        if self.shape_group.checkedButton().objectName() == "trapecia":
            leg1 = self.leg1.value()
            leg2 = self.leg2.value()
            base1 = self.base1.value()
            base2 = self.base2.value()
            height = self.tr_height.value()

            # just for demonstration, no need to be too precise
            if base1 == 0 or base2 == 0 or leg1 == 0 or leg1 == 0 or height == 0:
                QMessageBox.warning(self, "არასწორი მონაცემები", "ასეთი ტრაპეცია არ არსებობს!")
                return

            self.lcd_tr_s.display(height * (base1 + base2) / 2)
            self.lcd_tr_p.display(leg1 + leg2 + base1 + base2)

        if self.shape_group.checkedButton().objectName() == "kvadrati":
            side = self.side.value()
            self.lcd_sq_s.display(side * side)
            self.lcd_sq_p.display(4 * side)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget()
    window.show()

    sys.exit(app.exec_())
