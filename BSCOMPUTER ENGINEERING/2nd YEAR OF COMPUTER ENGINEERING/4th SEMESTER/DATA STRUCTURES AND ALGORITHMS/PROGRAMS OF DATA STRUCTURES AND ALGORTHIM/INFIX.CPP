#include <iostream>
#include <stack>
#include <algorithm>
#include <string>
using namespace std;
bool isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/');
}
int precedence(char op) {
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return 0;
}
string infixToPrefix(string infix) {
    stack<char> operators;
    string prefix;
    reverse(infix.begin(), infix.end());
    for (char& c : infix) {
        if (isalnum(c)) {
            prefix += c;
        } else if (c == ')') {
            operators.push(c);
        } else if (c == '(') {
            while (!operators.empty() && operators.top() != ')') {
                prefix += operators.top();
                operators.pop();
            }
            operators.pop(); // Discard the ')'
        } else if (isOperator(c)) {
            while (!operators.empty() && precedence(operators.top()) >= precedence(c)) {
                prefix += operators.top();
                operators.pop();
            }
            operators.push(c);
        }
    }
    while (!operators.empty()) {
        prefix += operators.top();
        operators.pop();
    }
    reverse(prefix.begin(), prefix.end());
    return prefix;
}
bool isValidInfix(string infix) {
    int openBrackets = 0;
    int closeBrackets = 0;
    for (char c : infix) {
        if (c == '(') {
            openBrackets++;
        } else if (c == ')') {
            closeBrackets++;
        }
    }
    return openBrackets == closeBrackets;
}
int main() {
    string infixExpression;
    cout << "Enter the infix expression: ";
    getline(cin, infixExpression);
    if (!isValidInfix(infixExpression)) {
        cout << "The infix expression is not valid." << endl;
        return 1;
    }
    string prefixExpression = infixToPrefix(infixExpression);
    cout << "Prefix expression: " << prefixExpression << endl;
    return 0;
}