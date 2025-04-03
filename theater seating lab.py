#Omar Carbajal
#4/2/2025
#Theater Seating Lab

def main():
    print()
    # These are the variables
    section_a_cost = 20
    section_b_cost = 15
    section_c_cost = 10

    # Input validation function
    def get_valid_input(prompt, min_val, max_val):
        while True:
            try:
                value = int(input(prompt))
                if min_val <= value <= max_val:
                    return value
                else:
                    print("Please enter a valid integer.")
            except ValueError:
                print("Error: Please enter a valid integer.")

    # This section requests seat input and quantity from the user
    seatA = get_valid_input("Input number of tickets sold in Section A: ", 0, 300)
    seatB = get_valid_input("Input number of tickets sold in Section B: ", 0, 500)
    seatC = get_valid_input("Input number of tickets sold in Section C: ", 0, 200)
    if seatA < 0 or seatA > 300:
        print("Input Section A must be between 0 - 300!")
    elif seatB < 0 or seatB > 500:
        print("Input Section B must be between 0 - 500!")
    elif seatC < 0 or seatC > 200:
        print("Input Section C must be between 0 - 200!")
    else:
        # This section calculates the total income amount
        income = (seatA * section_a_cost) + (seatB * section_b_cost) + (seatC * section_c_cost)
   
#this section prints the total income from ticket sales
        print("Total income from ticket sales: $" + str(income))
# this section calls for the main.
main()