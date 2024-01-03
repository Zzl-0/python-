'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
'''
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


def dfs(grid, x, y):
    grid[x][y] = "0"
    hang, lie = len(grid), len(grid[0])
    for h, l in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0<= h < hang and 0 <= l < lie and grid[h][l] == "1":
            dfs(grid, h, l)


def numIsLans(grid):
    hang, lie = len(grid), len(grid[0])
    if hang == 0:
        return
    nums = 0
    for x in range(hang):
        for y in range(lie):
            if grid[x][y] == "1":
                nums += 1
                dfs(grid, x, y)

    return nums

print(numIsLans(grid))

