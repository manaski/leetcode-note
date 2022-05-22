//
// Created by lifan on 2022/5/22.
//

#include <stack>
#include <iostream>

class MinStack {
 public:
  /** initialize your data structure here. */
  std::stack<int> _data, _min;

  MinStack() {
  }

  void push(int x) {
      _data.push(x);
      if (_min.empty()) {
          _min.push(x);
      } else if (_min.top() >= x) {
          _min.push(x);
      }
  }

  void pop() {
      if (_min.top() >= _data.top()) {
          _min.pop();
      }
      _data.pop();
  }

  int top() {
      return _data.top();
  }

  int min() {
      return _min.top();
  }
};

int main(int argc, char *argv[])
{
    MinStack s;
    s.push(4);
    std::cout << s.min() << std::endl;
    s.push(3);
    std::cout << s.min() << std::endl;
    s.push(2);
    std::cout << s.min() << std::endl;
    s.push(1);
    std::cout << s.min() << std::endl;

    return 0;
}