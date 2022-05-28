//
// Created by lifan on 2022/5/25.
//
#include <string>
#include <vector>
#include <math.h>
#include <iostream>
#include <numeric>

using namespace std;

class Solution {
 public:
  int findSubstringInWraproundString(string p) {
      int k = 0;
      vector<int>  dp(26);

      int idx = 0;
      while (idx < p.length()) {
          if (idx > 0 && (p[idx] - p[idx - 1] + 26) % 26 == 1) {
              k++;
          } else {
              k = 1;
          }
          dp[p[idx] - 'a'] = max(dp[p[idx] - 'a'], k);
          idx++;
      }

      return accumulate(dp.begin(), dp.end(), 0);
  }
};

int main(int argc, char *argv[])
{
    Solution s;
    cout << s.findSubstringInWraproundString("abc");

    return 0;
}

