import random
import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __str__(self):
        return f"({self.row},{self.column})"


# 最初は3✖️3
# mesh = [
#     [0, 1, 1],
#     [1, 0, 0],
#     [1, 1, 0],
# ]
row_num = 100
column_num = 100

# ランダムにmeshを作成する
mesh = [[random.randint(0, 1) for _ in range(column_num)] for _ in range(row_num)]
print(mesh)
visited = [[False for _ in range(len(mesh[0]))] for _ in range(len(mesh))]
# ブロックのまとまり
blocks = []


def search_true(row, col, block):
    # meshの外にいる or 値が0　or 過去に検索したときスキップ
    if (
        row < 0
        or row >= len(mesh)
        or col < 0
        or col >= len(mesh[0])
        or mesh[row][col] == 0
        or visited[row][col]
    ):
        return
    # 探索した点が1で過去に検索したことがない
    visited[row][col] = True
    block.append(Point(row, col))
    # 右検索
    search_true(row + 1, col, block)
    # 左検索
    search_true(row - 1, col, block)
    # 下検索
    search_true(row, col + 1, block)
    # 上検索
    search_true(row, col - 1, block)


# meshごとに探索を行う
for i in range(len(mesh)):
    for j in range(len(mesh[i])):
        # 1を見つけた　かつ　過去に閲覧していない
        if mesh[i][j] == 1 and not visited[i][j]:
            # 一つのブロック
            block = []
            search_true(i, j, block)
            blocks.append(block)

print(f"ブロックの数:{len(blocks)}")
block_counts = list(set([len(block) for block in blocks]))
block_counts.sort()
for block_count in block_counts:
    if block_count == 1:
        continue
    block_num = 0
    for block in blocks:
        if len(block) == block_count:
            block_num += 1
    print(f"{block_count}マスのブロックが{block_num}")


data_array = np.array(mesh)

# メッシュグラフの作成
plt.figure(figsize=(8, 6))
plt.pcolormesh(
    data_array, edgecolors="k", linewidth=0.1, cmap="gray"
)  # edgecolorsとlinewidthでグリッド線を追加
plt.colorbar()  # カラーバーを追加
plt.title("Mesh Graph")
plt.show()
