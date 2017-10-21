
class Water:

    def __init__(self):
        self.__f = open("text.txt", "w")
        try:
            self.__min_x = float(input("Enter min value of X: "))
            self.__max_x = float(input("Enter max value of X: "))
            self.__interval = float(input("Enter interval: "))
            self.__iteration = float(input("Enter required number of iterations: "))
            self.__medium_point = self.__min_x + (self.__max_x - self.__min_x) / 2
        except ValueError:
            print("You haven't entered the value or smth else :)\n")
            self.__init__()

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


if __name__ == "__main__":
    do_it = Water()
    do_it.water_spreading()
