//
// Created by lifan on 2022/5/22.
//
#include <unordered_map>
#include <iostream>

class Solution {
  std::unordered_map<int, bool> mem;

 private:
  bool df(int usedNums, int currentTotal, int maxChoosableInteger, int desiredTotal) {
      if (mem.count(usedNums) == 0) {
          bool res = false;
          for (int i = 0; i < maxChoosableInteger; ++i) {
              if (((usedNums >> i) & 1) == 0) {
                  if (currentTotal + i + 1 >= desiredTotal ||
                      !df(usedNums | 1 << i, currentTotal + i + 1, maxChoosableInteger, desiredTotal)) {
                      res = true;
                      break;
                  }
              }
          }
          mem[usedNums] = res;
      }

      return mem[usedNums];
  }

 public:
  bool canIWin(int maxChoosableInteger, int desiredTotal) {
      //如果所有数加起来都比期望小
      if ((1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal) {
              return false;
      }

      return df(0, 0, maxChoosableInteger, desiredTotal);
  }
};

int main() {
    Solution *s = new Solution();
    std::cout << s->canIWin(4, 6);
}