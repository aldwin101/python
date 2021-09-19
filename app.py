def input_num(numbers):
    for num in numbers:
        if (num%3==0 and num%5==0):
            print ("FizzBuzz")
        elif (num%3==0):
            print ("Fizz")
        elif (num%5==0):
            print ("Buzz")
        else:
            print ("Not divisible by 3 or 5 or 3 and 5.")

input_num([1, 18, 30, 50, 56, 90, 99, 54, 64, 44, 33, 14, 20, 26, 78])