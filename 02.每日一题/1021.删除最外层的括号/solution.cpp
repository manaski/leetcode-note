#include <string>

using namespace std;

class Solution {
 public:
  string removeOuterParentheses(string s) {
      string res;
      int left_cnt = 0, right_cnt = 0;

      for (char c : s) {
          if (c == ')') {
              right_cnt++;
          }

          if (left_cnt != right_cnt) {
              res.push_back(c);
          }

          if (c == '(') {
              left_cnt++;
          }
      }

      return res;
  }
};
