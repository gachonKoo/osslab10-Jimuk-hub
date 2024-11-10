import sys

def find_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(str(i))
    return divisors

if __name__ == "__main__":
    number = int(sys.argv[1])
    divisors = find_divisors(number)
    print(" ".join(divisors))
