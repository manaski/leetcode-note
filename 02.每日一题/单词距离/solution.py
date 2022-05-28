from typing import List


class Solution:
    # 遍历一次
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        idx1 = -1
        idx2 = -1
        min_dist = -1

        for idx, word in enumerate(words):
            if word == word1:
                idx1 = idx
            if word == word2:
                idx2 = idx

            if idx1 != -1 and idx2 != -1:
                if min_dist == -1:
                    min_dist = abs(idx1 - idx2)
                    continue
                min_dist = min(min_dist, abs(idx1 - idx2))

        return min_dist

    # 带缓存
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        word_index_map = {}
        for idx, word in enumerate(words):
            if word in word_index_map:
                word_index_map[word].append(idx)
            else:
                word_index_map[word] = [idx]

        index1 = word_index_map[word1]
        index2 = word_index_map[word2]

        if len(index1) == 0 or len(index2) == 0:
            return -1

        idx1 = 0
        idx2 = 0
        min_dist = -1

        # 双指针移动的方法
        while idx1 < len(index1) and idx2 < len(index2):
            if min_dist == -1:
                min_dist = abs(index1[idx1] - index2[idx2])
            else:
                min_dist = min(min_dist, abs(index1[idx1] - index2[idx2]))

            if index1[idx1] < index2[idx2]:
                idx1 += 1
            else:
                idx2 += 1

        return min_dist
