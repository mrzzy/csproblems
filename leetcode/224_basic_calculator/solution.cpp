/*
 * CSProblems
 * Leetcode
 * 224. Basic Calculator
 */

#include <algorithm>
#include <cctype>
#include <memory>
#include <pstl/glue_algorithm_defs.h>
#include <stack>
#include <stdexcept>
#include <string>
#include <utility>

using namespace std;

class Expr {
public:
  virtual int eval() const = 0;
  // define descructor since its relied upon by unique_ptr
  virtual ~Expr() = default;
};

class Constant : public Expr {
  int value;

public:
  Constant(int value) : value(value){};
  virtual int eval() const { return value; }
};

using ExprPtr = unique_ptr<Expr>;

class UnaryMinus : public Expr {
  ExprPtr operand;

public:
  UnaryMinus(ExprPtr operand) : operand(std::move(operand)) {}
  virtual int eval() const { return -operand->eval(); }
};

class Binary : public Expr {
  char op;
  ExprPtr left;
  ExprPtr right;

public:
  Binary(char op, ExprPtr left, ExprPtr right)
      : op(op), left(std::move(left)), right(std::move(right)) {}
  virtual int eval() const {
    switch (op) {
    case '+':
      return left->eval() + right->eval();
    case '-':
      return left->eval() - right->eval();
    }
    throw invalid_argument("bad op");
  }
};

class Solution {
public:
  int precedence(char op) {
    switch (op) {
    case '+':
    case '-':
    case '_':
      return 1;
    default:
      return 0;
    }
  }

  /* Parse the operator op using the given operands */
  void parseOp(char op, stack<ExprPtr> &operands) {
    if (op == '(')
      return;
    if (op == '_') {
      ExprPtr operand = std::move(operands.top());
      operands.pop();
      operands.push(make_unique<UnaryMinus>(std::move(operand)));
      return;
    }
    // binary operator
    ExprPtr right = std::move(operands.top());
    operands.pop();
    ExprPtr left = std::move(operands.top());
    operands.pop();
    operands.push(make_unique<Binary>(op, std::move(left), std::move(right)));
  }

  /* Parse the given infix into an expression for evaluation */
  ExprPtr parse(string s) {
    stack<ExprPtr> operands;
    stack<char> ops;
    string operand = "";

    // remove whitespace from string
    s.erase(remove(s.begin(), s.end(), ' '), s.end());

    for (int i = 0; i < s.size(); i++) {
      char c = s[i];
      if (isdigit(c)) {
        operand += c;
        continue;
      }
      // not an operand: parse any existing operand we are building
      if (operand.size() > 0) {
        operands.push(make_unique<Constant>(stoi(operand)));
        operand = "";
      }
      // c must be an operator
      if (c == '-' && (i <= 0 || s[i - 1] == '(')) {
        // unary minius: parse as underscore
        ops.push('_');
        continue;
      }
      if (c == '(') {
        ops.push('(');
        continue;
      }
      if (c == ')') {
        // parse until prior '('
        while (ops.top() != '(') {
          parseOp(ops.top(), operands);
          ops.pop();
        }
        // remove '('
        ops.pop();
        continue;
      }
      // evaluate any outstanding operators
      while (ops.size() > 0 && precedence(c) <= precedence(ops.top())) {
        parseOp(ops.top(), operands);
        ops.pop();
      }
      ops.push(c);
    }

    // parse any remaining operands & operators
    if (operand.size() > 0) {
      operands.push(make_unique<Constant>(stoi(operand)));
    }
    while (ops.size() > 0) {
      parseOp(ops.top(), operands);
      ops.pop();
    }

    return std::move(operands.top());
  }

  int calculate(string s) { return parse(s)->eval(); }
};
