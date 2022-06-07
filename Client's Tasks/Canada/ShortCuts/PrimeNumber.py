# detect if a number is prime or not and also find the divisors of non prime numbers and stores them in dictionary
def PrimeRec(Num):
    prime = set()                   # set for storing prime numbers
    non_prime = dict()              # dictionary for storing non prime numbers and divisors
    flag = 1                        # flag for detecting non prime and prime numbers

    for x in Num:
        for i in range((x // 2), 2, -1):
            if x % i == 0:
                flag = 0            # it means this a non prime number
                non_prime[x] = [i]  # store this non prime number in dictionary
                break

        if flag == 1:               # it means this a prime number
            prime.add(x)            # add this prime number to set 'prime'
        flag = 1

    return prime, non_prime         # return both the set and dictionary of prime and non prime numbers
