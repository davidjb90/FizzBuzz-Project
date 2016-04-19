import sys

print("The name of this script is {}".format(sys.argv[0]))
print("User supplied {} arguments at run time".format(len(sys.argv)))

print("sys.argv:", sys.argv)

if len(sys.argv) == 1:
    while True:
        try:
            n = int(input("Please enter a positive integer value using only number characters:)"))
            if n <= 0:
                print("Only numbers above 0 please :)")
                continue

        except (ValueError, NameError):
            print("I'm sorry but that won't work :(")

        else:
            break 

n = int(sys.argv[1])
for i in range(1, (n+1)):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 