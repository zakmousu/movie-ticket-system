class MovieTicket:
    def bookingPrice(self):
        while True:
            try:    
                age = int(input('How old are you? '))
                if 0 < age <= 12:
                    price = 5.00
                elif 12< age < 18:
                    price = 8.00
                elif 18 <= age < 64:
                    price = 12.00
                elif age >= 65:
                    price = 6.00
                else:
                    print('Invalid Input! Please enter your age.')
                    continue
                return price
            except ValueError:
                print('Invalid Input! Please enter your age: ')
    
    def bookingTime(self):
        while True:
            try:
                time = int(input('Enter 1 for the morning show \nEnter 2 for the afternoon show \nEnter 3 for the evening show\n'))
                if time == 1:
                    discountedPrice = 0.90
                elif time == 2:
                    discountedPrice = 0.95
                elif time == 3:
                    discountedPrice = 1.00
                else:
                    print('Invalid Input! Please enter a valid number.')
                    continue
                return discountedPrice
            except ValueError:
                print('Invalid Input! Please enter a valid number.')
    
    def priceCalculator(self):
        price = self.bookingPrice()
        discountedPrice = self.bookingTime()

        price = round((float(price * discountedPrice)), 2) 
        print(f'Your ticket price is EUR{price}')
    
def main():
    while True:
        ticket = MovieTicket()
        ticket.priceCalculator()
        choice = input('Enter \'Y\' to buy a new ticket or \'N\' to exit: ').upper()
        if choice == 'Y':
            continue
        elif choice == 'N':
            break
        else:
            print("Invalid choice! Please enter 'Y' or 'N'.")
            break            

if __name__ == "__main__":
    main()




