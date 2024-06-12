import time


def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def lcm(num1, num2):
    return num1 * num2 // gcd(num1, num2)


num1 = int(input("NUM1: "))
num2 = int(input("NUM2: "))

start_time = time.time()


# 最大公約数
gcd_num = gcd(num1, num2)
print(f"{num1}と{num2}の最大公約数:{gcd_num}")

# 最小公倍数
lcm_num = lcm(num1, num2)
print(f"{num1}と{num2}の最小公倍数:{lcm_num}")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"実行時間:{elapsed_time}ミリ秒")
