# モンテカルロ法
import random
import matplotlib.pyplot as plt
import math


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

    def __str__(self):
        return f"[{self.p_x}, {self.p_y}]"


# 総実行回数
sum = 10000
incircle_conut = 0
# 円の半径
radius = 1
for i in range(sum):
    plot = Plot(random.uniform(-1, 1), random.uniform(-1, 1))

    if plot.is_incircle(radius):
        incircle_conut += 1
        plt.plot(plot.p_x, plot.p_y, "bo", markersize=1)  # 円の内側の点は青色でプロット
    else:
        plt.plot(plot.p_x, plot.p_y, "ro", markersize=1)  # 円の外側の点は赤色でプロット
pi_approx = 4 * (incircle_conut / sum)
pi_actual = math.pi
diff_percent = abs((pi_approx - pi_actual) / pi_actual) * 100

print(f"pi={pi_approx}")
print(f"Diff = {diff_percent:.4f}%")

# 円の描画
center_x = 0
center_y = 0
circle = plt.Circle((center_x, center_y), radius, color="black", fill=False)
plt.gca().add_artist(circle)

# グラフの設定
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.gca().set_aspect("equal", adjustable="box")
plt.title(f"Monte Carlo Method \n(pi = {pi_approx} diff={diff_percent})")
plt.show()
