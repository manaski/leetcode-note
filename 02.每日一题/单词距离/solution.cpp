//
// Created by lifan on 2022/5/27.
//

#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

class Solution {

 public:
  int findClosest1(vector<string>& words, string word1, string word2) {
      int idx1 = -1, idx2 = -1;
      int min_dist = INT_MAX;

      for (int i = 0; i < words.size(); ++i) {
          if (words[i] == word1) {
              idx1 = i;
          }
          if (words[i] == word2) {
              idx2 = i;
          }

          if (idx1 != -1 && idx2 != -1) {
              min_dist = min(min_dist, abs(idx1 - idx2));
          }
      }

      return min_dist;
  }

  int findClosest(vector<string>& words, string word1, string word2) {
      map<string, vector<int>> word_index_map;

      for (int idx = 0; idx < words.size(); idx ++) {
          if ((word_index_map.count(words[idx])) == 0) {
              word_index_map[words[idx]] = vector<int>();
          }

          word_index_map[words[idx]].push_back(idx);
      }

      vector<int> index1 = word_index_map[word1];
      vector<int> index2 = word_index_map[word2];

      if (index1.empty() || index2.empty()) {
          return -1;
      }

      int i = 0, j = 0;
      int min_dist = INT_MAX;

      while (i < index1.size() && j < index2.size()) {
          min_dist = min(min_dist, abs(index1[i] - index2[j]));
          if (index1[i] < index2[j]) {
              i++;
          } else {
              j++;
          }
      }

      return min_dist;
  }
};

int main(int argc, char *argv[])
{
    Solution s;
    vector<string> words = {"1", "2", "3", "4"};
    int ans = s.findClosest(words,"5", "6");
    cout << ans;

    return 0;
}
