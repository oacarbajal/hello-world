# Lab 8 Palindrome
# Omar Carbajal
#4/9/25

#defining main
def main():


    def is_palindrome(s):
    # Create an empty list to use as a stack
        stack = []
    
    # Preprocess the string to ignore case, spaces, and punctuation
        filtered_s = ''.join([c.lower() for c in s if c.isalnum()])

    # Push all characters of the processed string onto the stack
        for character in filtered_s:
            stack.append(character)

    # Check if the characters pop from the stack match the characters in the processed string
        for character in filtered_s:
            if stack.pop() != character:
                return False

        return True

    # Prompt to input string to check for palindrome. 
    input_string = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(input_string):
        print("The string is a palindrome!")
    else:
        print("The string is not a palindrome.")

#calling main
main()    