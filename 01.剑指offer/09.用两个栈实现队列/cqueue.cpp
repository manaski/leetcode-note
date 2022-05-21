//
// Created by lifan on 2022/5/22.
//
#include <stack>
#include <iostream>

class CQueue {
 private:
  std::stack<int> instack, outstack;

 public:
  CQueue() {
  }

  void appendTail(int value) {
      instack.push(value);
  }

  int deleteHead() {
      if (!outstack.empty()) {
          int val = outstack.top();
          outstack.pop();
          return val;
      }

      if (instack.empty()) {
          return -1;
      }

      while (!instack.empty()) {
          outstack.push(instack.top());
          instack.pop();
      }

      int val = outstack.top();
      outstack.pop();

      return val;
  }
};

int main(int argc, char *argv[]) {
    CQueue *queue = new CQueue();

    queue->appendTail(1);
    queue->appendTail(2);
    queue->appendTail(3);

    std::cout << queue->deleteHead() << std::endl;
    std::cout << queue->deleteHead() << std::endl;
    std::cout << queue->deleteHead() << std::endl;
    std::cout << queue->deleteHead() << std::endl;

    return 0;
}