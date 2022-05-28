#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
 public:
  vector<int> reversePrint(ListNode* head) {
      int length = 0;
      ListNode *ptr = head;
      while (ptr != nullptr) {
          length++;
          ptr = ptr->next;
      }

      vector<int> ret(length);

      while (head != nullptr) {
          ret[--length] = head->val;
          head = head->next;
      }

      return ret;
  }
};

