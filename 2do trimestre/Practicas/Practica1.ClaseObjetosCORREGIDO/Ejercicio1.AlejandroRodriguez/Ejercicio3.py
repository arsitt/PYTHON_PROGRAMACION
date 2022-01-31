class Time():
    #Constructor que crea instancia de la clase
    def __init__ (self, sec, min, hour) -> None: #Variables
        self.__sec = sec
        self.__min = min
        self.__hour = hour

    #Getters como propiedades

    @property
    def sec(self):
        return self.__sec

    @property 
    def min(self):
        return self.__min

    @property 
    def hour(self):
        return self.__hour
    
    #Setters

    @sec.setter
    def base(self, sec):
        self.__sec = sec
        return sec
    
    @min.setter
    def altura(self, min):
        self.__min = min
        return min
    
    @hour.setter
    def hour(self, hour):
        self.__hour = hour
        return hour

    #Metodos 
    def showtimefull(self):
        return print(f'{self.__hour} hour {self.__min} min {self.__sec} secs.')
    
    def showtimemin(self):
        return print(f'{self.__min} min {self.__sec} secs.')
    
    def showtimesec(self):
        return print(f'{self.__sec} secs.')


a1 = Time(10,20,18)

a1.showtimefull()
a1.showtimemin()
a1.showtimesec()