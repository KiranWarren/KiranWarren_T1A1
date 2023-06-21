import math

prime_list = []

for i in range(1,101):
    prime_bool = True
    if i == 1:
        continue
    if 2 > math.sqrt(i):
        prime_list.append(i)
        continue
    for j in range(2,math.ceil(math.sqrt(i))+1):
        if i % j == 0:
            prime_bool = False
            break
    if prime_bool:
        prime_list.append(i)

print(prime_list)
