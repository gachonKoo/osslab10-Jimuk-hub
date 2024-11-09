def find_divisors(number):
   
    divisors = []
    
   
    for i in range(1, number + 1):
      
        if number % i == 0:
            divisors.append(i)
    
   
    return divisors


try:
    number = int(input("숫자를 입력하세요: "))
    
  
    print(f"{number}의 약수는: {find_divisors(number)}")
except ValueError:
    print("올바른 숫자를 입력해주세요.")
