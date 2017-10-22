import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLineEdit, QLabel

class Water:

    def set_min(self, min):
        self.__min_x = float(min)

    def set_max(self, max):
        self.__max_x = float(max)

    def set_interval(self, interval):
        self.__interval = float(interval)

    def set_iterations(self, iter):
        self.__iteration = float(iter)
        self.__medium_point = self.__min_x + (self.__max_x - self.__min_x) / 2

    def __piecewise_function(self, x_value):
        if self.__min_x <= x_value < self.__medium_point:
            return 1
        elif self.__medium_point <= x_value < self.__max_x:
            return 0

    def get_initial_array(self):
        current_value = self.__min_x
        values = []
        while current_value < self.__max_x:
            values.append(self.__piecewise_function(current_value))
            current_value += self.__interval
        return values

    def water_spreading(self):
        self.__f = open("text.txt", "w")
        z_array = self.get_initial_array()
        while self.__iteration > 0:
            for i in range(1, len(z_array)-1):
                z_array[i] = z_array[i] + 0.1*(z_array[i+1]+z_array[i-1]-2*z_array[i])
            z_array[0] = z_array[1]
            z_array[len(z_array)-1] = z_array[len(z_array)-2]
            self.__iteration -= 1

        for i in enumerate(z_array):
            self.__f.write(str(i) + '\n')
        self.__f.close()
        return z_array

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = Water()
        self.initUI()


    def initUI(self):

        runbtn = QPushButton("Run!", self)
        runbtn.move(90, 250)
        runbtn.clicked.connect(self.runButtonClicked)

        self.initQLables()
        self.initQLines()

        self.setGeometry(350, 350, 290, 350)
        self.setWindowTitle('Spreading')
        self.show()

    def initQLables(self):
        minlbl = QLabel("Min x:", self)
        minlbl.move(50, 25)

        maxlbl = QLabel("Max x:", self)
        maxlbl.move(50, 75)

        intlbl = QLabel("Interval:", self)
        intlbl.move(50, 125)

        itrlbl = QLabel("Number of iter.:", self)
        itrlbl.move(50, 175)
        #itrlbl.adjustSize()

        self.compl = QLabel("Waiting :)", self)
        self.compl.move(110, 300)

    def initQLines(self):
        min_value = QLineEdit(self)
        min_value.move(50, 50)
        min_value.textChanged[str].connect(self.minChanged)
        min_value.setText("0")

        max_value = QLineEdit(self)
        max_value.move(50, 100)
        max_value.textChanged[str].connect(self.maxChanged)
        max_value.setText("100")

        interval = QLineEdit(self)
        interval.move(50, 150)
        interval.textChanged[str].connect(self.intervalChanged)
        interval.setText("1")

        interations = QLineEdit(self)
        interations.move(50, 200)
        interations.textChanged[str].connect(self.iterationsChanged)
        interations.setText("10000")

    def minChanged(self, text):
        try:
            self.w.set_min(text)
        except:
            return

    def maxChanged(self, text):
        try:
            self.w.set_max(text)
        except:
            return

    def intervalChanged(self, text):
        try:
            self.w.set_interval(text)
        except:
            return

    def iterationsChanged(self, text):
        try:
            self.w.set_iterations(text)
        except:
            return

    def runButtonClicked(self):
        self.compl.setText("Computing")

        self.w.water_spreading()
        self.compl.setText("Done!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
