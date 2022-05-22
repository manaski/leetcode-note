from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache  # 开启缓存
        def df(usedNums: int, currentTotal: int) -> bool:
            for i in range(maxChoosableInteger):
                if (usedNums >> i) & 1 == 0:
                    if currentTotal + i + 1 >= desiredTotal or not df(usedNums | 1 << i, currentTotal + i + 1):
                        return True
            return False

        return (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and df(0, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.canIWin(10, 11))
