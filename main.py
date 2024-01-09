class Star_Cinema:
    __hall_list = []
    def entry_hall(self, hall):
        self.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, row, col, hall_no) -> None:
        super().entry_hall(self)
        self.__row = row
        self.__col = col
        self.__hall_no = hall_no
        self.__show_list = []
        self.__seats = {}
    
    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__seats = [[0]*self.__col] * self.__row

    def view_show_list(self):
        print('_______Showing All Lists________')
        return self.__show_list

    def book_seats(self, id, seats):
        pass
    def view_available_seats(self, id):
        pass

while True:
    pass