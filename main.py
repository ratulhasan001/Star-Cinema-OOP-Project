class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, row, col, hall_no) -> None:
        super().__init__()
        self.__row = row
        self.__col = col
        self.__hall_no = hall_no
        self.__show_list = []
        self.__seats = {}
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        self.__seats[id] = [[0] * self.__col for _ in range(self.__row)]

    def view_show_list(self):
        print('_______Showing All Lists________')
        return self.__show_list

    def book_seats(self, id, seats):
        if id not in [show[0] for show in self.__show_list]:
            raise Exception(f'ID {id} is invalid!')
        
        for seat in seats:
            if seat[0] >= self.__row or seat[1] >= self.__col:
                raise Exception('Invalid Seat Number')
            elif self.__seats[id][seat[0]][seat[1]] == 1:
                raise Exception('Already Booked!')
            else:
                self.__seats[id][seat[0]][seat[1]] = 1

    def view_available_seats(self, id):
        if id not in [show[0] for show in self.__show_list]: 
            raise Exception(f'ID {id} is invalid!')
        
        for i in range(self.__row):
            for j in range(self.__col):
                print(self.__seats[id][i][j], end=" ")
            print()


hall = Hall(10, 10, 1)
hall.entry_show(1, "Avengers: Chicken Edition", "10-01-2024 12.00 PM")
hall.entry_show(2, "Avengers: Murga Dynasty", "10-01-2024 11.00 PM")
hall.entry_show(3, "Dr Chicken", "10-01-2024 10.00 PM")

while True:
    print("Welcome to MurgiPlex")
    print("Press 1 to check all the shows")
    print("Press 2 to view available seats")
    print("Press 3 to book ticket")
    print("Press 0 to terminate the booking")
    n = int(input("Please Enter The Command : "))

    if n == 1:
        print("Introducing our shows : ")
        print(hall.view_show_list())
    elif n == 2:
        id = int(input("Enter the ID : "))
        hall.view_available_seats(id)
    elif n == 3:
        id = int(input("Enter Show ID : "))
        total_tickets = int(input("Enter number of tickets you want to book"))
        for _ in range(total_tickets):
            x, y = map(int, input().split())
            x -= 1
            y -= 1
            seats = [(x, y)]
            hall.book_seats(id, seats)
    elif n == 0:
        break
    else:
        raise Exception('Invalid option chosen')
    print()
