
struct ListNode {
  ListNode() {
  }
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
 public:
  ListNode *reverseList(ListNode *head) {
      if (head == nullptr or head->next == nullptr) {
          return head;
      }

      ListNode *hnode = new ListNode();

      while (head != nullptr) {
          ListNode *next = head->next;
          head->next = hnode->next;
          hnode->next = head;
          head = next;
      }

      return hnode->next;
  }
};

