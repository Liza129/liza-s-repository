num = int(input("Enter a number: "))
even = [2,4,6,8,0]
odd = [1,3,5,7,9]
def collatz(n):
    response = 0
    if n in even:
        response = n//2
    elif n in odd:
        response = 3*n + 1
    return response
response = collatz(num)

while response != 1:
    response = collatz(response)
    print(response)
        
