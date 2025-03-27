

def main():
    #variables and import math
    import math
    people = int(input("How many people are attending the cookout: "))
    hot_dogs = int(input("Enter the hot dogs each person will eat: "))
    hot_dog_buns = hot_dogs
    
    #constant integers 
    DOGS = people * hot_dogs
    BUNS = people * hot_dog_buns
    
    #math calculations 
    minDogs = math.ceil(DOGS/10)
    minBuns = math.ceil(BUNS/8)
    
    #packages of hot dog and buns needed
    hot_dog_packages_needed = minDogs * 10
    hot_dog_bun_packages_needed = minBuns * 8 

    #left over hot dogs and buns 
    hot_dog_leftover = hot_dog_packages_needed - DOGS
    hot_dog_buns_leftover = hot_dog_bun_packages_needed - BUNS
    
        
    # Display the minimum packages of hot dogs needed.
    print("Minimum packages of hot dogs needed: ", minDogs)
    # Display the minimum packages of buns needed.
    print("Minimum packages of hot dog buns needed: ", minBuns)
    
    # Display the number of hot dogs left over.
    print("hot dogs leftover: ", hot_dog_leftover)
    # Display the number of hot dog buns left over.
    print("hot dog buns leftover: ", hot_dog_buns_leftover)

main()