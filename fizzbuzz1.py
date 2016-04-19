num = input("Please enter an integer value that you would like FizzBuzz to count to:")
while True
try:
    int(num)
except ValueError:
    print("I'm sorry but please enter an integer value using only number characters :)")
else:    
    for i in range(1, (num+1)):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
