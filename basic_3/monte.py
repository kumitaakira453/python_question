# モンテカルロ法
import random


class Plot:
    """
    (x,y)の座標を指定してプロットするクラス
    """

    def __init__(self, p_x, p_y):
        self.p_x = p_x
        self.p_y = p_y

    def is_incircle(self, r):
        if self.p_x**2 + self.p_y**2 <= r**2:
            return True
        else:
            return False


# 総実行回数
sum = 10000000
incircle_conut = 0
# 円の半径
radius = 1
for i in range(sum):
    plot = Plot(random.random(), random.random())
    if plot.is_incircle(radius):
        incircle_conut += 1

print(f"pi={str(4*(incircle_conut/sum))}")
