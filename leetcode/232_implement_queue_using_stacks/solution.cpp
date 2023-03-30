/*
 * CSProblems
 * Leetcode
 * 232. Implement Queue using Stacks
 */

#include <algorithm>
#include <iostream>
#include <stack>

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
class MyQueue {
private:
  // stack acting as stack
  std::stack<int> stack_stack;
  // stack acting as queue
  std::stack<int> queue_stack;

  // Move elements from stack to stack
  void move(std::stack<int> &fromStack, std::stack<int> &toStack) {
    while (!fromStack.empty()) {
      toStack.push(fromStack.top());
      fromStack.pop();
    }
  
  }
public:
  MyQueue() {}

  void push(int x) {
    move(queue_stack, stack_stack);
    stack_stack.push(x);
  }

  int pop() {
    move(stack_stack, queue_stack);
    int value = queue_stack.top();
    queue_stack.pop();
    return value;
  }

  int peek() {
    move(stack_stack, queue_stack);
    return queue_stack.top();
  }

  bool empty() {
    return std::max(stack_stack.size(), queue_stack.size()) <= 0;
  }
};

int main() {
  MyQueue q;
  q.push(1);
  q.push(2);
  std::cout << q.pop() << std::endl;
  q.push(3);
  std::cout << q.pop() << std::endl;
  std::cout << q.pop() << std::endl;
}
