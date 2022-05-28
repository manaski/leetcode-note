from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(sx: int, sy: int, tx: int, ty: int) -> int:
            m, n = len(forest), len(forest[0])
            q = deque([(0, sx, sy)])
            vis = {(sx, sy)}
            while q:
                d, x, y = q.popleft()
                if x == tx and y == ty:
                    return d
                for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if 0 <= nx < m and 0 <= ny < n and forest[nx][ny] and (nx, ny) not in vis:
                        vis.add((nx, ny))
                        q.append((d + 1, nx, ny))
            return -1

        trees = sorted((h, i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1)
        ans = preI = preJ = 0
        for _, i, j in trees:
            d = bfs(preI, preJ, i, j)
            if d < 0:
                return -1
            ans += d
            preI, preJ = i, j
        return ans


if __name__ == "__main__":
    forest = [[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]]
    s = Solution()
    print(s.cutOffTree(forest))
