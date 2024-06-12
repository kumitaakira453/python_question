import time


def gcd(num1, num2):
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i


def lcm(num1, num2):
    for i in range(max(num1, num2), num1 * num2 + 1):
        if i % num1 == 0 and i % num2 == 0:
            return i


num1 = int(input("NUM1: "))
num2 = int(input("NUM2: "))

start_time = time.time()
# 最大公約数
gcd = gcd(num1, num2)
print(f"{num1}と{num2}の最大公約数:{gcd}")

# 最小公倍数
lcm = lcm(num1, num2)
print(f"{num1}と{num2}の最小公倍数{lcm}")
end_time = time.time()

elapsed_time = end_time - start_time
print(f"実行時間:{elapsed_time}ミリ秒")
