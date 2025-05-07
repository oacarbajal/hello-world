#Omar Carbajal
# Module 12 Lab 
# # Define the Pet class


# Define the Pet class
class Pet:
    def __init__(self, name="", type_="", age=0):
        # Initialize pet attributes: name, type, and age
        self.name = name
        self.type = type_
        self.age = age

# Main function to interact with the user
def main():
    # Prompt the user for pet details
    name = input("Enter a pet name: ")
    type_ = input("Enter a pet type: ")
    age = int(input("Enter a pet age: "))

    # Create a Pet object using the input values
    pet = Pet(name, type_, age)

    # Display the pet's details
    print(f"The pet name is {pet.name}")
    print(f"The pet type is {pet.type}")
    print(f"The pet age is {pet.age}")

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()