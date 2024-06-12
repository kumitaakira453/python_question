num = int(input("数字を入力してください"))

is_prime = True
for i in range(2, num):
    if num % i == 0:
        print("素数ではないです")
        is_prime = False
        break
    else:
        continue

if is_prime:
    print("素数です")
