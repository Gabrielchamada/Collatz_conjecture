while True: ##this "while" is to make the program run until the user stops it
    number = int(input("Your positive integer: "))

    ##status information
    tries = 0
    even_number = 0
    odd_number = 0

    ##program
    if number <= 0:
        print("please insert a valid positive integer")
    else:
        while number != 1:
            print(number)
            if number % 2 == 0:
                number = number / 2 #step when number is even
                tries +=1
                even_number += 1
            else:
                number = 3 * number + 1 #step when number is odd
                tries +=1
                odd_number += 1
        print(number)

    ##status on screen
    print("-------STATUS-------")
    if number != 1:
        print("YOU FOUND A COUNTEREXAMPLE TO THE CONJECTURE OF COLLATZ, CONGRATS!") #This will probably never happen.
    else:
        print(tries, " tries until 1")
        print("Even numbers: ", even_number)
        print("Odd numbers: ", odd_number)
    print("--------------------")