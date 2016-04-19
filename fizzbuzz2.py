dave = None
while dave is None:
    try:
        n = int(input("Please enter a positive integer value using only number characters:)"))
    
    except (ValueError, NameError):
        print("I'm sorry but that won't work :(")
        continue
    
    except n <= 0:
        print("Only numbers above 0 please :)")   
        
    
    
    
    else:    
        for i in range(1, (n+1)):
            if i % 5 == 0 and i % 3 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i) 
        break