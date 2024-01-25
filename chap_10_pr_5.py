class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print(f"The name of the trian is {self.name}")    
        print(f"The seat abilabe in the train are {self.seats}")    
    
    def fareInfo(self):
        print(f"The price of the ticket is:  RS {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"your tiket has been booked your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Seat is not abilable in this trian ")    



intercity = Train("Intercity Express: 142055",180, 50) 
intercity.getstatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getstatus()

