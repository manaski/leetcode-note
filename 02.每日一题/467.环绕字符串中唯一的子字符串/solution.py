from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        self.sub_string_map = {}  # 以字符c结尾长度已知子串的最大长度
        self.sub_length_map = {}  # idx位置向前有多少非空的子串
        self.total_sub_num = 0

    def findSubstring(self, p: str, idx: int):
        c = p[idx]  # 单字符
        if not c in self.sub_string_map:
            self.sub_string_map[c] = 1
            self.total_sub_num += 1

        if idx == 0:
            self.sub_length_map[idx] = 1

        if idx > 0:
            if (ord(p[idx]) - ord(p[idx - 1])) % 26 == 1:
                pre_length = self.sub_length_map[idx - 1]
                self.sub_length_map[idx] = pre_length + 1

                found_len = 0
                if c in self.sub_string_map:  # 之前发现过以c结尾的子串
                    found_len = self.sub_string_map[c]

                if found_len < pre_length + 1:
                    self.total_sub_num += pre_length + 1 - found_len
                    self.sub_string_map[c] = pre_length + 1

            else:
                self.sub_length_map[idx] = 1

    def findSubstringInWraproundString(self, p: str) -> int:
        for idx in range(len(p)):
            self.findSubstring(p, idx)

        return self.total_sub_num


class Solution2:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        k = 0
        for i, ch in enumerate(p):
            if i > 0 and (ord(ch) - ord(p[i - 1])) % 26 == 1:  # 字符之差为 1 或 -25
                k += 1
            else:
                k = 1
            dp[ch] = max(dp[ch], k)
        return sum(dp.values())


if __name__ == "__main__":
    s = Solution()
    print(s.findSubstringInWraproundString("zab"))
