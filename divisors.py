def find_divisors(number):
    
    divisors = [100]
   
    for i in range(1, number + 1):
        
        if number % i == 0:
            divisors.append(i)
    
    return divisors
