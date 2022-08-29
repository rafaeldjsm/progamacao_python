def fizzBuzz(n):
    for i in range(1,n+1):
        if not((i % 3 == 0) or (i % 5 == 0)):
            print(i)
        else:
            if i % 15 == 0:
                print('FizzBuzz')
            elif i % 3 == 0:
                print('Fizz')
            else:
                print('Buzz')

if __name__ == '__main__':
    
    n = int(input().strip())

fizzBuzz(n)
