#1.1 Implement a recursive function to calculate the factorial of a given number
def fact_rec(n):
  if (n == 1):
    return n 
  else:
    return n * fact_rec(n - 1)


# take input from the user
num = int(input("Enter a number: "))
# for direct assignment value
'''num=3'''

result = fact_rec(num)
print("The factorial of", num, "is", result)