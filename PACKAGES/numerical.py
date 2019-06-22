#function to check if number is prime
def isprime(num):
    if num ==2:
        return True
    for i in range(2, num//2 +1):
        if num%i == 0:
            return False
    return True

#function to determine number of prime factors for a given number
def numberOfPrimeFactors(number):
    if isprime(number):
        return 1
    count = 0
    for i in range(2, number//2 +1):
        if isprime(i) and number%i ==0:
            count+=1
    return count