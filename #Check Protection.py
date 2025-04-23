#Check Protection
#Omar Carbajal
#4/22/25


def check_protection():
    # Input the amount
    amount = float(input("Enter the check amount: $"))
    
    # Format the amount to 2 decimal places
    formatted_amount = f"{amount:.2f}"
    
    # Create check-protected version with leading asterisks in a field of 10 characters
    protected_amount = f"{formatted_amount:*>10}"
    
    # Display the protected amount with position numbers
    print("Check-Protected Output:")
    print(protected_amount)
    

# Run the function
check_protection()

