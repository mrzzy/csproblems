/*
 * Leetcode
 * 155. Min Stack
 */

#include <iostream>
#include <stack>

using namespace std;

class MinStack {
private:
  stack<int> values;
  stack<int> mins;

public:
  MinStack() {}

  void push(int val) {
    values.push(val);
    // only update min stack if new minimum set
    if (mins.empty() || val >= mins.top()) {
      mins.push(val);
    }
  }

  void pop() {
    // revert to old min if current min is removed
    if (mins.top() == values.top()) {
      mins.pop();
    }
    return values.pop();
  }

  int top() { return values.top(); }

  int getMin() { return mins.top(); }
};

int main(int argc, char *argv[]) {
  MinStack *obj = new MinStack();
  obj->push(-2);
  obj->push(0);
  obj->push(-3);
  cout << "min: " << obj->getMin() << endl;
  obj->pop();
  cout << "top:" << obj->top() << endl;
  cout << "min " << obj->getMin() << endl;
}
