class Time():

    def __init__ (self, sec, min, hour) -> None:
        self.__sec = sec
        self.__min = min
        self.__hour = hour
    
    def showtimefull(self):
        print(self.__hour, "hour :", self.__min, 'min :', self.__sec, 'secs.')
    
    def showtimemin(self):
        print(self.__min, 'min :', self.__sec, 'secs.')
    
    def showtimesec(self):
        print(self.__sec, 'secs.')

    def change(self):
        self.__hour = int(input("Enter new hour: "))
        self.__min = int(input("Enter new min: "))
        self.__sec = int(input("Enter new secs: "))

a1 = Time(10,20,18)

a1.showtimefull()
a1.change()
a1.showtimefull()