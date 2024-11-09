def find_divisors(number):
    
    divisors = [100]
   
    for i in range(1, number + 1):
        
        if number % i == 0:
            divisors.append(i)
    
    return divisors


number = int(input("숫자를 입력하세요: "))

print(f"{number}의 약수는: {find_divisors(number)}")
