class Star_Cinema: # done
    __hall_list = [] 
    def entry_hall(self, hall):
        self.__hall_list.append(hall)

class Hall(Star_Cinema): # done
    def __init__(self, row, col, hall_no) -> None:
        super().entry_hall(self)
        self.__row = row
        self.__col = col
        self.__hall_no = hall_no
        self.__show_list = []
        self.__seats = {}
    
    def entry_show(self, id, movie_name, time): # done
        show = (id, movie_name, time)
        self.__show_list.append(show) 
        self.__seats = [[0]*self.__col] * self.__row

    def view_show_list(self): # done
        print('_______Showing All Lists________')
        return self.__show_list

    def book_seats(self, id, seats): # seats = user    seat = admin
        # exception vul val seat + id
        if id not in self.__show_list:
            raise Exception(f'ID {id} is invalid!')
        for check in seats: # age row pore col
            if(seats[0] > self.__row or seats[1] < self.__col):
                raise Exception(f'Invalid Seat Number')       
            elif(self.__seats[id][self.__seat[0]][self.__seat[1]] == 1):
                raise Exception('Invalid Seat Number!')     
            else:
                self.__seats[id][self.__seat[0]][self.__seat[1]] = 1
    
    def view_available_seats(self, id):
        if id not in self.__show_list:
            raise Exception(f'ID {id} is invalid!')
        for i in self.__row:
            for j in self.__col:
                print(self.__seats[id][i][j], end = " ")
            print()

hall = Hall(10, 10, 1)
hall.entry_show(1, "Avengers : Chicken Edition", "10-01-2024 12.00 PM")
hall.entry_show(2, "Avengers : Murga Dynasty", "10-01-2024 11.00 PM")
hall.entry_show(3, "Dr Chicken", "10-01-2024 10.00 PM")

while True:
    print("Welcome to MurgiPlex")
    print("Press 1 to check all the shows")
    print("Press 2 to view available seats")
    print("Press 3 to book ticket")
    print("Press 0 to terminate the booking")
    n = int(input("Please Enter The Command"))

    try:
        if n == 1 :
            # show list
            print("Introducing our shows : ")
            full_list = hall.__show_list()
            for individual in full_list:
                print(f'Movie ID : {individual[0]}  Movie Name : {individual[1]} Date & Time : {individual[2]}')
        elif n == 2 :
            # seat dekha id daoa 
            id = int(input("Enter the ID : "))
            hall.view_available_seats(id)

        elif n == 3 :
            # ticket book
            
            pass
        elif(n == 0) :
            # terminate program
            break
        else :
            raise Exception('invalid option choosen')
    except:
        print("Invalid option choosen! ")
