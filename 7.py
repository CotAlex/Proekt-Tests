n = int(input())
k = 0
for i in range(1 , int(n**0.5) + 1) :
    if n % i == 0 :
        k += 1
if k > 1 :
    print("Составное число")
else :
    print("Простое число")
