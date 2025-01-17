# movie-ticket-system

Technical Features Used and Learned in the Movie Ticket Class:
Class Definition (class MovieTicket):

We used a class to represent the movie ticket booking system. A class allows you to organize related functions (methods) together, improving code readability and structure.
Methods within a Class:

def bookingPrice(self) and def bookingTime(self):
These methods handle the core functionality of the ticket booking system: determining the ticket price based on age and applying a discount based on the chosen showtime.
Methods are defined with the self parameter, which refers to the instance of the class. This allows the method to access attributes and other methods within the same class.
Input Handling:

We used the input() function to collect user input for age and showtime selection. Since user input is always returned as a string, we used int() to convert input to integers when appropriate, such as for age and time choices.
Exception Handling (try-except):

try-except blocks were used to catch invalid inputs and ensure that the program does not crash if non-numeric values are entered when asking for age or showtime.
ValueError is caught when the input cannot be converted to an integer.
If an invalid input is detected, the program prints an error message and prompts the user to enter valid data again.
Control Flow (if-elif-else):

We used if-elif-else statements to apply the correct logic based on the user's input:
Age-based conditions to assign the correct ticket price.
Showtime selection to apply the appropriate discount.
Handling of invalid inputs where the user is prompted to re-enter the data.
While Loops:

We used while True loops to continuously ask for valid input from the user until a valid response is given.
The loop allows the program to retry input if a user provides an incorrect age or showtime, making the program more user-friendly.
The program keeps running until the user decides to exit by entering 'N'.
String Methods:

upper(): This method was used to ensure the user input (Y or N) is case-insensitive. It converts the input string to uppercase, allowing the user to input 'y', 'Y', 'n', or 'N' to proceed.
Floating Point Calculations:

In priceCalculator(), the program calculated the final ticket price after applying the appropriate discount. The round() function was used to round the result to two decimal places for better presentation of the final ticket price.
Return Statements:

The return keyword was used to return values from methods (such as price and discountedPrice), which are then used in other parts of the program (such as calculating the final ticket price).
The main() Function:

The main() function serves as the entry point for the program. It orchestrates the flow by calling the MovieTicket class methods and looping to allow multiple purchases. It uses a while loop to repeatedly offer the user the choice to buy another ticket or exit.
Summary:
By working on this class, you’ve used several key programming concepts like classes, methods, input validation, exception handling, conditional logic, loops, and floating-point arithmetic. These features provide a solid foundation for building more complex programs and handling user input effectively.
