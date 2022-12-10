def collatz(number):
    if number%2 == 0:
        return number//2 
    elif number%2 != 0:
        return number*3+1
    else:
        print('Something went wrong')
        return None


number = int(input('Whats the number? '))

while number != 1:
     number = collatz(number)
     print(number)

