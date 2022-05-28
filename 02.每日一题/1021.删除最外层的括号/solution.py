
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        left_cnt = 0
        right_cnt = 0

        ans = ""

        for c in s:
            if c == ')':
                right_cnt += 1

            if left_cnt != right_cnt:
                ans += c

            if c == '(':
                left_cnt += 1

        return ans
