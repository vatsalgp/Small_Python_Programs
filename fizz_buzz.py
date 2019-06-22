# FizzBuzz

for num in range(1,31):
    string = str(num)
    if(num%3==0):
        string="Fizz"
    if(num%5==0):
        string="Buzz"
    if(num%15==0):
        string="FizzBuzz"
    print(string)

for num in range(1,31):
    string = ""
    if(num%3==0):
        string+="Fizz"
    if(num%5==0):
        string+="Buzz"
    if(string==""):
        string = str(num)
    print(string)

for num in range(1,31):
    if(num%3==0 and num%5==0):
        print("FizzBuzz")
    elif (num%3==0):
        print("Fizz")
    elif (num%5==0):
        print("Buzz")
    else:
        print(num)
