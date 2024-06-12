base = int(input("BASE: "))
num = int(input("NUM: "))

index = 0
while True:
    if base**index >= num:
        break
    index += 1

for i in range(index, -1, -1):
    quotient = num // (base**i)
    num = num % (base**i)
    if i == index and quotient == 0:
        continue
    print(quotient, end=" ")

print(f"({base})")
